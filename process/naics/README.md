[Community Data](../../)

# Processing NAICS by Zip Code

From 2019 forward we'll pull zip data from the same census API as our [county and state processing](/data-pipeline/industries/naics/)

Portions of this page will be moved into a new ztca page within [data-pipeline/industries/naics](/data-pipeline/industries/naics/)

The code and data in the current "process/naics" folder will be deleted.


## Annual ZCTA Files

The ZBP API page states that only naics level-2 provide payroll.
We have however seen some of the payroll values populated at other naics levels.
All levels have both Establishments and Employees count.

<!--
[View Data by Zip](https://model.earth/zip/io/#zip=30318)
[Process Timelines](/data-pipeline/timelines/prep/all)
-->

153 US zip zcta areas reside in more than one state, so state zip code agreegates could be inflated.

**Postal Code File Name (Upcoming)**

All state's zip codes (zcta) and their industries (3 levels):
community-data/industries/naics/US/zcta/NY/US-NY-census-naics2-zcta-2023.csv
community-data/industries/naics/US/zcta/NY/US-NY-census-naics4-zcta-2023.csv
community-data/industries/naics/US/zcta/NY/US-NY-census-naics6-zcta-2023.csv

**Columns**
- Ztca
- Naics - ActivityProducedBy (6-digit naics)  
- Establishments (Number of Locations)
- Employees (Number of Employees)  
- Payroll - US Dollars (Annual Wages)<!--
Population - Included with our [Machine Learning](/machine-learning/) output
Sqkm or Sqmiles - To be added -->

<!--
**Postal Code File Name (OLD)**

https://github.com/ModelEarth/community-data/tree/master/process/naics/zips/30501

[CountryCode] - zip[5-digit postalcode] - census - naics level (2, 4, 6) - year

US-zip-census-naics2-2020.csv
US-zip-census-naics4-2020.csv
US-zip-census-naics6-2020.csv

These will reside in 1/2/3/4/5 folders:

US-zip30318-census-naics2-2020.csv
US-zip30318-census-naics4-2020.csv
US-zip30318-census-naics6-2020.csv
-->

## Older Notes

### NAICS zip code files

Processed using <b>split\_zip\_data.py</b> in the current folder.
Creates files for naics levels 2,4 and 6 in "zips" subfolder.

Example:
[Zip 53521](https://github.com/ModelEarth/community-data/tree/master/us/zipcodes/naics/5/3/5/2/1)



### Timeline zip code files

Community-Forecasting timeline zip code files reside at:  
[https://github.com/ModelEarth/community-usa/tree/main/data/zip](https://github.com/ModelEarth/community-usa/tree/main/data/zip)
Range 2012 to 2016 projected to 2021. [Regression project](/community-forecasting/?page=zip/#zip=30318) was in 2019.


# Industries by Zip Code (ZCTA)

Benjamin Liu processed [naics by zip code](https://github.com/modelearth/community-data/tree/master/process/naics). (Payroll is mostly 0 in these.)

We're pulling [zip demographic data](../../zip/io/) into a json file for each zip code from [uszipcode.readthedocs.io](https://uszipcode.readthedocs.io/01-Tutorial/index.html).  

[Bureau of Labor Statistics (BLS)](https://www.bls.gov/data/) also provides annual industry data by zip code.

Here's a example of [clustering zip code data for multiple parameters](../../community/zip/leaflet/#columns=JobsAgriculture:50;JobsManufacturing:50).  


## Older - ZIP Code Industries from BEA Spreadsheets


Here's a [prep all](/community/prep/all/) script with industries by zip code from spreadsheets with a random forest applied. 


<b>Industry Employment Levels</b><br>

Script resides in prep/industries/source

To run:  
sqlite3 industry.db < industry.SQL.txt > industry.OUT.txt  
First change the year in industry.SQL.txt  

### Data Sources

Due to the delay of 2017 Economic Census, the 2017 zip data became available in December of 2019. (The above script has not yet been updated and run for the 2017 data.)  
<!--
Companies per industry within each zipcode. Normally these are available annually at the end April, but the [ 2019 release will be in November and December](https://www.census.gov/programs-surveys/cbp/news-updates/updates/dec-2018.html) due to the delay of 2017 Economic Census.  
-->
[Start here](https://www.census.gov/programs-surveys/cbp/data/datasets.html) 
Choose "County Business Patterns: [Year]" then "Complete ZIP Code Industry Detail File"  

Issue: 2018 zipcode data is not available as of June 2020.  

[Source of Zipcode lat/lon - 2018 Census](https://www.census.gov/geo/maps-data/data/gazetteer2018.html)  

From similar data collection with crosswalking of zips to zcta...  
https://www.urban.org/sites/default/files/publication/29311/412248-business-patterns-and-trends-national-summary.pdf


Not currently used (similar, but no file download)...  
[Census.gov - US zips to NAICS industry sectors](https://www.census.gov/data/developers/data-sets/cbp-nonemp-zbp/zbp-api.html)   

Also not used...  
[NAICS to ISIC](https://www.census.gov/eos/www/naics/concordances/concordances.html) -
[About](https://blog.opencorporates.com/2018/01/18/new-feature-global-industry-codes/)  
[opencorporates.com](https://opencorporates.com/info/networks)  
[International Data Base (IDB)](https://www.census.gov/programs-surveys/international-programs/about/idb.html)
[World Health Scatterplot](http://bl.ocks.org/msbarry/9911363)

Example of data format:  
"zip","naics","est","n1_4","n5_9","n10_19","n20_49","n50_99","n100_249","n250_499","n500_999","n1000"  
"00501","------",2,1,0,0,1,0,0,0,0,0  
"00501","81----",2,1,0,0,1,0,0,0,0,0  
"00501","813///",2,1,0,0,1,0,0,0,0,0  
"00501","8131//",2,1,0,0,1,0,0,0,0,0  
"00501","81311/",2,1,0,0,1,0,0,0,0,0  
"00501","813110",2,1,0,0,1,0,0,0,0,0  
"01001","------",472,228,83,64,57,24,13,2,0,1  
"01001","22----",1,0,0,0,1,0,0,0,0,0  
"01001","221///",1,0,0,0,1,0,0,0,0,0  
"01001","2213//",1,0,0,0,1,0,0,0,0,0  
"01001","22132/",1,0,0,0,1,0,0,0,0,0  
"01001","221320",1,0,0,0,1,0,0,0,0,0  
"01001","23----",58,36,9,5,5,3,0,0,0,0  
"01001","236///",9,6,1,2,0,0,0,0,0,0  
"01001","2361//",8,6,1,1,0,0,0,0,0,0  
"01001","23611/",8,6,1,1,0,0,0,0,0,0  
"01001","236116",1,1,0,0,0,0,0,0,0,0  
"01001","236118",7,5,1,1,0,0,0,0,0,0  
"01001","2362//",1,0,0,1,0,0,0,0,0,0  
"01001","23622/",1,0,0,1,0,0,0,0,0,0  
"01001","236220",1,0,0,1,0,0,0,0,0,0  
"01001","237///",1,1,0,0,0,0,0,0,0,0  
"01001","2373//",1,1,0,0,0,0,0,0,0,0  
"01001","23731/",1,1,0,0,0,0,0,0,0,0  
"01001","237310",1,1,0,0,0,0,0,0,0,0  


<a href="/localsite/info/">View Industry Comparison using this data</a>  
