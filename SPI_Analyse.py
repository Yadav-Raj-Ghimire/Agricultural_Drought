import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Load the merged SPI CSV file
file_path = r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\SPI\SPI_merged.csv'  # Change this to your file path
spi_df = pd.read_csv(file_path)

# Print the column names to debug
print("Column Names in CSV:", spi_df.columns)

# Ensure the 'Year' and 'Month' columns are of type int
spi_df['Year'] = spi_df['Year'].astype(int)
spi_df['Month'] = spi_df['Month'].astype(int)

# Print the first few rows of the dataframe to inspect the data
print(spi_df.head())

# Assuming the correct column for SPI values is 'SPI'
spi_yearly = spi_df.groupby('Year')['SPI'].mean().reset_index()

# Calculate linear regression
slope, intercept, r_value, p_value, std_err = linregress(spi_yearly['Year'], spi_yearly['SPI'])

# Print regression results
print(f"Regression Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
print(f"P-value: {p_value}")

# Plot SPI over the years
plt.figure(figsize=(14, 8))
sns.lineplot(data=spi_yearly, x='Year', y='SPI', marker='o', label='Mean SPI')
plt.plot(spi_yearly['Year'], intercept + slope * spi_yearly['Year'], 'r', label=f'Fitted line (R²={r_value**2:.2f})')

# Add regression equation to the plot
regression_eq = f'Y = {intercept:.2f} + {slope:.2f}X'
plt.text(spi_yearly['Year'].min(), spi_yearly['SPI'].max(), regression_eq, fontsize=14, color='red', weight='bold')

# Customize the plot
plt.title('Yearly Mean Standard Precipitation Index (SPI) Trend', fontweight='bold', fontsize=16)
plt.xlabel('Year', fontweight='bold', fontsize='14')
plt.ylabel('Mean SPI', fontweight='bold', fontsize='14')
plt.legend(fontsize=14)
plt.grid(True)

plt.grid(True)
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
plt.tight_layout()

plt.savefig('SPI.png', dpi=200)

# Ensure the years on the x-axis are shown as integers
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# Show the plot
plt.show()

# Interpretation
if p_value < 0.05:
    print("The trend is statistically significant.")
    trend_interpretation = "statistically significant"
else:
    print("The trend is not statistically significant.")
    trend_interpretation = "not statistically significant"

# Detailed interpretation
print(f"\nThe regression equation is: {regression_eq}")
print(f"The R-squared value is: {r_value**2:.2f}, indicating that {r_value**2 * 100:.2f}% of the variability in SPI can be explained by the year.")
print(f"The p-value is: {p_value:.5f}, which means the trend is {trend_interpretation}.\n")
