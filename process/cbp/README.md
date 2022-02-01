# County Business Patterns (CBP)

Using 2018 data manually pulled from [Panel with Harmonized 2012 NAICS Industry Codes](http://www.fpeckert.me/cbp/) which resides at [source/efsy_panel_naics_2018.csv](source/efsy_panel_naics_2018.csv)

Parse the following into state CSV files:  
fipstate, fipscty, naics12, emp, year, v1  

With new column headers:  
FIPS,NAICS,Establishments,Employees,Payroll  
(Machine learning export might also include Population)

Generate for all states in the format:  
community-data/us/state/GA/GA-county-naics-6-digits-2018.csv





