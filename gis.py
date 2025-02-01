import os
import geopandas as gpd
import matplotlib.pyplot as plt

# Construct the path to your shapefile using os.path.join
shapefile_dir = r'D:\Working\Working2\New_Output\Bagmati_data'
shapefile_name = 'Bagmati_Road.shp'
shapefile_path = os.path.join(shapefile_dir, shapefile_name)

# Check if the shapefile exists
if not os.path.exists(shapefile_path):
    raise ValueError(f"Shapefile not found at {shapefile_path}")

# Load the shapefile using geopandas
gdf = gpd.read_file(shapefile_path)

# Plot the data
gdf.plot()
plt.title('GIS Data Plot')
plt.show()
