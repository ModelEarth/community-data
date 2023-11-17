# Community Data (us_econ)

Online at our [Google Colab](https://colab.research.google.com/drive/1gXlpE6Hmc60RRsbYXuJ4QRoKyfnv2wzC) - not tested  

Open Jupyter Notebook in a browser with the command:

	jupyter-notebook

You may need to run `pip install notebook` after installing Python.  

To process, run [process/python/us_econ.ipynb](process/python/us_econ.ipynb) in a Jupyter Notebook or by running:  


	jupyter nbconvert --to notebook --inplace --execute us_econ.ipynb

It takes a few hours for the Python scripts to run. The biggest part is getting data from API. the second big one is aggregating the CSV files and deleting the prior files.  

After running, you can delete the county_level folder inside data_raw\BEA_Industry_Factors.  

The last block of this notebook contains the code for generating the state-wide data. Getting the state-wide totals directly from the Census API results in numbers different from the sum of each state’s county totals since the cesus excludes payroll and number of employees for counties with only a couple firms.  


## Usage  

Resulting data is used with Environmentally-Enable Input-Output widgets within Model.earth and Neighborhood.org.  We're developing a framework for global analysis and we encourage your participation integrating datasets and pulling visualizations into your other projects.

### Data Includes

#### US Industries by County
Annual Payroll, Employee Count, Establishments (with estimates filling gaps that protect anonymity)  



### For NAICS industry charts

The Jupyter Notebook for industry data preparation resides in [us_econ.ipynb](us_econ.ipynb).  

Run the notebook cells either in juyter notebook or by running from the command line:

	jupyter nbconvert --to notebook --inplace --execute us_econ.ipynb

After aggregating the data, you can delete the county\_level and state\_level folders inside data/data_raw/BEA\_Industry\_Factors.  

The last block of this notebook contains the code for generating the state-wide data. When only 1 or 2 of an industry reside in a county, numbers are omitted by the US Census to protect privacy. As a result, the state-wide totals from the Census API are larger than the sum of each state’s county totals.  
[Additional info](https://github.com/modelearth/community/issues/9)  
### API calls
As included in the [us_econ.ipynb](us_econ.ipynb) notebook, the base url for API calls is:

	https://api.census.gov/data

A full URL follows the following format:

	{base_url}/{year}/cbp?get={columns_to_select}&for=county:*&in=state:{fips:02d}

For example, to get the 2016 data for all counties in the state of Georgia, you can use the following URL:

	https://api.census.gov/data/2016/cbp?get=GEO_ID,GEO_TTL,COUNTY,YEAR,NAICS2012,NAICS2012_TTL,ESTAB,EMP,PAYANN&for=county:*&in=state:13

You can find a list of columns to select on [this link](https://api.census.gov/data/2016/cbp/variables.html).
### Note for the data used in the Bubblemap
If rounding off 8 decimals, ozone depletion, pesticides and a few others would need to be switched to scientific notation in the data file. This would allow the files to be reduced
US from 151kb to under 72.7kb
GA from 120kb, to under 59.2kb


