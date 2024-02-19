[Data Pipeline](/data-pipeline/)

# Community Datasets

Pre-processed data for local industry levels (including employment, establishments and payroll).

Files for Timelines and Observable: [industries/naics/US/counties](industries/naics/US/counties/)

- [Process Industries by State and County](process/python/bea) - Gaurav
- [Process Industries by Zip](process/naics/) - Gaurav
- [Build IO json for all states](/io/charts/) - Zhu<!-- Honglin -->
- [Process Multi-County State Regions (ChatGPT)](us/edd/)
- [Process Product Impact Profiles by Zip](/io/template/feed/)
- [Process US Census by Zip and International Postal Codes](/zip/io/#zip=10001) - Chen and Gary
- [Process All the Places by Zip](/places) - Chen
- [SQLite in Browser for Timelines](/data-pipeline/timelines/sqlite/) - We need help deploying to Github. [Like this.](https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/)
- [Timeline Data Prep, Random Forest](/data-pipeline/timelines/prep/all/) - Sijia
<!--

	mark huang - deep learning

	Overview video
	https://platform.openai.com/docs/actions/introduction

	https://retool.com/component-library

	- 

	[Google Places API]() - Hours of Operation, All The Places Recyclers, BuildingTransparency Manufacturers
-->

<!-- [Imputation for NAICS Using Machine Learning](/machine-learning/)-->

Exploration areas

- [Observable Framework Notes](/data-pipeline/timelines/observable)
- [ChatGPT Web Assistant Repo](https://github.com/Niek/chatgpt-web) - We need help deploying to Github. [Like this.](https://niek.github.io/chatgpt-web/)
- [Google Data Commons API](https://docs.datacommons.org/api/) - Pull International, Push impact data from US EPA
- [CensusReporter.com](https://CensusReporter.com)
- [Process Farm Fresh Data](process/python/farmfresh/)
- [Commodity Flow Survey for Counties](https://github.com/modelearth/commodity-flow-survey)
- [International Data Pipeline](../data-pipeline/international) - Imports and exports by country by year

<!--   
[Zipcode files with employment levels](https://github.com/modelearth/community-data/tree/master/us/zipcodes/naics) - Includes nunber of Establishments and Employees 
-->

---
<br>

TO DO: [Update our state map filter](#geoview=country) with color levels like the [new report maps](https://figshare.com/collections/USEEIO_State_Models_v1_0_-_Supporting_Figures/7041473) from US EPA engineer Wes Ingwersen.
<br>

Feb 2024

Hi State Partners,

I’m happy to share that our report, supporting figures and all the data files for v1.0 of the USEEIO State Models are now published. [View Report](https://cfpub.epa.gov/si/si_public_record_Report.cfm?dirEntryId=360453&Lab=CESER)

[Excel version of 2020 models](http://doi.org/10.23719/1530076) for all states:

We have files with models for all states for a given year in a native useeior Model format on a public server as well.

We have 100’s of supporting figures [including maps of the U.S.](https://doi.org/10.6084/m9.figshare.c.7041473) showing environmental pressure intensity grouped by indicator and commodity for all states and rankings of sectors by consumption by environmental pressure for 2020.

Please review the materials and let Wes know if you have any questions.
 
[The industry comparisons](../localsite/info/) draw on our EPA data prepared and presented using useeior (R Language),  useeio.js and the [useeio-widgets](../io/charts/) (Javascript and HTML using the USEEIO-API). Let us know if you have priorities and interests there and could provide us with some interactive feedback (testing) as we put that together.

As a reminder (and mentioned in the report) we’re working on Consumption-based GHG inventories (CBEI) for Maine and other Northeast states as an application of these models but the functionalities we develop and describe will be available for all States. We anticipate that being completed by early summer. 
 

Wesley W. Ingwersen, Ph.D.
Center for Environmental Solutions and Emergency Response (CESER)
Office of Research and Development
US Environmental Protection Agency

[Contact Model.Earth Team](../io/team/)