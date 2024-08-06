import json 
import pandas as pd
import requests
import sys
import yaml
import os
import logging.handlers


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
        # Process the data (example: print it)
        # print(json.dumps(data, indent=2))
        # logger.info("Successfully fetched data from USDA API")
    else:
        #print(f"Failed to fetch data: {response.status_code}")
        logger.error(f"Failed to fetch data: {response.status_code}")
        return {}
    return data_json["data"]

def update_column_names(data_df):
    columns_map = {
        "directory_type"    :"type"     ,
        "listing_name"      :"name"     ,
        "media_website"     :"website"  ,
        "media_facebook"    :"facebook" ,
        "media_twitter"     :"twitter"  ,  
         "location_street"  :"street"   ,
        "location_city"     :"city"     ,
        "location_state"    :"state"    ,
        "location_zipcode"  :"zip"      ,
        "location_x"        :"longitude",
        "location_y"        :"latitude" ,
        "brief_desc"        : "tags"    
    }
    df1 = data_df.rename(columns=columns_map)
    df1 = df1.drop(columns=['distance'], errors='ignore')
    # logger.info("Updated column names")
    return df1


def export_data(state):
    
    try:
        apikey = os.environ["USDA_FARMFRESH_API"]
        # print("API Key:", apikey)  # Debugging line
    except KeyError:
        logger.error("API key not available!")
        # apikey="UXLbsdPdCU"
        sys.exit(1)  # Exit the script if the API key is not available
    # apikey="UXLbsdPdCU"
    market_type = "farmersmarket"
    # logger.info(f"Exporting data for state: {state}")
    data_json1 = fetch_usda_markets(apikey, state, market_type)
    data_df1 =  pd.DataFrame.from_dict(data_json1)
    market_type = "onfarmmarket"
    data_json2 = fetch_usda_markets(apikey, state, market_type)
    data_df2 =  pd.DataFrame.from_dict(data_json2)

    data_merge = pd.concat([data_df1, data_df2], ignore_index=True)

    data_merge = update_column_names(data_merge)
    
    return data_merge

def export_all_states():
    export_dir = "../us"
    curr_file_dir = os.path.dirname(__file__)
    export_dir =os.path.join(curr_file_dir, export_dir)
    #print("Exporting to", export_dir)
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
                print("exporting state:", curr_state_dir )
                os.mkdir(curr_state_dir)
            data_merged = export_data(state)
            file_name = os.path.join(curr_state_dir,state.lower()+"-farmfresh")
            data_merged.to_csv(file_name+".csv")
            data_merged.to_json(file_name+".json")

            with open(file_name+".yaml", 'w') as file:
                documents = yaml.dump({'data': data_merged.to_dict(orient='records')}, file, default_flow_style=False)
            # data_merged.to_yaml(file_name+".yaml")
            # logger.info(f"Data for state {state} exported successfully")
    logger.info(f"Data for all states exported successfully")
    

    


if __name__=="__main__":

    export_all_states()

    # market_type = sys.argv[1]
    # state =  sys.argv[2]
    # output_file =  sys.argv[3]
    # apikey="UXLbsdPdCU"
    # data_json = fetch_usda_markets(apikey, state, market_type)
    # str_data = json.dumps(data_json,indent=2)
    # with open(output_file, mode="w") as f:
    #     f.write(str_data)

    # df = pd.DataFrame.from_dict(data_json)
    # output_file_csv = output_file.split(".")[0] + ".csv"
    # df.to_csv(output_file_csv)


