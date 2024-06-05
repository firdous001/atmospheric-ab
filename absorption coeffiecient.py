import os
import pandas as pd

# Define the file and folder paths
ghi_file = "C:/Users/Firdos/Downloads/output_csv_files/Reference.csv"
dni_folder = "C:/Users/Firdos/Downloads/output_csv_files/alone unzip"

# Define the wavelengths of interest
wavelengths_of_interest = [800, 1550, 2200]

# Read the GHI(AM0) data from the single CSV file
ghi_df = pd.read_csv(ghi_file)

# Filter GHI(AM0) for the specific wavelengths
ghi_filtered = ghi_df[ghi_df['Wavelength'].isin(wavelengths_of_interest)]

# Initialize a DataFrame to store the results
results = pd.DataFrame(columns=['File', 'Wavelength', 'Abs_Coeff'])

# Iterate over each CSV file in the folder
for file_name in os.listdir(dni_folder):
    if file_name.endswith('.csv'):
        # Read the DNI(AM1.5) data from the current CSV file
        dni_df = pd.read_csv(os.path.join(dni_folder, file_name))

        # Filter DNI(AM1.5) for the specific wavelengths
        dni_filtered = dni_df[dni_df['Wavelength'].isin(wavelengths_of_interest)]

        # Merge GHI(AM0) and DNI(AM1.5) data on Wavelength
        merged_df = pd.merge(ghi_filtered, dni_filtered, on='Wavelength', suffixes=('_GHI', '_DNI'))

        # Apply the equation to calculate abs_coeff
        merged_df['Abs_Coeff'] = 100 - (merged_df['Spectral DNI 280-4000 nm (W/m2/nm)'] * 100) / merged_df['Etr W*m-2*nm-1']

        # Append the results to the results DataFrame
        for _, row in merged_df.iterrows():
            results = results.append({
                'File': file_name,
                'Wavelength': row['Wavelength'],
                'Abs_Coeff': row['Abs_Coeff']
            }, ignore_index=True)

# Save the results to a CSV file
results.to_csv('abs_coeff_results.csv', index=False)

print('Calculation completed and results saved to abs_coeff_results.csv')