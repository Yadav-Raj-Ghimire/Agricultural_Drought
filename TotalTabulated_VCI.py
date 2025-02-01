import os
import rasterio
from rasterio.features import shapes
from collections import defaultdict
import pandas as pd
from shapely.geometry import shape

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

def calculate_overlap_areas(raster_path, class_values):
    """
    Calculate overlap areas (in square meters) between different classes in the raster.

    Parameters:
    - raster_path: Path to the reclassified raster file.
    - class_values: Dictionary mapping raster values to their respective drought categories.

    Returns:
    - overlap_areas: Nested dictionary containing overlap areas (in square meters) for each class combination.
    """
    overlap_areas = defaultdict(lambda: defaultdict(float))

    with rasterio.open(raster_path) as src:
        transform = src.transform

        # Read the raster data and shapes
        raster_data = src.read(1)
        raster_shapes = shapes(raster_data, transform=transform)

        # Iterate through each geometry and value in the raster
        for index1, (geom1, val1) in enumerate(raster_shapes):
            try:
                if geom1['type'] == 'Polygon':
                    class_label1 = class_values[val1]
                    geom1_shape = shape(geom1['geometry'])  # Convert to Shapely geometry

                    # Compare with other geometries to find overlaps
                    for index2, (geom2, val2) in enumerate(raster_shapes):
                        try:
                            if geom2['type'] == 'Polygon':
                                class_label2 = class_values[val2]
                                geom2_shape = shape(geom2['geometry'])  # Convert to Shapely geometry

                                intersection = geom1_shape.intersection(geom2_shape)
                                if not intersection.is_empty:
                                    area = intersection.area
                                    overlap_areas[class_label1][class_label2] += area

                        except Exception as e:
                            print(f"Error processing geometry {index2}: {e}")
                            continue

            except Exception as e:
                print(f"Error processing geometry {index1}: {e}")
                continue

    return overlap_areas

# Calculate overlap areas for each class combination
overlap_areas = calculate_overlap_areas(raster_path, class_values)

# Convert areas to square kilometers for easier interpretation
overlap_areas_km2 = {class1: {class2: value / 1000000 for class2, value in values.items()} for class1, values in overlap_areas.items()}

# Create a DataFrame for the table
df_overlap = pd.DataFrame(columns=['Class from Raster 1'] + list(class_values.values()))
for class1, overlap_dict in overlap_areas_km2.items():
    df_overlap = df_overlap.append({'Class from Raster 1': class1, **overlap_dict}, ignore_index=True)

# Print or display the table
print("Overlap Area Calculation Results:")
print(df_overlap)
