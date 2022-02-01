# County Business Patterns (CBP)

Using 2018 data in [source/efsy_panel_naics_2018.csv](source/efsy_panel_naics_2018.csv)  
Which was manually copied from: [Panel with Harmonized 2012 NAICS Industry Codes](http://www.fpeckert.me/cbp/)  

**Parse the following columns into state CSV files:**  
fipstate, fipscty, naics12, emp, year, v1  

**Use these column headers:**  
FIPS, NAICS, Establishments, Employees, Payroll  
(Our [Machine Learning Imputation](https://github.com/modelearth/machine-learning) also includes Population)

**Generate files for all states and save at:**	  
community-data/us/state/GA/naics/GA-county-naics6-2018.csv





