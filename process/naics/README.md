[Data Pipeline](https://model.earth/localsite/info/data)  
# County Business Patterns (CBP)

Using 2018 data in [source/efsy_panel_naics_2018.csv](source/efsy_panel_naics_2018.csv)  
which was manually copied from: [Panel with Harmonized 2012 NAICS Industry Codes](http://www.fpeckert.me/cbp/)  

**Parse the following columns into state CSV files:**  
fipstate, fipscty, naics12, emp, year, v1  

**Use these column headers:**  
FIPS, NAICS, Establishments, Employees, Payroll  
(Our [Machine Learning Imputation](https://github.com/modelearth/machine-learning) also includes Population)

Combine fipstate, fipscty into a 5 character string.  
We'll need to figure out if the Eckert source can provide a payroll estimate.  

**Generate folders and files for all states in the format:**	  
community-data/us/state/GA/naics/GA-counties-naics6-2018.csv

[Example of saving to state files](../python/bea). Make this a process we can share with our ML processing.


Run a Python script:
https://github.com/marketplace/actions/run-python-script

A Jupyter Notebook can also be run:
https://github.com/marketplace/actions/run-notebook


