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


        # Perform subtraction
        data_df = reference_df["Etr W*m-2*nm-1"] - data_df["Spectral GHI 280-4000 nm (W/m2/nm)"]
        #data_df["Spectral GHI 280-4000 nm (W/m2/nm)"] -= reference_df["Etr W*m-2*nm-1"]



        # Save the modified data into a new CSV file
        data_df.to_csv(output_filepath, index=False)

print("Subtraction completed and saved in output directory.")
