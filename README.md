# Community Data

To process, run [process/python/us_econ.ipynb](process/python/us_econ.ipynb) in Jupyter Notebook or by running:  


	jupyter nbconvert --to notebook --inplace --execute us_econ.ipynb


After running, you can delete the county_level folder inside data_raw\BEA_Industry_Factors.  

The last block of this notebook contains the code for generating the state-wide data. Getting the state-wide totals directly from the Census API results in numbers different from the sum of each state’s county totals.  


## Usage  

Resulting data is used with Environmentally-Enable Input-Output widgets within Model.earth and Neighborhood.org.  Our goal is to provide a framework for global analysis and we welcome your participation. You may also pull this data into your other projects.

### Data Includes

#### US Industries by County
Annual Payroll, Employee Count, Establishments (with estimates filling gaps that protect anonymity)


