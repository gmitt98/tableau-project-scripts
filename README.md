# Module 18 - Tableau
This repo just contains the data used for the tableau project.
I downloaded the data from citibike then used python to combine them and access the single file, instead of trying to do it in tableau. I also used python to create a ranked list of the bike stations, with the total rides per station. This ranking is used in the map.

Tableau Public link for this story is here:
https://public.tableau.com/app/profile/galen.mittermann/viz/citibike_book1/Story1

## Data

I used the availble March-June data for 2023. This goes from 3/1/23 to 6/23/23. These are the tripdata csv files.

## Code in the repo

There are two python files in the repo:
- citibike_file_join.py: this combines the tripdata csv files
- stations_volume_ranks.py: this uses pandas to create the grouped data that i use on the map

## Dashboards

The following dashboards are available by name:
- Stations: contains the ride summary data for the stations
- Ride Volume: ride count by day, including by rider type
- Riders and Bicycle Types: a breakdown of the bicycle type amongs the rider types

There is also a map, and the underlying workbooks for these dashboards.

## Findings

In the Tableau story, we can clearly see a few trends:

- ridership increases over the course of the spring
- daily ridership is centered on the morning and evening hours
- there is a spike on Fridays and on weekends
- there are differences in bike selection between casual and membership riders
