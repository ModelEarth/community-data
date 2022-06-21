# Python Script: Single Zipcode
# This script allows the user to input a single zipcode (string), and it outputs the data for that zipcode
# Ex: '98006', '30308', '00501'

# Note this is an inefficient solution, will be updated 6/10/2022

import os
import json, requests, csv
import pandas as pd


### Explanation of  zipcode() Function
### In the zipcode() function, we have a base url which retrieves all relevant data for a certain IND Level. We can loop through each IND
### level and therefore retrieve all data for whichever IND Levels we are interested in.

### Following, we create a response object containing the data and use .json() to get the data into a json format, which we then write
### to a file. Then we open the file, and create a pandas DF of all the data. To generate the zip code folders, we group the dataframe
### by the "Zip Code" column and export it as a .csv file into the corresponding folder within naics/zips/xxxxx

inds = ["2"]

def single_zipcode(input_zip, ind_level): # populates zip code folders with data for given zip and NAICS (ind) level
    url = "https://api.census.gov/data/2018/zbp?get=ZIPCODE,NAICS2017,ESTAB,EMPSZES,PAYANN&for=&INDLEVEL=" + str(ind_level)
    response = requests.get(url)
    data = response.json()
    with open('ind_data.json', 'w') as f:
        json.dump(data, f)

    with open("ind_data.json", "r") as f2:
        jsdata = json.load(f2)

    df = pd.DataFrame(jsdata, columns = ["Zip", "Naics", "Establishments", "Employees", "Payroll", "NaicsLevel"])
    df['Employees'] =  df['Employees'].str.lstrip('0')

    if df.loc[df["Zip"] == input_zip].empty == True:
        print("No Data")
    else:
        if not os.path.exists("us/zipcodes/naics/" + input_zip[0]): # check if directory for 1st num already there
            os.makedirs("us/zipcodes/naics/" + input_zip[0])
        if not os.path.exists("us/zipcodes/naics/" + input_zip[0] + "/" + input_zip[1]):
            os.makedirs("us/zipcodes/naics/" + input_zip[0] + "/" + input_zip[1])
        if not os.path.exists("us/zipcodes/naics/" + input_zip[0] + "/" + input_zip[1] + "/" + input_zip[2]):
            os.makedirs("us/zipcodes/naics/" + input_zip[0] + "/" + input_zip[1] + "/" + input_zip[2])
        if not os.path.exists("us/zipcodes/naics/" + input_zip[0] + "/" + input_zip[1] + "/" + input_zip[2] + "/" + input_zip[3]):
            os.makedirs("us/zipcodes/naics/" + input_zip[0] + "/" + input_zip[1] + "/" + input_zip[2] + "/" + input_zip[3])
        if not os.path.exists("us/zipcodes/naics/" + input_zip[0] + "/" + input_zip[1] + "/" + input_zip[2] + "/" + input_zip[3] + "/" + input_zip[4]):
            os.makedirs("us/zipcodes/naics/" + input_zip[0] + "/" + input_zip[1] + "/" + input_zip[2] + "/" + input_zip[3] + "/" + input_zip[4])

    df.loc[df["Zip"] == input_zip].to_csv("us/zipcodes/naics/" + input_zip[0] + "/" + input_zip[1] + "/" 
    + input_zip[2] + "/" + input_zip[3] + "/" + input_zip[4] + "/zipcode" + input_zip + "-census-naics" + str(ind_level) + "-2018" + ".csv", index = False)

    print("Done")

## Function Call
single_zipcode("98006", 2)
print("Complete")