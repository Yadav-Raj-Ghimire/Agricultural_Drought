import os
import pandas as pd

# Directory containing the CSV files
directory = r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\SPI'  # Change this to your directory path

# List to hold dataframes
dataframes = []

# Verify if directory exists
if not os.path.isdir(directory):
    print(f"The directory {directory} does not exist.")
else:
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            print(f"Reading file: {file_path}")  # Debug print
            # Read the CSV file and append it to the list
            df = pd.read_csv(file_path)
            dataframes.append(df)
    
    # Check if any dataframes were added to the list
    if len(dataframes) == 0:
        print("No CSV files were found in the directory.")
    else:
        # Concatenate all dataframes in the list
        merged_df = pd.concat(dataframes, ignore_index=True)
        
        # Save the merged dataframe to a new CSV file
        output_path = r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\SPI_merged.csv'  # Ensure the file path includes a filename with .csv extension
        merged_df.to_csv(output_path, index=False)
        
        print(f"All CSV files merged into {output_path}")
