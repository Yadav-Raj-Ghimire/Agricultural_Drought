import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load your VCI data into a pandas DataFrame
df = pd.read_csv(r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\ExcelSheet\2001_2019VCI.csv')

# Convert 'Month' and 'Year' columns to datetime if necessary
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(day=1))

# Extract year and month for plotting purposes
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Get the unique years
years = df['Year'].unique()

# Specify the folder to save plots
save_folder = r'D:\Working\Working2\New_Output\VCI_Plots'

# Create the folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

# Set a fixed figure size for consistency
fig_width = 6.0  # Width of the figure in inches
fig_height = 4.0  # Height of the figure in inches

# Create separate plots for each year
for year in years:
    yearly_data = df[df['Year'] == year]
    
    # Create a new figure with specified size
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    
    # Plot the data
    ax.plot(yearly_data['Month'], yearly_data['Average_VCI'], marker='o', label=f'{year}')
    ax.set_title(f'Average VCI Changes in {year}', fontsize=15, color='black', weight='bold')
    ax.set_xlabel('Month', fontsize=8, color='black', weight='bold')
    ax.set_ylabel('Average VCI', fontsize=8, color='black', weight='bold')
    ax.legend()
    ax.grid(True)
    ax.set_xticks(np.arange(1, 13, 1))  # Ensure x-axis shows each month from 1 to 12
    
    # Find the maximum and minimum VCI values
    max_vci = yearly_data['Average_VCI'].max()
    min_vci = yearly_data['Average_VCI'].min()
    max_vci_month = yearly_data.loc[yearly_data['Average_VCI'].idxmax(), 'Month']
    min_vci_month = yearly_data.loc[yearly_data['Average_VCI'].idxmin(), 'Month']
    
    # Annotate the maximum and minimum VCI values
    ax.annotate(f'Max VCI: {max_vci:.2f}', xy=(max_vci_month, max_vci), xytext=(max_vci_month, max_vci + 0.05),
                arrowprops=dict(facecolor='green', shrink=0.05), fontsize=8, color='green', weight='bold')
    ax.annotate(f'Min VCI: {min_vci:.2f}', xy=(min_vci_month, min_vci), xytext=(min_vci_month, min_vci - 0.05),
                arrowprops=dict(facecolor='red', shrink=0.05), fontsize=8, color='red', weight='bold')
    
    # Save plot for the current year with equal dimensions
    save_path = os.path.join(save_folder, f'Average_VCI_Changes_{year}.png')
    fig.tight_layout()
    fig.savefig(save_path, dpi=300, bbox_inches='tight')  # Save figure with high resolution and tight bounding box
    plt.show()  # Display the plot (debugging purposes)
    plt.close(fig)  # Close the figure to free memory

print(f"Plots saved in folder: {save_folder}")
