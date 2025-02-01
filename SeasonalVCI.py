import pandas as pd
import matplotlib.pyplot as plt

# Load your VCI data into a pandas DataFrame
df = pd.read_csv(r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\ExcelSheet\2001_2019VCI.csv')

# Convert 'Month' and 'Year' columns to datetime if necessary
df['Date'] = pd.to_datetime(df[['Month', 'Year']].assign(day=1))

# Define seasons (adjust as per your specific definition)
seasons = {
    'Dry Season': [1, 2, 3, 11, 12],   # November to March
    'Wet Season': list(range(4, 11))   # April to October
}

# Assign seasons based on month
df['Season'] = df['Date'].dt.month.apply(lambda x: next((season for season, months in seasons.items() if x in months), None))

# Group by season and calculate seasonal statistics
seasonal_stats = df.groupby('Season')['Average_VCI'].agg(['mean', 'median', 'min', 'max'])

# Plotting example: Seasonal variation
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the mean and median VCI with error bars
seasonal_stats.plot(kind='bar', y=['mean', 'median'], yerr=seasonal_stats[['max', 'min']].values.T, 
                    ax=ax, rot=0, capsize=5)

# Set labels and title
ax.set_title('Seasonal VCI Variations (2001-2019)', fontsize=14)
ax.set_xlabel('Season', fontsize=12)
ax.set_ylabel('Average VCI', fontsize=12)

# Add gridlines for better readability
ax.grid(axis='y', linestyle='--')

plt.tight_layout()
plt.show()
