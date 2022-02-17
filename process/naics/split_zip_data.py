# Zips

#from uszipcode import SearchEngine
import os
import json, requests, csv

#base_url = "http://api.census.gov/data/2018/zbp?get=NAICS2017,ZIPCODE,ESTAB,EMPSZES&for=&INDLEVEL="

url_beg = "api.census.gov/data/2018/zbp?get=NAICS2017,ESTAB,EMPSZES&for=ZIPCODE:"
url_end = "&for=&INDLEVEL="

inds = ["2", "3", "4", "5", "6"]
raw_nums = list(range(0,99951))
zips = []

for number in raw_nums:
    if len(str(number)) == 3:
        zips.append("00" + str(number))
    elif len(str(number)) == 4:
        zips.append("0" + str(number))
    else:
        zips.append(number)

def zipcode_data():
    for i in zips:
        for j in inds:
            url = base_beg + str(i) + url_end + j
            response = requests.get(url)
            data = response.json()





def zipcodes(indlevel):
    url = base_url + str(indlevel)
    response = requests.get(url)
    data = response.json()

    with open('feb11_test.csv', 'w', newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(data)

### Function Call
if __name__ == '__main__':
    #zipcodes(6)
    print("OK")
