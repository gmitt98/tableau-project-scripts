import pandas as pd
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir((current_directory))

#print my current directory to check...
print("Current Directory:", current_directory)

csv_files = ["JC-202303-citibike-tripdata.csv", "JC-202304-citibike-tripdata.csv", "JC-202305-citibike-tripdata.csv", "JC-202306-citibike-tripdata.csv"]
dataframes = []

for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

output_csv = "citibike_data_mar-jun_combined.csv"

combined_df.to_csv(output_csv, index=False)
