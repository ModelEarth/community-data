if (!require(sf)) {install.packages('sf')}
if (!require(tidyverse)) {install.packages('tidyverse')}
library(sf)

# read shp data
state = read_sf('tl_2019_us_state/tl_2019_us_state.shp')

# drop geometry, select column, rename column names
num_decimals = 4
state_csv = st_drop_geometry(state) %>% 
  select(STATEFP, STUSPS, NAME, ALAND, INTPTLAT, INTPTLON) %>%
  mutate(ALAND = round(ALAND / 1e+06, 0)) %>% # change unit from m2 to km2, round to integer
  rename(lat = INTPTLAT, lon = INTPTLON, name = NAME, kilometers = ALAND, fips = STATEFP, state = STUSPS) %>%
  mutate(lat = round(as.numeric(lat), num_decimals), lon = round(as.numeric(lon), num_decimals))


# write csv
readr::write_csv(state_csv, 'select.csv')

# write dropdown menu list
outfile = "dropdown_menu_list.html"
cat("", file = outfile)
for(row in 1:nrow(state_csv)) {
  cat(paste0("<option value=\"", state_csv$state[row],
             "\" stateid=\"", state_csv$fips[row],
             "\" lat=\"", state_csv$lat[row],
             "\" lon=\"", state_csv$lon[row],
             "\" km=\"", state_csv$kilometers[row],
             "\">", state_csv$name[row],
             "</option>\n"),
      file = outfile,
      append = T)
}
