# Economic Development Districts (EDDs)

TO DO: Implement the Python below by adding a FIPS lookup library.
TO DO: Lazy load the .csv into [Region Dropdown](/localsite/info/#show=farmfresh&state=ME&imgview=state&geoview=state) when clicked.
TO DO: In our [Observable DataCommons](/data-pipeline/timelines/observable) repo, load international state (territory, municipality) menus and region menus for all countries.

Process [District Attributes](EDDLayer2_attributes.xls) (237 KB) to add a column with county FIPS so we can disply multi-county regions within states on maps.

    python -m venv venv && source venv/bin/activate
Should we use python3 above instead? .venv? The venv line is from [FastAPI ChatGPT plugins quickstart](https://github.com/keryc/chatgpt-plugins-fastapi-quickstart)

Request sent to ChatGPT

Add a column called Fips containing comma seperated FIPS codes for each county listed in the Counties column (separated by commas) within the State indicated in the State column. If the word City indicates the string is a city, use the county FIPS that the city resides in within the indicated state. Sometimes a city may reside in multiple counties. Provide a Python script to run this process. Use a Python library that looks up county FIPS codes based on county and state. And use a Python library that looks up counties for cities. Provide a link to download the resulting .xls file once you've added and populated the Fips column. Thanks!

[Response from ChatGPT](https://chat.openai.com/c/38d2c360-10bc-41b4-9efe-f0e606f1c0b1) - Currently functions are incomplete, and we'll need to find lookup libraries for citystate-to-counties and county-to-fips.

```
import pandas as pd

# Function to fetch FIPS code for a county
def get_county_fips(county_name, state_abbr):
    # This function should return the FIPS code for the given county and state.
    # Implementation depends on the library or API you choose to use.
    pass

# Function to fetch FIPS codes for a city (which may span multiple counties)
def get_city_county_fips(city_name, state_abbr):
    # This function should return a list of FIPS codes for the counties the city spans across.
    # Implementation depends on the library or API you choose to use.
    pass

# Load the dataset
file_path = 'path_to_your_file/EDDLayer2_attributes.xls'
data = pd.read_excel(file_path)

# New column for FIPS codes
data['Fips'] = ''

for index, row in data.iterrows():
    state_abbr = row['State']
    locations = row['Counties'].split(', ')  # Assuming the counties or cities are separated by commas
    fips_codes = []

    for loc in locations:
        if 'City of' in loc or 'city' in loc.lower():  # Identifying cities
            city_name = loc.replace('City of ', '').strip()
            fips_codes.extend(get_city_county_fips(city_name, state_abbr))
        else:  # Assuming remaining entries are counties
            county_name = loc.strip()
            fips_code = get_county_fips(county_name, state_abbr)
            if fips_code:
                fips_codes.append(fips_code)
    
    # Handling multiple FIPS codes (e.g., for cities spanning multiple counties)
    data.at[index, 'Fips'] = ', '.join(set(fips_codes))  # Removing duplicates and converting to string

# Save the updated dataset to a new Excel file
updated_file_path = 'path_to_your_file/updated_EDDLayer2_attributes.xls'
data.to_excel(updated_file_path, index=False)

print(f"Updated file saved to {updated_file_path}")
```


<!--
117 MB
Create a Python script that processes a 117 MB json shape file and splits it into small .csv files for each state and one file for the entire US (less than 1.5 MB).
-->

View map of federally-designated [Economic Development Districts](https://www.nado.org/eddmap)

Data organized by the National Association of Development Organizations (NADO)



Shape_Length is in meters
Shape_Area is in square meters

<!--Additional
[EDA.gov economic-development grant-resources by state](https://www.eda.gov/economic-development-directory?q=/grant-resources/economic-development-directory/)
-->

Please include a link to NADO.org if you use. And send us a link to checkout the cool things you build!

Send questions to [Loren and Wes at ModelEarth](/io/team/) or [Bret at NADO](https://www.nado.org/eddmap/).