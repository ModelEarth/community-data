# Community Data

## Data preparation


Run [process/python/us_econ.ipynb](data/us_econ.ipynb) in Jupyter Notebook or by running:  


	jupyter nbconvert --to notebook --inplace --execute us_econ.ipynb


After running, you can delete the county_level folder inside data_raw\BEA_Industry_Factors.  

The last block of this notebook contains the code for generating the state-wide data. Getting the state-wide totals directly from the Census API results in numbers different from the sum of each state’s county totals.  
