# Zips
# Retrieving NAICS data for each (zip code, IND level) pair
# 2/23/2022

import os
import json, requests, csv
import pandas as pd

inds = ["2", "4", "6"]
raw_nums = list(range(501,99951))
zips = []

for number in raw_nums: # appending 0's to begining of zip codes with <5 numbers
    if len(str(number)) == 3:
        zips.append("00" + str(number))
    elif len(str(number)) == 4:
        zips.append("0" + str(number))
    else:
        zips.append(str(number))

def create_folders(): # creates a folder for every zip code
    for each in zips:
        if not os.path.exists("zips/"+each): # check if directory for zipcode already there before
            os.makedirs("zips/"+each)

### Explanation of  zipcode() Function
### In the zipcode() function, we have a base url which retrieves all relevant data for a certain IND Level. We can loop through each IND
### level and therefore retrieve all data for whichever IND Levels we are interested in.

### Following, we create a response object containing the data and use .json() to get the data into a json format, which we then write
### to a file. Then we open the file, and create a pandas DF of all the data. To generate the zip code folders, we group the dataframe
### by the "Zip Code" column and export it as a .csv file into the corresponding folder within naics/zips/xxxxx

### The total time it took to run was around 2.5 hours

def zipcode(): # populates zip code folders with data for each zip
    for j in inds:
        url = "https://api.census.gov/data/2018/zbp?get=ZIPCODE,NAICS2017,ESTAB,EMPSZES,PAYANN&for=&INDLEVEL=" + j
        response = requests.get(url)
        data = response.json()
        with open('ind2_data.json', 'w') as f:
            json.dump(data, f)

        with open("ind2_data.json", "r") as f2:
            jsdata = json.load(f2)

        df = pd.DataFrame(jsdata, columns = ["Zip", "Naics", "Establishments", "Employees", "Payroll", "NaicsLevel"])

        for num in zips[30000:30500]:
            if df.loc[df["Zip Code"] == num].empty == True:
                continue
            elif not os.path.exists("zips/" + num): # check if directory for zipcode already there before
                os.makedirs("zips/" + num)
                df.loc[df["Zip"] == num].to_csv("zips/" + num + "/zipcode" + num + "-naics" + j + "-2018" + ".csv", index = False)
            else:
                df.loc[df["Zip"] == num].to_csv("zips/" + num + "/zipcode" + num + "-naics" + j + "-2018" + ".csv", index = False)
        print("Done with IND")


def delete_empty(): # deletes zip folders without data in them
    dir = "zips"
    folders = list(os.walk(dir))[1:]

    for folder in folders:
        if not folder[2]:
            os.rmdir(folder[0])




### Function Calls
if __name__ == '__main__':
    #create_folders()
    zipcode()
    #delete_empty()
    print("Complete...")

