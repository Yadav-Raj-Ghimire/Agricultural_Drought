import pandas as pd
import glob
from simpledbf import Dbf5

# Define the directory containing the DBF files and the output file path
dbf_directory = r'D:\Working\Working2\New_Output\integratedData\LULC_VCI'
output_file_path = r'D:\Working\Working2\New_Output\integratedData\LULC_VCI\LULC_VCI_merged.csv'

# Find all DBF files in the directory
dbf_files = glob.glob(f"{dbf_directory}/*.dbf")

# Initialize an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

# Process each DBF file
for dbf_file in dbf_files:
    # Load the DBF file into a DataFrame
    dbf = Dbf5(dbf_file)
    df = dbf.to_dataframe()

    # Identify the year from the file name
    year = int(dbf_file.split('\\')[-1].split('_')[-1].split('.')[0])

    # Reshape the DataFrame to have 'Year' and 'Value' columns
    value_columns = [col for col in df.columns if col.startswith('VALUE_')]
    
    # Create a new DataFrame for long format with 'Year' and 'Value' columns
    df_long = pd.DataFrame()

    # Melt the DataFrame to long format
    for col in value_columns:
        month_idx = int(col.split('_')[-1])
        temp_df = df[[col]].rename(columns={col: 'Value'})
        temp_df['Month'] = month_idx
        temp_df['Year'] = year
        df_long = pd.concat([df_long, temp_df], ignore_index=True)

    # Append to the merged DataFrame
    merged_df = pd.concat([merged_df, df_long], ignore_index=True)

# Filter out rows with zero values
merged_df = merged_df[merged_df['Value'] != 0]

# Drop unnecessary columns and reorder the DataFrame
merged_df = merged_df[['Year', 'Month', 'Value']]

# Save the merged DataFrame to a CSV file
merged_df.to_csv(output_file_path, index=False)

print(f"Merged data saved to {output_file_path}")
