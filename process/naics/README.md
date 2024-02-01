[Community Data](../../)

# Processing NAICS by Zip Code

[View Data by Zip](https://model.earth/zip/io/#zip=30318)

### NAICS zip code files

Processed using <b>split\_zip\_data.py</b> in the current folder.
Creates files for naics levels 2,4 and 6 in "zips" subfolder.

Bug: Payroll column is mostly 0. Why do some get populated? [Example](https://github.com/ModelEarth/community-data/tree/master/us/zipcodes/naics/5/3/5/2/1)

The columns from the census naics zip file are:
Zip Naics Establishments Employees Payroll 

Population and Sqmiles would be good to add from another source.

The file title format contains naics2, naics4 or naics6 and the year:
zipcode53521-census-naics6-2020.csv

### Timeline zip code files

Community-Forecasting timeline zip code files reside at:  
[https://github.com/ModelEarth/community-usa/tree/main/data/zip](https://github.com/ModelEarth/community-usa/tree/main/data/zip)