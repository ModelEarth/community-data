# Community Datasets

Pre-processed data for local industry levels (including employment, establishments and payroll).

- [Process Industries by State and County](process/python/bea) - Gaurav
- [Process Industries by Zip](process/naics/) - Gaurav
- [Process Multi-County State Regions](us/edd/)
- [Process Product Impact Profiles by Zip](/io/template/feed/)
- [Process US Census by Zip and International Postal Codes](/zip/io/#zip=10001) - Chen and Gary
- [Process All the Places by Zip](/places) - Chen
- [SQLite in Browser for Timelines](/data-pipeline/timelines/sqlite/) - We Need Help!
- [Timeline Data Prep and Samples](/data-pipeline/timelines/prep/all/) - Sijia
- [ChatGPT Web Assistant Setup](https://github.com/Niek/chatgpt-web)
<!--
	Overview video
	https://platform.openai.com/docs/actions/introduction

	https://retool.com/component-library
-->
- [Process Farm Fresh Data](process/python/farmfresh/)
- New: Update [State Map](#geoview=country) with [EPA color levels](https://figshare.com/collections/USEEIO_State_Models_v1_0_-_Supporting_Figures/7041473)
- [Data Pipeline: US EPA Data Sources](/data-pipeline/)
- [Model.Earth](https://model.earth)
<!-- [Imputation for NAICS Using Machine Learning](/machine-learning/)-->

Other areas:
Google Places - For Recyclers, EV Parts Manufactures
Google Data Commons
CensusReporter.com

Investigations of [Commodity Flow Survey for Counties](https://github.com/modelearth/commodity-flow-survey)
[International Data Pipeline](../data-pipeline/international) - Imports and exports by country by year (to be developed)  

<!--   
[Zipcode files with employment levels](https://github.com/modelearth/community-data/tree/master/us/zipcodes/naics) - Includes nunber of Establishments and Employees 
-->

---
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

[Model.Earth Team](../io/team/)