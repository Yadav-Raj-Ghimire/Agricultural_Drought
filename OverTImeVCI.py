import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Load your VCI data into a pandas DataFrame (assuming it's already loaded correctly)
df = pd.read_csv(r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\ExcelSheet\2001_2019VCI.csv')

# Convert 'Month' and 'Year' columns to datetime if necessary
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(day=1))

# Parameters for customization
title_fontsize = 15
axis_label_fontsize = 12
legend_fontsize = 12
text_fontsize = 12
x_label_gap = 15
y_label_gap = 15
text_y_gap = 0.02  # Gap for the text labels in y-direction

# Plotting example: Trend over time with months on x-axis
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Average_VCI'], label='Average VCI')
plt.title('Average VCI Trend Over Time with Months on X-axis', fontsize=title_fontsize, weight='bold')
plt.xlabel('Date', fontsize=axis_label_fontsize, labelpad=x_label_gap)
plt.ylabel('Average VCI', fontsize=axis_label_fontsize, labelpad=y_label_gap)
plt.legend(fontsize=legend_fontsize)

# Calculate trend line using linear regression
# Convert dates to ordinal numbers for regression
x = df['Date'].map(pd.Timestamp.toordinal).values.reshape(-1, 1)
y = df['Average_VCI'].values.reshape(-1, 1)
slope, intercept, r_value, p_value, std_err = stats.linregress(x.flatten(), y.flatten())

# Plot trend line
plt.plot(df['Date'], intercept + slope * x.flatten(), 'r', label='Trend Line')

# Display regression equation and correlation coefficient on the plot
regression_equation = f'Y = {intercept:.2f} + {slope:.6f}X'
correlation_coefficient = f'R = {r_value:.2f}'

# Adjust the position for better visibility
text_x_position = df['Date'].iloc[int(len(df) * 0.1)]
text_y_position = max(df['Average_VCI']) - text_y_gap

plt.text(text_x_position, text_y_position, regression_equation, fontsize=text_fontsize, color='red', verticalalignment='bottom')
plt.text(text_x_position, text_y_position - text_y_gap, correlation_coefficient, fontsize=text_fontsize, color='red', verticalalignment='top')

# Show plot
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Interpretation and Analysis
print(f"Interpretation and Analysis:")
print(f"---------------------------")
print(f"The regression equation Y = {intercept:.2f} + {slope:.6f}X indicates that there is a linear relationship between time (X) and Average VCI (Y).")
print(f"The correlation coefficient R = {r_value:.2f} suggests a {'positive' if r_value > 0 else 'negative'} correlation between time and Average VCI.")
print(f"This means that as time progresses, there is a tendency for the Average VCI to {'increase' if slope > 0 else 'decrease'}.")
print(f"The trend line (red line) visually represents this relationship, showing the overall direction of change in Average VCI over time.")
