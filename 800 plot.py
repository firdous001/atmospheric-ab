import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = "C:/Users/Firdos/Downloads/output_csv_files/absorption_coefficients_800.csv"
data = pd.read_csv(file_path)

# Extract the column for histogram
column_name = 'Abs_Coeff'  # Replace 'column_name_to_plot' with the actual column name
column_data = data[column_name]

# Plot the histogram
plt.hist(column_data, bins=500, color='blue', edgecolor='black')  # Adjust bins as needed
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of ' + column_name)
plt.grid(True)
plt.show()