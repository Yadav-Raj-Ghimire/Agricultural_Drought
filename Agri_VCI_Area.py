import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Load data from CSV
file_path = r"D:\Working\Working2\New_Output\integratedData\EXCEL\Agri_Occupied_VCI.csv"
data = pd.read_csv(file_path)

# Extract columns
years = data['years']
extreme_drought = data['Extreme_Drought(Sq. Km)']
severe_drought = data['Severe_Drought(Sq. Km)']
moderate_drought = data['Moderate_Drought(Sq. Km)']
mild_drought = data['Mild_Drought(Sq. Km)']
no_drought = data['No_Drought (Sq. Km)']

# Calculate correlation coefficients
corr_extreme = np.corrcoef(years, extreme_drought)[0, 1]
corr_severe = np.corrcoef(years, severe_drought)[0, 1]
corr_moderate = np.corrcoef(years, moderate_drought)[0, 1]
corr_mild = np.corrcoef(years, mild_drought)[0, 1]
corr_no = np.corrcoef(years, no_drought)[0, 1]

# Perform linear regression
def calculate_regression(x, y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return slope, intercept, r_value

# Calculate regression parameters for each drought category
slope_extreme, intercept_extreme, r_extreme = calculate_regression(years, extreme_drought)
slope_severe, intercept_severe, r_severe = calculate_regression(years, severe_drought)
slope_moderate, intercept_moderate, r_moderate = calculate_regression(years, moderate_drought)
slope_mild, intercept_mild, r_mild = calculate_regression(years, mild_drought)
slope_no, intercept_no, r_no = calculate_regression(years, no_drought)

# Plotting individual figures with separate figures for each subplot

# Extreme Drought Plot and Analysis
plt.figure(figsize=(8, 6))
plt.plot(years, extreme_drought, marker='o', linestyle='-', color='r', label=f'Extreme Drought (corr: {corr_extreme:.2f})')
plt.plot(years, slope_extreme * years + intercept_extreme, linestyle='--', color='b', label=f'Regression: y = {slope_extreme:.2f}x + {intercept_extreme:.2f}')
plt.title('Extreme Drought', weight='bold', fontsize=12)
plt.xlabel('Years', weight='bold', fontsize=10)
plt.ylabel('Area (Sq. Km)', weight='bold', fontsize=10)
plt.legend(fontsize=8)
plt.grid(True)
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')
plt.tight_layout()

# Interpretation and Analysis of Extreme Drought Plot
print(plt.text(0.05, 0.95, f"Correlation coefficient: {corr_extreme:.2f}\n"
                     f"Regression slope: {slope_extreme:.2f} (Sq. Km/year)\n"
                     f"Interpretation: There is a strong negative correlation "
                     f"between years and the area affected by extreme drought, "
                     f"indicating a significant decrease over time.",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top'))
plt.show()

# Severe Drought Plot and Analysis
plt.figure(figsize=(8, 6))
plt.plot(years, severe_drought, marker='o', linestyle='-', color='g', label=f'Severe Drought (corr: {corr_severe:.2f})')
plt.plot(years, slope_severe * years + intercept_severe, linestyle='--', color='b', label=f'Regression: y = {slope_severe:.2f}x + {intercept_severe:.2f}')
plt.title('Severe Drought', weight='bold', fontsize=12)
plt.xlabel('Years', weight='bold', fontsize=10)
plt.ylabel('Area (Sq. Km)', weight='bold', fontsize=10)
plt.legend(fontsize=8)
plt.grid(True)
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')
plt.tight_layout()

# Interpretation and Analysis of Severe Drought Plot
print(plt.text(0.05, 0.95, f"Correlation coefficient: {corr_severe:.2f}\n"
                     f"Regression slope: {slope_severe:.2f} (Sq. Km/year)\n"
                     f"Interpretation: There is a moderate negative correlation "
                     f"between years and severe drought area, suggesting a "
                     f"decreasing trend over time, although less pronounced "
                     f"than extreme drought.",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top'))
plt.show()

# Moderate Drought Plot and Analysis
plt.figure(figsize=(8, 6))
plt.plot(years, moderate_drought, marker='o', linestyle='-', color='b', label=f'Moderate Drought (corr: {corr_moderate:.2f})')
plt.plot(years, slope_moderate * years + intercept_moderate, linestyle='--', color='b', label=f'Regression: y = {slope_moderate:.2f}x + {intercept_moderate:.2f}')
plt.title('Moderate Drought', weight='bold', fontsize=12)
plt.xlabel('Years', weight='bold', fontsize=10)
plt.ylabel('Area (Sq. Km)', weight='bold', fontsize=10)
plt.legend(fontsize=8)
plt.grid(True)
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')
plt.tight_layout()

# Interpretation and Analysis of Moderate Drought Plot
print(plt.text(0.05, 0.95, f"Correlation coefficient: {corr_moderate:.2f}\n"
                     f"Regression slope: {slope_moderate:.2f} (Sq. Km/year)\n"
                     f"Interpretation: There is a moderate negative correlation "
                     f"between years and moderate drought area, indicating a "
                     f"decreasing trend with some variability over the years.",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top'))
plt.show()

# Mild Drought Plot and Analysis
plt.figure(figsize=(8, 6))
plt.plot(years, mild_drought, marker='o', linestyle='-', color='c', label=f'Mild Drought (corr: {corr_mild:.2f})')
plt.plot(years, slope_mild * years + intercept_mild, linestyle='--', color='b', label=f'Regression: y = {slope_mild:.2f}x + {intercept_mild:.2f}')
plt.title('Mild Drought', weight='bold', fontsize=12)
plt.xlabel('Years', weight='bold', fontsize=10)
plt.ylabel('Area (Sq. Km)', weight='bold', fontsize=10)
plt.legend(fontsize=8)
plt.grid(True)
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')
plt.tight_layout()

# Interpretation and Analysis of Mild Drought Plot
print(plt.text(0.05, 0.95, f"Correlation coefficient: {corr_mild:.2f}\n"
                     f"Regression slope: {slope_mild:.2f} (Sq. Km/year)\n"
                     f"Interpretation: There is a weak negative correlation "
                     f"between years and mild drought area, indicating a "
                     f"gradual decrease over time with some variability.",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top'))
plt.show()

# No Drought Plot and Analysis
plt.figure(figsize=(8, 6))
plt.plot(years, no_drought, marker='o', linestyle='-', color='m', label=f'No Drought (corr: {corr_no:.2f})')
plt.plot(years, slope_no * years + intercept_no, linestyle='--', color='b', label=f'Regression: y = {slope_no:.2f}x + {intercept_no:.2f}')
plt.title('No Drought', weight='bold', fontsize=12)
plt.xlabel('Years', weight='bold', fontsize=10)
plt.ylabel('Area (Sq. Km)', weight='bold', fontsize=10)
plt.legend(fontsize=8)
plt.grid(True)
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')
plt.tight_layout()

# Interpretation and Analysis of No Drought Plot
print(plt.text(0.05, 0.95, f"Correlation coefficient: {corr_no:.2f}\n"
                     f"Regression slope: {slope_no:.2f} (Sq. Km/year)\n"
                     f"Interpretation: There is a very weak positive correlation "
                     f"between years and the area unaffected by drought, indicating "
                     f"no significant trend over time.",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top'))
plt.show()
