import os
import rasterio
from rasterio.features import shapes
from collections import defaultdict
import pandas as pd

# Path to your reclassified VCI raster file
raster_path = r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\reclassify\VCI_2001_3.tif'

# Define class labels and corresponding values from the reclassified raster
class_values = {
    1.0: 'Extreme Drought',
    2.0: 'Severe Drought',
    3.0: 'Moderate Drought',
    4.0: 'Mild Drought',
    5.0: 'No Drought'
}

def calculate_area_from_raster(raster_path, class_values):
    """
    Calculate area (in square meters) for each class in the raster.

    Parameters:
    - raster_path: Path to the reclassified raster file.
    - class_values: Dictionary mapping raster values to their respective drought categories.

    Returns:
    - areas: Dictionary containing areas (in square meters) for each class.
    """
    with rasterio.open(raster_path) as src:
        areas = defaultdict(float)
        transform = src.transform

        for index, (geom, val) in enumerate(shapes(src.read(1), transform=transform)):
            if geom['type'] == 'Polygon':
                try:
                    class_label = class_values[val]
                    area = 0

                    # Calculate area using the vertices of the polygon
                    vertices = geom['coordinates'][0]
                    for i in range(len(vertices) - 1):
                        x1, y1 = vertices[i]
                        x2, y2 = vertices[i + 1]
                        area += x1 * y2 - x2 * y1

                    areas[class_label] += abs(area) / 2

                except Exception as e:
                    print(f"Error processing geometry {index}: {e}")
                    continue

    return areas

# Calculate areas for each class
class_areas = calculate_area_from_raster(raster_path, class_values)

# Convert areas to square kilometers for easier interpretation
class_areas_km2 = {key: value / 1000000 for key, value in class_areas.items()}

# Create a DataFrame for the table
df = pd.DataFrame(class_areas_km2.items(), columns=['Drought Class', 'Area (square kilometers)'])

# Print or display the table
print("Area Calculation Results:")
print(df)
