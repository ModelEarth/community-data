# split_US_data.py v1.1
# Splits county level concatenated US file into separate state files
# John Andrew Taylor, September 2021

import pandas as pd
import random

# Set to year desired. Must be string.
year = "2018"

# Set to quarter desired. Must be string.
# quarter = "Q1"

for i in range(2,7): # Generate for 2 to 6

    #df = pd.read_csv('country/US-counties-naics'+str(i)+'-'+year+'-'+quarter+'.csv', dtype = str)
    df = pd.read_csv('source/efsy_panel_naics_'+year+'.csv', dtype = str)

    states = pd.read_csv("source/FIPS_state_no_starting_zero.csv", dtype = str)
    fips_list = states['FIPS'].tolist()
    usps_list = states['USPS'].tolist()

    for fips, usps in zip(fips_list, usps_list):
        # print(usps)
        state_df = df[df['FIPS'].str.startswith(fips)]
        state_df.to_csv("states/"+usps+"/US-"+usps+'-counties-naics'+str(i)+'-'+year+'-'+quarter+'.csv', index = False)
