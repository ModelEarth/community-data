# Community Data

## Data preparation for localsite community profiles

[Jupyter notebook](data/data_collection.ipynb).  

Run the notebook cells in Jupyter notebook or by running:  

	jupyter nbconvert --to notebook --inplace --execute data_collection.ipynb


After running, you can delete the county_level folder inside data\data_raw\BEA_Industry_Factors.  

The last block of this notebook contains the code for generating the state-wide data. Getting the state-wide totals directly from the Census API results in numbers different from he sum of each state’s county totals.  
