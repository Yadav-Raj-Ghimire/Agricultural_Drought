import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Path to the XLSX file containing the data
xlsx_file = r'D:\Working\Working2\New_Output\GEEimages\Bagmati_march\ExcelSheet\DroughtAreaKM.xlsx'

try:
    # Read the data from XLSX into a pandas DataFrame
    df = pd.read_excel(xlsx_file, sheet_name='Sheet1', engine='openpyxl', header=0)  # Adjust header as needed

    # Plotting each drought category over the years
    categories = ['Extreme Drought Area (Sq.Km)', 'Severe Drought (Sq Km)', 
                  'Moderate Drought (Sq Km)', 'Mild Drought (Sq Km)', 'No Drought (Sq Km)']

    colors = ['darkred', 'red', 'orange', 'yellowgreen', 'darkgreen']
    labels = ['Extreme', 'Severe', 'Moderate', 'Mild', 'No']

    plt.figure(figsize=(12, 8))

    # Loop through each category to plot and calculate regression
    for i, category in enumerate(categories):
        plt.subplot(3, 2, i+1)  # Creating subplots for each category
        plt.plot(df['Years'], df[category], marker='o', color=colors[i], label=labels[i])
        plt.title(f'{labels[i]} Drought Area', fontweight='bold')  # Title in bold
        plt.xlabel('Years', fontweight='bold')  # X-axis label in bold
        plt.ylabel('Area (Sq. Km)', fontweight='bold')  # Y-axis label in bold
        plt.legend(fontsize='large', title_fontsize='15', frameon=False)  # Legend with increased font size
        plt.grid(True)

        # Set x-axis ticks with integer years
        plt.xticks(df['Years'].astype(int), rotation=45, fontsize=10, fontweight='bold')

        # Calculate regression line
        slope, intercept, r_value, p_value, std_err = linregress(df['Years'], df[category])
        regression_line = slope * df['Years'] + intercept
        plt.plot(df['Years'], regression_line, color='black', linestyle='--', label=f'Regression (r={r_value:.2f})', linewidth=1.5)

        # Add correlation coefficient to the plot
        plt.text(0.1, 0.9, f'Correlation Coefficient: {r_value:.2f}', transform=plt.gca().transAxes, fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig('drought_area_trends_regression.png', dpi=500)  # Save the plot as high-resolution PNG with 500 dpi
    plt.show()

except Exception as e:
    print(f"Error reading or processing the data: {e}")
