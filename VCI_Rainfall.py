import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the CSV file into a pandas DataFrame
file_path = r"D:\Working\Working2\New_Output\climate_data\RainfallData_Final\ExcelData\Rainfall_VCI.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# Extract VCI and Precipitation columns
vci = df['VCI']
precipitation = df['Precipitation (mm)']

# Calculate correlation coefficient
corr_coef = np.corrcoef(precipitation, vci)[0, 1]
print(f"Correlation Coefficient between Precipitation and VCI: {corr_coef:.2f}")

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(precipitation, vci)

# Print slope and intercept
print(f"Slope of the regression line: {slope:.5f}")
print(f"Intercept of the regression line: {intercept:.2f}")
print(f"R-squared value: {r_value**2:.2f}")

# Plotting the data points and the regression line
plt.figure(figsize=(8, 6))

# Scatter plot of data points
plt.scatter(precipitation, vci, color='b', label='Data points')

# Regression line
plt.plot(precipitation, intercept + slope*precipitation, color='r', linewidth=2, label=f'Regression line\ny = {intercept:.2f} + {slope:.5f}x')

# Title and labels with bold fonts
plt.title('Relationship between Precipitation and VCI', fontsize=14, fontweight='bold')
plt.xlabel('Precipitation (mm)', fontsize=12, fontweight='bold')
plt.ylabel('VCI', fontsize=12, fontweight='bold')

# Annotation with correlation coefficient
plt.text(0.05, 0.95, f'Correlation Coefficient: {corr_coef:.2f}', ha='left', va='top', transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.5), fontsize=12)

# Legend with bold fonts
plt.legend(prop={'size': 12, 'weight': 'bold'})

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
plt.savefig('vci_precipitation_relationship.png', dpi=300)

# Show the plot
plt.show()
