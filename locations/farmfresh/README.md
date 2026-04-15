# About Farmfresh Data

<!-- LAST_UPDATED -->Python pulled fresh state data on **April 15, 2026**

Listings are pulled from the USDA API for our [Farm Fresh state maps](/localsite/map/#show=farmfresh&state=NY)

Output goes to [2-char state folders](https://github.com/ModelEarth/community-data/tree/master/locations/farmfresh/us).
Those folders reside locally when running the python, so no need to push to Github now.

The python and running instructions reside in [/community-data/locations/farmfresh/prep](prep)

For an initial test, just pull for GA (Georgia).

### Output File

Each state produces a single combined CSV: `../us/<STATE>/<state>-farmfresh.csv`

All listing types from the USDA API are merged into this one file. The `Type` column identifies each record:

- farmers market
- on-farm market
- csa enterprise
- food hub

### Column Names

Type, ModifyDate, Image, ListingID, Name, Description, ContactName, ContactEmail, ContactPhone,
Website, Facebook, Twitter, Instagram, Pinterest, Youtube, Blog,
Address, State, Street, City, Zip, Longitude, Latitude, Dates, Products

Any API columns not in the list above are renamed to CamelCase automatically.

### Data Cleanup Applied

DONE: CamelCase applied to all column names; snake_case API names are mapped to the columns above.

DONE: Tags column split into Dates and Products — "Open: " and "; Available Products: " prefixes removed.

DONE: In Name column, all-caps names converted to Title Case. (e.g. CAVE SPRING FARMERS MARKET → Cave Spring Farmers Market)

DONE: In Name column, L.L.C. replaced with LLC.


## API Key

The script reads the key from the `USDA_FARMFRESH_API` environment variable.
The working key (`UXLbsdPdCU`) is referenced in the commented line inside `fetch_data.py`.
See the [prep README](prep/README.md) for full setup and running instructions.

The GitHub Actions workflow reads the key from `secrets.USDA_FARMFRESH_API`
(see `.github/workflows/actions.yml`).


## Prior Pull

The data was previously scraped (no longer needed now that the API is available):
[model.earth/community-data/process/python/farmfresh/](https://model.earth/community-data/process/python/farmfresh/)
[model.earth/community/farmfresh](https://model.earth/community/farmfresh)

Prior column rename reference:
- directory\_name → Type
- updatetime → ModifyDate
- listing\_image → Image
- listing\_id → ListingID
- listing\_desc → Description
- media\_instagram → Instagram
- media\_pinterest → Pinterest
- media\_youtube → Youtube
- media\_blog → Blog
- location\_address → Address

Data was previously stored per state under `us/state/` — example:
[github.com/ModelEarth/community-data/blob/master/us/state/AK/ak-farmfresh.csv](https://github.com/ModelEarth/community-data/blob/master/us/state/AK/ak-farmfresh.csv)
