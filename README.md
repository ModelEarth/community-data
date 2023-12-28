
[Data Pipeline](https://model.earth/data-pipeline)
<!--# Community Datasets -->

### County Business Patterns (CBP)
Pre-processed data for local industry levels (including employment, establishments and payroll).
Processed data resides in [https://github.com/modelearth/community-data/tree/master/community-data/us/state](us/state) <span class="local" style="display:none">- <a href="us/state">local</a></span>

<!-- https://github.com/modelearth/community-data/tree/master/ -->
Here are [the steps](process/python/bea) we used to generate subfolders with [us_econ.ipynb](process/python/bea) from the US Census&nbsp;API.

TO DO: Generate folders above with a GitHub Action - [Github&nbsp;Actions&nbsp;samples](https://model.earth/community/projects/#pipeline)  

Prior to GitHub Actions, another approach was the [Public Tree Map Pipeline](https://github.com/Public-Tree-Map/public-tree-map-data-pipeline).  
Here's a [fork of the resulting Santa Monica tree map](https://neighborhood.org/public-tree-map/).

How to process zipcodes for testing:
1) Access the single_zipcode.py file.
2) Select which NAICS levels you want by modifying the list "inds".
3) Run the function with desired incode as your parameter. This input should be a string, and contain five characters. Ex: '98006', '30308', '00501'

[Model.Earth](https://model.earth)