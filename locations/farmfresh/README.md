# About Farmfresh Data

We're pulling listings from the USDA API for our [Farm Fresh state maps](/localsite/map/#show=farmfresh&state=NY)

We send the output to [2-char state folders](https://github.com/ModelEarth/community-data/tree/master/locations/farmfresh/us)  
The python resides in [locations/farmfresh/prep](https://github.com/ModelEarth/community-data/locations/farmfresh/prep)


TO DO: Omit columns: type, mydesc, term

TO DO: Rename columns:

directory\_name to Type  
updatetime to ModifyDate  
listing\_image to Image  
listing\_id to ListingID  
listing\_desc to Description  
media\_instagram to Instagram  
media\_pinterest to Pinterest  
media\_youtube to Youtube  
media\_blog to Blog  
location\_address to Address

TO DO: Capitalize titles in columns, remove underscore, remove spaces

TO DO: Split Tags column into two columns called: Dates and Products.  
Remove "Open: " and "; Available Products: " before saving.

TO DO: In Name column, change all-caps to Title Case . (Offender: CAVE SPRING FARMERS MARKET)

TO DO: In Name column, replace L.L.C. with LLC

---

We're no longer using thse two scrapper pages now that the API is available:
[model.earth/community-data/process/python/farmfresh/](https://model.earth/community-data/process/python/farmfresh/)
[model.earth/community/farmfresh](https://model.earth/community/farmfresh)

The data was sent here previously - Arkansas example:
[github.com/ModelEarth/community-data/blob/master/us/state/AK/ak-farmfresh.csv](https://github.com/ModelEarth/community-data/blob/master/us/state/AK/ak-farmfresh.csv)



Include these column names in the new output:

Type
Name
Street
City
State (2-char)
Zip
Tags
Website
Twitter
Facebook
Longitude
Latitude

And any other columns in the API source, capitalize using CamelCase.
If the column names differ in the API, we could use the new column names if they are decent.

## Setting Up the Secret Key - API Key

1. Locate the Workflow File
    Navigate to community-data/.github/workflows/actions.yml.
2. Identify the Secret Key
    Copy the value of {{secrets.USDA\_FARMFRESH\_API}}. In this case, it is USDA\_FARMFRESH\_API.
3. Access Repository Settings
    Click on the Settings tab of your repository.
4. Navigate to Secrets
    In the left sidebar, under the Security section, click on Secrets and variables.
5. Select Actions
    Choose Actions from the available options.
6. Create a New Repository Secret
    Click on New repository secret.
7. Add the Secret Key
    In the Name field, enter the exact secret key name (USDA\_FARMFRESH\_API), ensuring it matches the name in the .yml file.
    In the Secret field, enter the API key value.
    Click Add secret to save.
