import pandas as pd
import os

# move to current directory and open combined file
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir((current_directory))

file_path = 'citibike_data_mar-jun_combined.csv'
df = pd.read_csv(file_path)

# group the data and count things
grouped_data = df.groupby('start_station_id').agg({
    'start_station_id': 'count',
    'start_lat': 'mean',
    'start_lng': 'mean'
})

# rename columns so it's clear what i did
grouped_data.rename(columns={
    'start_station_id': 'count_of_rides',
    'start_lat': 'avg_start_lat',
    'start_lon': 'avg_start_lng'
}, inplace=True)

# add rankings
sorted_data = grouped_data.sort_values(by='count_of_rides', ascending=False)
sorted_data['ranking'] = range(1, len(sorted_data) + 1)

# save it off
output_file_path = 'stations_volume_ranked.csv'
sorted_data.to_csv(output_file_path)

print(f"successfully saved new file to {output_file_path}")