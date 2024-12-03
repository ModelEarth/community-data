import json 
import pandas as pd
import requests
import sys
import yaml
import os
import logging.handlers
import re


## Notes
# Referred API docs: https://www.usdalocalfoodportal.com/fe/datasharing/


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
curr_file_dir = os.path.dirname(__file__)
logger_file_handler = logging.handlers.RotatingFileHandler(
    os.path.join(curr_file_dir,"status.log"),
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

def fetch_usda_markets(api_key, state, market_type="farmersmarket"):
    # USDA Farmers Markets API endpoint

    url = "https://www.usdalocalfoodportal.com/api/"+market_type+"/"
    params = {
        "apikey": api_key,
        "state": state
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    #print(url, params)
    # logger.info(f"Fetching data from URL: {url} with params: {params}")

    response = requests.get(url, headers=headers, params=params)
    # logger.info(f"Received response with status code: {response.status_code}")


    data_json = {}
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        data_json = data
        
    else:
        logger.error(f"Failed to fetch data: {response.status_code}")
        return {}
    return data_json["data"]

def update_column_names(data_df):
    columns_map = {
        "directory_name"    :"Type"     ,
        "updatetime"        :"ModifyDate",
        "listing_id"        :"ListingID",
        "listing_name"      :"Name"     ,
        "listing_image"     :"Image"     ,
        "listing_desc"      :"Description",
        "contact_name"      :"ContactName",
        "contact_email"     :"ContactEmail",
        "contact_phone"     :"ContactPhone",
        "media_website"     :"Website"  ,
        "media_facebook"    :"Facebook" ,
        "media_twitter"     :"Twitter"  ,
        "media_instagram"   :"Instagram",
        "media_pinterest"   :"Pinterest",
        "media_youtube"     :"Youtube",
        "media_blog"        :"Blog",
         "location_street"  :"Street"   ,
        "location_city"     :"City"     ,
        "location_state"    :"State",
        "location_zipcode"  :"Zip",
        "location_address"  :"Address",
        "location_x"        :"Longitude",
        "location_y"        :"Latitude",
        "brief_desc"        :"Tags"    
    }
    data_df.columns = data_df.columns.astype(str)
    data_df = data_df.drop(columns=data_df.columns[data_df.columns.str.contains('^Unnamed')])
    df1 = data_df.rename(columns=columns_map).reset_index(drop=True)
    df1 = df1.drop(columns=['distance', 'mydesc', 'term', 'directory_type'], errors='ignore')
    return df1

#Split the Tags column into Dates and Products, and clean the data.
def split_tags_column(data_df):
    if 'Tags' in data_df.columns:
        # Ensure 'Tags' column has no NaN values and all entries are strings
        data_df['Tags'] = data_df['Tags'].fillna('').astype(str)
        
        # Regular expressions to capture Dates and Products
        date_pattern = r'Open:\s*(.*?)(?:;\s*<br>|;|\s*<br>Available Products:|$)'
        products_pattern = r'Available Products:\s*(.*)'

        # Extract Dates
        data_df['Dates'] = data_df['Tags'].str.extract(date_pattern, expand=False)

        # Extract Products
        products = data_df['Tags'].str.extract(products_pattern, expand=False)
        data_df['Products'] = products.fillna('').apply(lambda x: ', '.join([item.strip() for item in x.split(';') if item.strip()]))
        
        #remove comment if want to save storage data
        # products = data_df['Tags'].str.extract(products_pattern, expand=False)
        # data_df['Products'] = products.fillna('').apply(lambda x: [item.strip() for item in x.split(';') if item.strip()])

        # Drop the original Tags column
        data_df = data_df.drop(columns=['Tags'], errors='ignore')
    return data_df

#Clean the Name column to convert all-caps to title case and replace 'L.L.C.' with 'LLC'.
def clean_name_column(data_df):
    if 'Name' in data_df.columns:
        data_df['Name'] = data_df['Name'].fillna('').astype(str)  # Ensure string
        # Convert all-caps strings to title case
        data_df['Name'] = data_df['Name'].apply(lambda x: x.title() if x.isupper() else x)
        # Replace 'L.L.C.' with 'LLC'
        data_df['Name'] = data_df['Name'].str.replace('L.L.C.', 'LLC')
    return data_df


def export_data(state):
    
    try:
        # apikey="UXLbsdPdCU"
        apikey = os.environ["USDA_FARMFRESH_API"]
        # print("API Key:", apikey)  # Debugging line
    except KeyError:
        logger.error("API key not available!")
        # apikey="UXLbsdPdCU"
        sys.exit(1)  # Exit the script if the API key is not available
    
    market_type = "farmersmarket"
    data_json1 = fetch_usda_markets(apikey, state, market_type)
    data_df1 =  pd.DataFrame.from_dict(data_json1)

    market_type = "onfarmmarket"
    data_json2 = fetch_usda_markets(apikey, state, market_type)
    data_df2 =  pd.DataFrame.from_dict(data_json2)
    # print(data_json1)

    data_merge = pd.concat([data_df1, data_df2], ignore_index=True)

    data_merge = update_column_names(data_merge)
     # Split the Tags column into Dates and Products, and clean the data.
    data_merge = split_tags_column(data_merge)  
    
    # Clean the Name column to convert all-caps to title case and replace 'L.L.C.' with 'LLC'.
    data_merge = clean_name_column(data_merge)
    return data_merge

def export_all_states():
    export_dir = "../us"
    curr_file_dir = os.path.dirname(__file__)
    export_dir =os.path.join(curr_file_dir, export_dir)
    # print("Exporting to", export_dir)
    logger.info(f"Exporting to directory: {export_dir}")
    
    if not os.path.exists(export_dir):
        os.mkdir(export_dir)

    state_list_path = os.path.join(curr_file_dir, "state_list.txt")

    with open(state_list_path) as state_file:
        states = state_file.read().split()
        for state in states:
            curr_state_dir = os.path.join(export_dir,state)
            # print("exporting state:", curr_state_dir )
            if not os.path.exists(curr_state_dir):
                # print("exporting state:", curr_state_dir )
                os.mkdir(curr_state_dir)
            data_merged = export_data(state)
            data_merged.reset_index(drop=True, inplace=True)
            #save farmersmarket files
            file_name = os.path.join(curr_state_dir,state.lower()+"-farmfresh")
            data_merged.to_csv(file_name+".csv", index=False)
            data_merged.to_json(file_name+".json", orient='records')
            with open(file_name+".yaml", 'w') as file:
                documents = yaml.dump({'data': data_merged.to_dict(orient='records')}, file, default_flow_style=False)

            #save onfarmmarket files
            file_name = os.path.join(curr_state_dir,state.lower()+"-onfarm")
            data_merged.to_csv(file_name+".csv", index=False)
            data_merged.to_json(file_name+".json", orient='records')
            with open(file_name+".yaml", 'w') as file:
                documents = yaml.dump({'data': data_merged.to_dict(orient='records')}, file, default_flow_style=False)
            # data_merged.to_yaml(file_name+".yaml")
            # logger.info(f"Data for state {state} exported successfully")
    logger.info(f"Data for all states exported successfully")
    

    


if __name__=="__main__":
    try:
        export_all_states()
    except Exception as e:
        logger.error(f"An error occurred: {e}")



