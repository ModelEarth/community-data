[Community Data](../../../)
# Farm Fresh Data

[Data Processing Notes](../../../locations/farmfresh/) (2024)


We previously used [a Python scraper](https://github.com/ModelEarth/community-data/tree/master/process/python/farmfresh/scraper) to pull and merge locations from the national USDA dataset.  

TO DO (older notes before 2024):

Please update our "Makefile" python script to use the new [USDA API](https://www.ams.usda.gov/local-food-directories/farmersmarkets).
Please call 877-333-9336 or write the maintainers of the USDA API since they have not responded to email.

The following USDA export used in our scrape no longer exists.
https://search.ams.usda.gov/farmersmarkets/ExcelExport.aspx

Processed data resides in: [community-data/us/state](https://github.com/modelearth/community-data/tree/master/us/state)
The API pull can send to a new folder at community-data/farmfresh/us/NY
The script can reside at [data-pipeline](/data-pipeline/)/farmfresh/us/NY

Sample of [API file pull using Python](../bea/)

TO DO: We also need a file containing an overview for all the states. It could include a column for the total location in each state.


TO DO: Set up a GitHub Action that runs the static file creation process nightly. 


### About USDA Source

[National USDA map of farmer's markets](https://www.ams.usda.gov/local-food-directories/farmersmarkets) - [Google Map for full data download](https://search.ams.usda.gov/farmersmarkets/googleMapFull.aspx)  

Issue with federal datasource:  
Needs to require either http or https at time of data entry.  

<br>

# About Our Previous Scrapper

## USDA Farm Fresh Screen Scraper

Scrapes and merges the USDA's lists of [farmer's markets](https://search.ams.usda.gov/farmersmarkets/ExcelExport.aspx) and [on-farm markets](https://search.ams.usda.gov/onfarmmarkets/ExcelExport.aspx). The results are saved into CSV and JSON files.

## Dependencies

[jq](https://stedolan.github.io/jq/), [yarn](https://yarnpkg.com/), [python3](https://www.python.org/downloads/), [ds-dsv](https://github.com/d3/d3-dsv), and [make](https://www.gnu.org/software/make/).


## Run

Install all the above dependencies.  
Run the following in the scraper folder.  
Note: the first time you run, you will need to manually create a folder called 'out' in the scraper folder.

### Setup

Setup the environment:

`python3 -m venv .venv`

OSX / Linux:

`source .venv/bin/activate`

Windows:

`\.venv\Scripts\activate.bat`


### Install dependencies

`pip install -r requirements.txt` (not needed here)

`yarn install`  Install dependencies (generates node_modules folder).

`make all`  Scrape, process, and merge.

The combined results are placed into the folder `out/merged/`.

The individual states are then split into `out/states/`.
<br><br>
