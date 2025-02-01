import os
import matplotlib.pyplot as plt
import rasterio
from matplotlib.colors import ListedColormap, BoundaryNorm

# Directory containing the VCI raster files
raster_directory = r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\reclassify'

# Directory to save the output images
output_directory = r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\output_images'
os.makedirs(output_directory, exist_ok=True)

# Function to get the VCI raster file paths for a given year
def get_vci_raster_paths(directory, year):
    return [os.path.join(directory, f'VCI_{year}_{month}.tif') for month in range(3, 4)]

# Function to plot VCI map for a given year
def plot_vci_map(raster_path, year):
    try:
        with rasterio.open(raster_path) as src:
            vci_data = src.read(1, masked=True)  # Read VCI data from the first band
            
            # Define boundaries, ticks, and labels for the custom colormap
            boundaries = [1, 2, 3, 4, 5, 6]
            ticks = [1.5, 2.35, 3.50, 4.65, 5.5]
            labels = ['Extreme Drought', 'Severe Drought', 'Moderate Drought', 'Mild Drought', 'No Drought']
            
            # Create a custom colormap
            colors = ['darkred', 'red', 'orange', 'yellowgreen', 'green']
            cmap = ListedColormap(colors)
            norm = BoundaryNorm(boundaries, cmap.N)
            
            plt.figure(figsize=(8, 6))
            plt.imshow(vci_data, cmap=cmap, norm=norm)
            
            # Add colorbar with custom ticks and labels
            cbar = plt.colorbar(ticks=ticks, boundaries=boundaries)
            cbar.ax.set_yticklabels(labels)
            cbar.set_label('VCI Class')
            
            # Add north arrow pointing upward
            plt.annotate('N', xy=(0.95, 0.95), xytext=(0.95, 0.85),
                         arrowprops=dict(facecolor='black', shrink=0.05),
                         fontsize=12, ha='center', va='center', xycoords='axes fraction')
            
            plt.title(f'VCI Map - {year}')
            plt.axis('off')

            # Save the figure to the specified directory
            output_path = os.path.join(output_directory, f'VCI_Map_{year}.png')
            plt.savefig(output_path, bbox_inches='tight')
            
            plt.show()
            
    except Exception as e:
        print(f"Error processing {raster_path}: {e}")

# Loop through years from 2001 to 2002 and plot VCI maps
for year in range(2001, 2003):
    raster_paths = get_vci_raster_paths(raster_directory, year)
    for raster_path in raster_paths:
        plot_vci_map(raster_path, year)
