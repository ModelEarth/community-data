### ZipCode Metrics List

# This code is generating a comprehensive list of all zipcodes that contain data for a given industry level.
# We are calculating the number of unique idustries, and total numbers for employees, establishments, and payroll
# The industry level is modifiable

# We achieve this using Pandas dataframes manipulation

import os
import json, requests, csv
import pandas as pd

ind_level = "6"
url = "https://api.census.gov/data/2018/zbp?get=ZIPCODE,NAICS2017,ESTAB,EMPSZES,PAYANN&for=&INDLEVEL=" + ind_level

# Simple way to get all Data
orig = pd.read_json(url)
new_header = orig.iloc[0]
orig = orig[1:]
orig.columns = new_header

# Converting to Integer Values
# cannot convert to int '44-45' -> need to determine best course of action
# duplicate row with 44 and 45 line?
int_df1 = orig.astype({'NAICS2017':'str', 'ESTAB' : 'int', 'EMPSZES' : 'int', 'PAYANN' : 'int', 'ZIPCODE' : 'str'})
int_df = int_df1.rename({'ZIPCODE' : 'Zip', 'NAICS2017': 'Industries', 'ESTAB': 'Establishments', 'EMPSZES' : 'Employees', 'PAYANN' : 'Payroll'}, axis=1)
print(int_df.columns)

# Grouping (Count Unique & Sum)
gr1 = int_df[['Zip','Industries']].groupby(['Zip']).nunique()
gr2 = int_df[['Zip','Establishments', 'Employees', 'Payroll']].groupby(['Zip']).sum()

# Merging Grouped Dataframes
combined = gr1.merge(gr2, left_on='Zip', right_on='Zip')
#final_df = combined.rename({'NAICS2017': 'Industries', 'ESTAB': 'Establishments', 'EMPSZES' : 'Employees', 'PAYANN' : 'Payroll'}, axis=1)
final_df = combined


# Exporting to CSV
final_df.to_csv('us/zipcodes/zipcodes' + ind_level + '.csv')
print(final_df)


# Testing with Small Subset
# df = pd.read_csv("test_data.csv")
# df2 = df.drop('0', inplace=False, axis=1)

# grouped1 = df2[['ZIPCODE','NAICS2017']].groupby(['ZIPCODE']).nunique()
# grouped2 = df2[['ZIPCODE','ESTAB', 'EMPSZES', 'PAYANN']].groupby(['ZIPCODE']).sum()

# final = grouped1.merge(grouped2, left_on='ZIPCODE', right_on='ZIPCODE')
# final2 = final.rename({'NAICS2017': 'Num Industries', 'ESTAB': 'Total Establishments', 'EMPSZES' : 'Total Employees', 'PAYANN' : 'Total Payroll'}, axis=1)

