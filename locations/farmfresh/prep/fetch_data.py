import json
import pandas as pd
import requests
import sys
import yaml
import os
import logging.handlers
import re
from datetime import datetime


## Notes
# API docs: https://www.usdalocalfoodportal.com/fe/datasharing/
#
# All known market type endpoints:
MARKET_TYPES = [
    "farmersmarket",
    "onfarmmarket",
    "csa",
    "foodhub",
    "cooperative",
]

# The USDA API misroutes these 2-letter codes — use full state name instead.
STATE_API_PARAM = {
    "AR": "Arkansas",
    "IA": "Iowa",
    "ID": "Idaho",
    "IN": "Indiana",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "OR": "Oregon",
    "RI": "Rhode Island",
    "UT": "Utah",
    "VA": "Virginia",
    "WA": "Washington",
}


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
curr_file_dir = os.path.dirname(__file__)
logger_file_handler = logging.handlers.RotatingFileHandler(
    os.path.join(curr_file_dir, "status.log"),
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


def fetch_usda_markets(api_key, state, market_type="farmersmarket"):
    """Fetch listings from the USDA Local Food Portal API for a given state and market type."""
    url = "https://www.usdalocalfoodportal.com/api/" + market_type + "/"
    params = {
        "apikey": api_key,
        "state": STATE_API_PARAM.get(state, state)
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        logger.error(f"Failed to fetch {market_type} for {state}: {response.status_code}")
        return []


def update_column_names(data_df):
    columns_map = {
        "directory_name"    : "Type",
        "updatetime"        : "ModifyDate",
        "listing_id"        : "ListingID",
        "listing_name"      : "Name",
        "listing_image"     : "Image",
        "listing_desc"      : "Description",
        "contact_name"      : "ContactName",
        "contact_email"     : "ContactEmail",
        "contact_phone"     : "ContactPhone",
        "media_website"     : "Website",
        "media_facebook"    : "Facebook",
        "media_twitter"     : "Twitter",
        "media_instagram"   : "Instagram",
        "media_pinterest"   : "Pinterest",
        "media_youtube"     : "Youtube",
        "media_blog"        : "Blog",
        "location_street"   : "Street",
        "location_city"     : "City",
        "location_state"    : "State",
        "location_zipcode"  : "Zip",
        "location_address"  : "Address",
        "location_x"        : "Longitude",
        "location_y"        : "Latitude",
        "brief_desc"        : "Tags",
    }
    data_df.columns = data_df.columns.astype(str)
    data_df = data_df.drop(columns=data_df.columns[data_df.columns.str.contains('^Unnamed')])
    df = data_df.rename(columns=columns_map).reset_index(drop=True)
    df = df.drop(columns=['distance', 'mydesc', 'term', 'directory_type'], errors='ignore')
    # Rename any remaining snake_case columns to CamelCase
    def snake_to_camel(name):
        return ''.join(word.capitalize() for word in name.split('_'))
    df.columns = [snake_to_camel(c) if '_' in c else c for c in df.columns]
    return df


def split_tags_column(data_df):
    """Split the Tags column into Dates and Products columns."""
    if 'Tags' in data_df.columns:
        data_df['Tags'] = data_df['Tags'].fillna('').astype(str)

        date_pattern = r'Open:\s*(.*?)(?:;\s*<br>|;|\s*<br>Available Products:|$)'
        products_pattern = r'Available Products:\s*(.*)'

        data_df['Dates'] = data_df['Tags'].str.extract(date_pattern, expand=False)
        products = data_df['Tags'].str.extract(products_pattern, expand=False)
        data_df['Products'] = products.fillna('').apply(
            lambda x: ', '.join([item.strip() for item in x.split(';') if item.strip()])
        )
        data_df = data_df.drop(columns=['Tags'], errors='ignore')
    return data_df


def clean_name_column(data_df):
    """Convert all-caps names to Title Case and replace L.L.C. with LLC."""
    if 'Name' in data_df.columns:
        data_df['Name'] = data_df['Name'].fillna('').astype(str)
        data_df['Name'] = data_df['Name'].apply(lambda x: x.title() if x.isupper() else x)
        data_df['Name'] = data_df['Name'].str.replace('L.L.C.', 'LLC', regex=False)
    return data_df


def export_data(state):
    """Fetch all market types for a state and return a single combined DataFrame."""
    try:
        apikey = os.environ["USDA_FARMFRESH_API"]
    except KeyError:
        logger.error("API key not available! Set the USDA_FARMFRESH_API environment variable.")
        sys.exit(1)

    frames = []
    for market_type in MARKET_TYPES:
        records = fetch_usda_markets(apikey, state, market_type)
        if records:
            frames.append(pd.DataFrame.from_dict(records))

    if not frames:
        logger.warning(f"No data found for state: {state}")
        return pd.DataFrame()

    combined = pd.concat(frames, ignore_index=True)
    combined = update_column_names(combined)
    combined = split_tags_column(combined)
    combined = clean_name_column(combined)
    return combined


def export_all_states(states=None, include_json_yaml=False):
    """Export farmfresh data for each state as a single combined CSV.

    Args:
        states: list of 2-char state codes, or None to use state_list.txt
        include_json_yaml: set True to also write .json and .yaml files
    """
    export_dir = os.path.join(curr_file_dir, "../us")
    logger.info(f"Exporting to directory: {export_dir}")

    if not os.path.exists(export_dir):
        os.mkdir(export_dir)

    if states is None:
        state_list_path = os.path.join(curr_file_dir, "state_list.txt")
        with open(state_list_path) as f:
            states = f.read().split()

    for state in states:
        curr_state_dir = os.path.join(export_dir, state)
        if not os.path.exists(curr_state_dir):
            os.mkdir(curr_state_dir)

        df = export_data(state)
        if df.empty:
            logger.warning(f"Skipping {state} — no data returned.")
            continue

        df.reset_index(drop=True, inplace=True)
        base_name = os.path.join(curr_state_dir, state.lower() + "-farmfresh")

        df.to_csv(base_name + ".csv", index=False)
        logger.info(f"{state}: {len(df)} records written to {base_name}.csv")

        if include_json_yaml:
            df.to_json(base_name + ".json", orient='records')
            with open(base_name + ".yaml", 'w') as f:
                yaml.dump({'data': df.to_dict(orient='records')}, f, default_flow_style=False)
            logger.info(f"{state}: also wrote .json and .yaml")

    logger.info(f"Export complete for: {states}")
    update_readme_timestamp()


def update_readme_timestamp():
    """Update the <!-- LAST_UPDATED --> placeholder in the parent README.md."""
    readme_path = os.path.join(curr_file_dir, "../README.md")
    readme_path = os.path.normpath(readme_path)
    if not os.path.exists(readme_path):
        logger.warning(f"README not found at {readme_path}")
        return
    date_str = datetime.now().strftime("%B %-d, %Y")
    updated_line = f"<!-- LAST_UPDATED -->Python pulled fresh state data on **{date_str}**"
    with open(readme_path, "r") as f:
        content = f.read()
    new_content = re.sub(
        r"<!-- LAST_UPDATED -->.*",
        updated_line,
        content
    )
    with open(readme_path, "w") as f:
        f.write(new_content)
    logger.info(f"README updated: {updated_line}")


if __name__ == "__main__":
    try:
        export_all_states()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
