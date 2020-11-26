# Updates for State Menu

The following R-Language updates to countyTiger.R in the [community-data repo](https://github.com/modelearth/community-data/tree/master/us) will allow us to output a drowpdown menu with values for zooming into selected states.  

1. Round the lat and lon values to four decimals.  
2. Round decimals off kilometers  
3. In addition to outputing the select.csv file, output a dropdown menu list in the following format:  

<code>
<option value="WY" stateid="56" lat="42.9897" lon="-107.5444" km="251459">Wyoming</option>  
</code>

Loren will add the resulting menu updates here to zoom into the state county maps:  

[https://model.earth/localsite/info/#select=counties](https://model.earth/localsite/info/#select=counties)


