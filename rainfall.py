import pandas as pd
import chardet
import matplotlib.pyplot as plt

# Function to detect encoding (Note: Usually not needed for Excel files)
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

# File path to your Excel file
file_path = r'D:\Working\Working2\New_Output\climate_data\RainfallData_Final\ExcelData\Rainfall_2001_2019.xlsx'  # Replace with your actual file path

# Detect encoding (typically not necessary for Excel)
encoding = detect_encoding(file_path)

# Read Excel file
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Display the entire dataframe (optional)
print(df)

# Perform analysis or visualization here

# Example: Calculate mean rainfall for each year
mean_rainfall_per_year = df.iloc[:, 6:].mean()

# Example: Plot mean rainfall over years
plt.figure(figsize=(10, 6))
mean_rainfall_per_year.plot(kind='bar', color='skyblue')

# Setting bold font for all text elements
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Mean Rainfall (mm)', fontsize=14, fontweight='bold')
plt.title('Mean Rainfall per Year', fontsize=16, fontweight='bold')

# Making tick labels bold
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

plt.grid(True)
plt.tight_layout()
plt.show()

# Statistical Analysis
# Calculate overall mean, median, and standard deviation of rainfall
overall_mean = mean_rainfall_per_year.mean()
overall_median = mean_rainfall_per_year.median()
overall_std = mean_rainfall_per_year.std()

# Print statistical results
print("Overall Mean Rainfall (2001-2019): {:.2f} mm".format(overall_mean))
print("Overall Median Rainfall (2001-2019): {:.2f} mm".format(overall_median))
print("Overall Standard Deviation of Rainfall (2001-2019): {:.2f} mm".format(overall_std))

# Detailed interpretation of the results
print("\nDetailed Interpretation:")
print("The mean rainfall per year from 2001 to 2019 shows a variation in the annual rainfall patterns. The overall mean rainfall over these years is {:.2f} mm, indicating the average rainfall the region received each year. The median rainfall is {:.2f} mm, suggesting that half of the years had rainfall below this value, and half had above. The standard deviation of {:.2f} mm indicates the variability in the annual rainfall; a higher standard deviation would imply greater variability. The plotted bar chart provides a visual representation of these variations, highlighting years with significantly higher or lower rainfall compared to the overall mean.".format(overall_mean, overall_median, overall_std))
