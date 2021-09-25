# Farm Fresh Data

We're using [a Python scraper](scraper) to pull and merge locations from the national USDA dataset.  
Note that USDA now also provides an [API](https://www.ams.usda.gov/local-food-directories/farmersmarkets).  

It fetches data for our [Map of Fresh Produce](https://model.earth/localsite/info/#show=farmfresh).  

Processed data resides in: [community-data/us/state](https://github.com/modelearth/community-data/tree/master/us/state)

TO DO: Set up a GitHub Action that runs the [Python scraper](scraper) nightly.  
Update the state files if changed. Call the nightly process from a page listing all the data pulls.  


### About USDA Source

[National USDA map of farmer's markets](https://www.ams.usda.gov/local-food-directories/farmersmarkets) - [Google Map for full data download](https://search.ams.usda.gov/farmersmarkets/googleMapFull.aspx)  

Issue with federal datasource:  
Needs to require either http or https at time of data entry.  


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
