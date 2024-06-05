import os
import pandas as pd

# Path to the folder containing CSV files
folder_path = "C:/Users/Firdos/Downloads/june 20/20230620 - Copy"

# Iterate through each CSV file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        # Extract timestamp from file name
        timestamp_parts = file_name.split('_')[:2]  # Extracting the first 2 parts
        timestamp = "_".join(timestamp_parts)

        # Read CSV file into a DataFrame
        df = pd.read_csv(os.path.join(folder_path, file_name))

        # Add a new column with the timestamp
        df['timestamp'] = timestamp

        # Write the modified DataFrame back to the CSV file
        df.to_csv(os.path.join(folder_path, file_name), index=False)