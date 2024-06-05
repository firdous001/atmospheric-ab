import pandas as pd
import os

# Folder containing the CSV files
folder_path = "C:/Users/Firdos/Downloads/june 20/20230620 - Copy"


# Function to calculate absorption coefficient
def calculate_absorption_coeff(dni_value):
    return 100 - ((dni_value - 100) / 1.138)


# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Check if 'DNI' column exists in the DataFrame
        if 'DNI' in df.columns:
            # Apply the formula to the 'DNI' column to calculate the 'absorption_coeff' column
            df['absorption_coeff'] = df['DNI'].apply(calculate_absorption_coeff)

            # Save the updated DataFrame back to the CSV file
            df.to_csv(file_path, index=False)

            print(f'Updated {filename} with absorption_coeff column')
        else:
            print(f'Column "DNI" not found in {filename}')
