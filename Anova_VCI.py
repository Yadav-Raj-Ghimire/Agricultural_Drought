import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# Load your VCI data into a pandas DataFrame
df = pd.read_csv(r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\ExcelSheet\2001_2019VCI.csv')

# Convert 'Month' and 'Year' columns to datetime if necessary
df['Date'] = pd.to_datetime(df[['Month', 'Year']].assign(day=1))

# Parameters for customization
title_fontsize = 15
axis_label_fontsize = 12
legend_fontsize = 12
text_fontsize = 12
x_label_gap = 15
y_label_gap = 15
text_y_gap = 0.2  # Gap for the text labels in y-direction

# Perform ANOVA to compare Average VCI across different months
model_month = ols('Average_VCI ~ C(Month)', data=df).fit()
anova_results_month = anova_lm(model_month)

# Print ANOVA results for months
print("ANOVA Results by Month:\n", anova_results_month)

# Plotting example: Boxplot to visualize the distribution of VCI across months
plt.figure(figsize=(10, 6))
df.boxplot(column='Average_VCI', by='Month', grid=False)
plt.title('Average VCI Distribution Across Months', fontsize=title_fontsize, weight='bold')
plt.suptitle('')  # Suppress the automatic title to match with our custom title
plt.xlabel('Month', fontsize=axis_label_fontsize, labelpad=x_label_gap)
plt.ylabel('Average VCI', fontsize=axis_label_fontsize, labelpad=y_label_gap)
plt.grid(True)
plt.tight_layout()
plt.show()

# Perform ANOVA to compare Average VCI across different years
model_year = ols('Average_VCI ~ C(Year)', data=df).fit()
anova_results_year = anova_lm(model_year)

# Print ANOVA results for years
print("ANOVA Results by Year:\n", anova_results_year)

# Plotting example: Boxplot to visualize the distribution of VCI across years
plt.figure(figsize=(10, 6))
df.boxplot(column='Average_VCI', by='Year', grid=False)
plt.title('Average VCI Distribution Across Years', fontsize=title_fontsize, weight='bold')
plt.suptitle('')  # Suppress the automatic title to match with our custom title
plt.xlabel('Year', fontsize=axis_label_fontsize, labelpad=x_label_gap)
plt.ylabel('Average VCI', fontsize=axis_label_fontsize, labelpad=y_label_gap)
plt.grid(True)
plt.tight_layout()
plt.show()
