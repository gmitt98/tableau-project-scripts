import pandas as pd
import os

# move to the right directory
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir((current_directory))

# print my current directory to check...
print("Current Directory:", current_directory)

# list the files and set up and empty dataframe
csv_files = ["JC-202303-citibike-tripdata.csv", "JC-202304-citibike-tripdata.csv", "JC-202305-citibike-tripdata.csv", "JC-202306-citibike-tripdata.csv"]
dataframes = []

# open the files and append to my dataframe
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

# save it
output_csv = "citibike_data_mar-jun_combined.csv"

combined_df.to_csv(output_csv, index=False)
