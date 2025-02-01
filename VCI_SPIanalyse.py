import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib import ticker

# Load the CSV file into a pandas DataFrame
file_path = r"D:\Working\Working2\New_Output\GEEimages\Bagmati_march\SPI\SPI_VCI.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# Extract VCI and SPI columns
vci = df['VCI']
spi = df['SPI']

# Calculate correlation coefficient
corr_coef = np.corrcoef(vci, spi)[0, 1]
print(f"Correlation Coefficient between VCI and SPI: {corr_coef}")

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(vci, spi)

# Print slope and intercept
print(f"Slope of the regression line: {slope}")
print(f"Intercept of the regression line: {intercept}")
print(f"R-squared value: {r_value**2}")

# Plotting the data points and the regression line
plt.figure(figsize=(8, 6))

# Scatter plot of data points
plt.scatter(vci, spi, color='b', label='Data points')

# Regression line
plt.plot(vci, intercept + slope*vci, color='r', label='Regression line')

# Title and labels with bold fonts
plt.title('Relationship between VCI and SPI', fontsize=14, fontweight='bold')
plt.xlabel('VCI', fontsize=12, fontweight='bold')
plt.ylabel('SPI', fontsize=12, fontweight='bold')

# Legend with bold fonts
plt.legend(prop={'size': 12, 'weight': 'bold'})

# Add equation of regression line to the plot
equation = f"y = {intercept:.2f}+{slope:.2f}x"
plt.text(0.05, 0.95, equation, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))

# Grid and ticks with bold fonts and increased visibility
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=10, width=1.5)
plt.tick_params(axis='both', which='minor', labelsize=8, width=1)

# Customize tick labels to be bold
plt.gca().tick_params(axis='both', which='major', width=1.5, labelsize=10)
plt.gca().tick_params(axis='both', which='minor', width=1, labelsize=8)

# Adjust the layout to prevent clipping of labels
plt.tight_layout()

# Save the plot as a high-quality image (optional)
plt.savefig('vci_spi_relationship.png', dpi=300)

# Show the plot
plt.show()
