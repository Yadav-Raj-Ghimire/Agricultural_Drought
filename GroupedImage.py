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

# Parameters for customization
title_fontsize = 15
axis_label_fontsize = 12
legend_fontsize = 12
text_fontsize = 10
x_label_gap = 15
y_label_gap = 15
text_y_gap = 0.02  # Gap for the text labels in y-direction

# Calculate number of plots per A4 page and total number of pages needed
plots_per_page = 4  # Adjust as needed based on your total number of plots
total_pages = int(np.ceil(len(years) / plots_per_page))

# Loop through each page
for page_num in range(total_pages):
    start_index = page_num * plots_per_page
    end_index = min((page_num + 1) * plots_per_page, len(years))
    
    # Create a figure for the current A4 page
    fig, axs = plt.subplots(2, 2, figsize=(8.27, 11.69))  # A4 size in inches
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.4, hspace=0.4)
    
    # Flatten the axs array for easier indexing
    axs = axs.flatten()
    
    # Loop through each subplot on the current page
    for i, year_index in enumerate(range(start_index, end_index)):
        if year_index >= len(years):
            break
        
        year = years[year_index]
        yearly_data = df[df['Year'] == year]
        
        # Plot the data on the corresponding subplot
        ax = axs[i]
        ax.plot(yearly_data['Month'], yearly_data['Average_VCI'], marker='o', label=f'{year}')
        ax.set_title(f'Average VCI Changes in {year}', fontsize=title_fontsize, weight='bold')
        ax.set_xlabel('Month', fontsize=axis_label_fontsize, color='black', weight='bold', labelpad=x_label_gap)
        ax.set_ylabel('Average VCI', fontsize=axis_label_fontsize, color='black', weight='bold', labelpad=y_label_gap)
        ax.legend(fontsize=legend_fontsize)
        ax.grid(True)
        ax.set_xticks(np.arange(1, 13, 1))  # Ensure x-axis shows each month from 1 to 12
        
        # Find the maximum and minimum VCI values
        max_vci = yearly_data['Average_VCI'].max()
        min_vci = yearly_data['Average_VCI'].min()
        max_vci_month = yearly_data.loc[yearly_data['Average_VCI'].idxmax(), 'Month']
        min_vci_month = yearly_data.loc[yearly_data['Average_VCI'].idxmin(), 'Month']
        
        # Annotate the maximum and minimum VCI values
        ax.annotate(f'Max VCI: {max_vci:.2f}', xy=(max_vci_month, max_vci), xytext=(max_vci_month, max_vci + text_y_gap),
                    arrowprops=dict(facecolor='green', shrink=0.05), fontsize=text_fontsize, color='green', weight='bold')
        ax.annotate(f'Min VCI: {min_vci:.2f}', xy=(min_vci_month, min_vci), xytext=(min_vci_month, min_vci - text_y_gap),
                    arrowprops=dict(facecolor='red', shrink=0.05), fontsize=text_fontsize, color='red', weight='bold')
    
    # Save the current A4 page as PNG
    save_path = os.path.join(save_folder, f'VCI_Plots_Page_{page_num + 1}.png')
    plt.savefig(save_path, format='png', dpi=300)  # Save figure with high resolution
    plt.close()

print(f"Plots saved in folder: {save_folder}")
