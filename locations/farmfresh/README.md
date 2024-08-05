# New Farmfresh Data Pull

We're pulling USDA for our [Farm Fresh state maps](/localsite/map/#show=farmfresh&state=NY)

We'll eliminate these two scrapper pages after the new API pull is ready:
[model.earth/community-data/process/python/farmfresh/](https://model.earth/community-data/process/python/farmfresh/)
[model.earth/community/farmfresh](https://model.earth/community/farmfresh)

The data was sent here previously - Arkansas example:
[github.com/ModelEarth/community-data/blob/master/us/state/AK/ak-farmfresh.csv](https://github.com/ModelEarth/community-data/blob/master/us/state/AK/ak-farmfresh.csv)

We'll send the new output to 2-char state folders here:
https://github.com/ModelEarth/community-data/locations/farmfresh

The new python can reside here:
https://github.com/ModelEarth/community-data/locations/farmfresh/prep

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

Setting Up the Secret Key - API Key
1. Locate the Workflow File
    Navigate to community-data/.github/workflows/actions.yml.
2. Identify the Secret Key
    Copy the value of {{secrets.USDA_FARMFRESH_API}}. In this case, it is USDA_FARMFRESH_API.
3. Access Repository Settings
    Click on the Settings tab of your repository.
4. Navigate to Secrets
    In the left sidebar, under the Security section, click on Secrets and variables.
5. Select Actions
    Choose Actions from the available options.
6. Create a New Repository Secret
    Click on New repository secret.
7. Add the Secret Key
    In the Name field, enter the exact secret key name (USDA_FARMFRESH_API), ensuring it matches the name in the .yml file.
    In the Secret field, enter the API key value.
    Click Add secret to save.
