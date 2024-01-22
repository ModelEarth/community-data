[Community Data](../../../)

# Process Industries for Counties
<!--Import from BEA for NAICS industry charts us_econ)-->

The Jupyter Notebook for industry data preparation resides in [us_econ.ipynb](us_econ.ipynb).

Open Jupyter Notebook with this command in the folder process/python/bea then click us_econ.ipynb and run each step:

	jupyter-notebook

Or you can run [us_econ.ipynb](process/python/us_econ.ipynb) from the command line:  

	jupyter nbconvert --to notebook --inplace --execute us_econ.ipynb

You may need to run `pip install notebook` after installing Python.  

Change the timeout (sleep) on your computer. Changed Start Screen Saver when inactive from 20 minutes to never.

It may take a few hours for the Python scripts to run. The most time is getting data from API. The second most is aggregating the CSV files and deleting the prior files.<!-- let's record actual times -->

After running, you can delete the county_level folder inside data_raw\BEA_Industry_Factors.  

The last block of this notebook contains the code for generating the state-wide data. Getting the state-wide totals directly from the Census API results in numbers different from the sum of each state’s county totals since the cesus excludes payroll and number of employees for counties with only a couple firms.  

TO DO: Columns of final output should be something like:

FIPS, NAICS, Establishments, Employees, Payroll


TO DO: Generate folders quarterly with a GitHub Action - [Github&nbsp;Actions&nbsp;samples](https://model.earth/community/projects/#pipeline)  


## Usage  

Resulting data is used within the [industry comparison](/localsite/info/) page to load industries for counties.

### Data Includes US Industries by County

Annual Payroll, Employee Count, Establishments (with estimates filling gaps that protect anonymity)  

Currently years 2012 to 2020 work.

The last block of this notebook contains the code for generating the state-wide data. When only 1 or 2 of an industry reside in a county, numbers are omitted by the US Census to protect privacy. As a result, the state-wide totals from the Census API are larger than the sum of each state’s county totals.

[Additional info](https://github.com/modelearth/community/issues/9)

After aggregating the data, you can delete the folders inside bea/data_raw/BEA\_Industry\_Factors/county\_level and state\_level.



### API calls

As included in the [us_econ.ipynb](us_econ.ipynb) notebook, the base url for API calls is:

	https://api.census.gov/data

A full URL follows the following format:

	{base_url}/{year}/cbp?get={columns_to_select}&for=county:*&in=state:{fips:02d}

For example, to get the 2016 data for all counties in the state of Georgia, you can use the following URL:

	https://api.census.gov/data/2016/cbp?get=GEO_ID,GEO_TTL,COUNTY,YEAR,NAICS2012,NAICS2012_TTL,ESTAB,EMP,PAYANN&for=county:*&in=state:13

You can find a list of columns to select on [this link](https://api.census.gov/data/2016/cbp/variables.html).

### Note for the data used in the Bubblemap
If rounding off 8 decimals, ozone depletion, pesticides and a few others would need to be switched to scientific notation in the data file. This would allow the files to be reduced as follows:

US from 151kb to under 72.7kb
GA from 120kb, to under 59.2kb


