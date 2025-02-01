import pandas as pd
import matplotlib.pyplot as plt

# Path to the XLSX file containing the data
xlsx_file = r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\ExcelSheet\DroughtAreaKM.xlsx'

try:
    # Read the data from XLSX into a pandas DataFrame
    df = pd.read_excel(xlsx_file, sheet_name='Sheet1', engine='openpyxl', header=0)  # Adjust header as needed

    # Print the first few rows to inspect the DataFrame
    print(df.head())

    # Plotting each drought category over the years
    categories = ['Extreme Drought Area (Sq.Km)', 'Severe Drought (Sq Km)', 
                  'Moderate Drought (Sq Km)', 'Mild Drought (Sq Km)', 'No Drought (Sq Km)']

    colors = ['darkred', 'red', 'orange', 'yellowgreen', 'darkgreen']
    labels = ['Extreme', 'Severe', 'Moderate', 'Mild', 'No']

    # Adjust figure DPI for high resolution
    plt.figure(figsize=(12, 8), dpi=120)  # Increase dpi for higher resolution

    for i, category in enumerate(categories):
        plt.plot(df['Years'], df[category], marker='o', color=colors[i], label=labels[i])

    plt.title('Drought Area Trends (2001-2019)', fontsize=16)
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Area (Sq. Km)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.xticks(df['Years'], rotation=45, fontsize=12)  # Adjust font size for x-axis ticks

    # Adjust font properties for all other text elements
    plt.tight_layout()

    # Save the plot as a high-resolution image
    plt.savefig('drought_area_trends.png', dpi=300)  # Adjust dpi for desired resolution
    plt.show()

except Exception as e:
    print(f"Error reading or processing the data: {e}")
