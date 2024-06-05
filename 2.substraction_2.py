import pandas as pd
import os

# Step 1: Read the reference CSV file
reference_df = pd.read_csv("reference.csv")

# Check if the output directory exists, if not, create it
output_directory = "output_csv_files"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Get the current directory
current_directory = os.getcwd()

# Process each CSV file containing "Spectral GHI 280-4000 nm (W/m2/nm)" in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(".csv"):
        input_filepath = os.path.join(current_directory, filename)
        output_filepath = os.path.join(output_directory, filename)

        # Read the CSV file
        data_df = pd.read_csv(input_filepath)

        # Check if the "Spectral GHI 280-4000 nm (W/m2/nm)" column exists in the data DataFrame
        if "Spectral GHI 280-4000 nm (W/m2/nm)" in data_df.columns:
            # Replace "Wvlgth nm" column in data_df with the one from reference_df
            data_df["Wvlgth nm"] = reference_df["Wvlgth nm"]

            # Perform inversion of subtraction
            data_df["Spectral GHI 280-4000 nm (W/m2/nm)"] = reference_df["Etr W*m-2*nm-1"] - data_df[
                "Spectral GHI 280-4000 nm (W/m2/nm)"]

            # Save the modified data into a new CSV file
            data_df.to_csv(output_filepath, index=False)
        else:
            print(f"Warning: File '{filename}' does not contain 'Spectral GHI 280-4000 nm (W/m2/nm)' column. Skipping.")

print("Subtraction completed and saved in output directory.")
