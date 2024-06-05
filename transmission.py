#import datetime
#from pvlib import spectrum, solarposition, irradiance, atmosphere
import pandas as pd
#import matplotlib.pyplot as plt
#import daytime as dt
#import matplotlib.pyplot as plt
#import pvlib
import pytz
import os
import pandas as pd
reference_df = pd.read_csv("reference.csv")
# Specify the path to the directory containing the CSV files
data_path = "C:/Users/Firdos/Downloads/alone unzip"
#print(reference_df)
directory = "C:/Users/Firdos/Downloads/alone unzip"
# Initialize an empty DataFrame
df = pd.DataFrame()

# Iterate over all files in the directory
for file in os.listdir(data_path):
    # Check if the file is a CSV
    if file.endswith('.csv'):
        # Read the CSV file into a DataFrame
        data_frame = pd.read_csv(os.path.join(data_path, file), skiprows=0)
        # Concatenate the DataFrame to the main DataFrame
        df = pd.concat([df, data_frame], ignore_index=True)

# Optionally, display the combined DataFrame
#print(df.head())

#print(data_frame)


