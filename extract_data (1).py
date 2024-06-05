import os
import pandas as pd

# Path to the folder containing CSV files
folder_path = "C:/Users/Firdos/Downloads/june 20/20230620 - Copy"

# Ensure the output folder exists, if not, create it
output_folder_path = "C:/Users/Firdos/Downloads/june 20/800 nm"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Wavelength of interest
target_wavelength = 800  # nm

# Iterate through each CSV file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        # Read CSV file into a DataFrame
        df = pd.read_csv(os.path.join(folder_path, file_name))

        # Find the column name closest to the target wavelength
        closest_column = min(df.columns, key=lambda x: abs(int(x) - target_wavelength))

        # Extract data for the closest wavelength to the target wavelength
        extracted_df = df[['Wavelength', closest_column]].rename(columns={closest_column: 'Intensity'})

        # Save the extracted DataFrame to a new CSV file in the output folder
        output_file_path = os.path.join(output_folder_path, f"{os.path.splitext(file_name)[0]}_800nm.csv")
        extracted_df.to_csv(output_file_path, index=False)