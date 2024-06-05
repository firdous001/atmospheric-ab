import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'filtered_data_for_2200.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Plot the histogram
plt.hist(data['Spectral GHI 280-4000 nm (W/m2/nm)'], bins=800, edgecolor='black')  # You can adjust the number of bins
plt.xlabel('Wavelength (nm)')
plt.ylabel('Atmospheric Adsorption')
plt.title('2200nm')

plt.savefig('Histagram at 2200nm.png')
plt.show()
