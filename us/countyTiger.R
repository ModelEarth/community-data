if (!require(sf)) {install.packages('sf')}
if (!require(tidyverse)) {install.packages('tidyverse')}
library(sf)

# read shp data
state = read_sf('tl_2019_us_state/tl_2019_us_state.shp')

# drop geometry, select column, rename column names
state_csv = st_drop_geometry(state) %>% 
  select(STATEFP, STUSPS, NAME, ALAND, INTPTLAT, INTPTLON) %>%
  mutate(ALAND = round(ALAND / 1e+06, 0)) %>% # change unit from m2 to km2, round to integer
  rename(lat = INTPTLAT, lon = INTPTLON, name = NAME, kilometers = ALAND, fips = STATEFP, state = STUSPS) %>%
  mutate(lat = as.numeric(lat), lon = as.numeric(lon))


# write csv
readr::write_csv(state_csv, 'select.csv')