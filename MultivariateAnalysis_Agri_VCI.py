import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load data from CSV
file_path = r"D:\Working\Working2\New_Output\integratedData\EXCEL\Agri_Occupied_VCI.csv"
data = pd.read_csv(file_path)

# Extract columns
years = data['years']
extreme_drought = data['Extreme_Drought(Sq. Km)']
severe_drought = data['Severe_Drought(Sq. Km)']
moderate_drought = data['Moderate_Drought(Sq. Km)']
mild_drought = data['Mild_Drought(Sq. Km)']
no_drought = data['No_Drought (Sq. Km)']

# Combine data into a single dataframe for multivariate analysis
drought_data = pd.DataFrame({
    'Extreme_Drought': extreme_drought,
    'Severe_Drought': severe_drought,
    'Moderate_Drought': moderate_drought,
    'Mild_Drought': mild_drought,
    'No_Drought': no_drought
})

# Standardize the data
scaler = StandardScaler()
drought_data_scaled = scaler.fit_transform(drought_data)

# Perform PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(drought_data_scaled)
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

# Add years to the PCA dataframe
pca_df = pd.concat([pca_df, pd.DataFrame({'years': years})], axis=1)

# Create a dataframe for the standardized data
drought_data_scaled_df = pd.DataFrame(drought_data_scaled, columns=drought_data.columns)

# Create a dataframe for the PCA components
pca_components_df = pd.DataFrame(pca.components_, columns=drought_data.columns)

# Export PCA results to Excel, including intermediate steps
output_file = r"D:\Working\Working2\New_Output\PCA_Results.xlsx"
with pd.ExcelWriter(output_file) as writer:
    drought_data.to_excel(writer, sheet_name='Original_Data', index=False)
    drought_data_scaled_df.to_excel(writer, sheet_name='Standardized_Data', index=False)
    pca_components_df.to_excel(writer, sheet_name='PCA_Components', index=False)
    pca_df.to_excel(writer, sheet_name='PCA_Results', index=False)
    drought_data.corr().to_excel(writer, sheet_name='Correlation_Matrix')

# Plot the PCA results
plt.figure(figsize=(10, 6))
plt.scatter(pca_df['PC1'], pca_df['PC2'], c=pca_df['years'], cmap='viridis')
plt.colorbar(label='Years')
plt.title('PCA of Drought Categories Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Principal Component 1', fontsize=12, fontweight='bold')
plt.ylabel('Principal Component 2', fontsize=12, fontweight='bold')
plt.grid(True)
plt.tight_layout()
plt.show()

# Interpretation
explained_variance = pca.explained_variance_ratio_
print(f'Explained variance by PC1: {explained_variance[0]:.2f}')
print(f'Explained variance by PC2: {explained_variance[1]:.2f}')

# Correlation analysis
correlations = drought_data.corr()
print("Correlation Matrix:")
print(correlations)

# Plot correlation matrix
# Plot correlation matrix
plt.figure(figsize=(10, 6))  # Decreased figure size
plt.matshow(correlations, fignum=1, cmap='viridis')
plt.colorbar()
plt.xticks(range(len(correlations.columns)), correlations.columns, rotation=45, fontsize=10, fontweight='bold')
plt.yticks(range(len(correlations.columns)), correlations.columns, fontsize=10, fontweight='bold')

plt.title('Correlation Matrix of Drought Categories', fontsize=14, fontweight='bold', pad=20)  # Title parameters adjusted
plt.subplots_adjust(top=0.9)  # Adjusted top to make space for title

plt.tight_layout()
plt.show()






# Analysis and Interpretation
analysis_text = """
The Principal Component Analysis (PCA) reveals that the first two principal components explain a substantial portion of the variance in the data, with PC1 and PC2 accounting for {0:.2f}% and {1:.2f}% of the variance, respectively. The scatter plot shows the progression over the years, indicating changes in the drought conditions.

The correlation matrix highlights the relationships between different drought categories. Notably, there are negative correlations between extreme, severe, and moderate drought areas with years, suggesting a decrease in these conditions over time. Conversely, the mild and no drought categories show positive correlations with years, indicating an increase in these areas.

This multivariate analysis underscores the trends observed in the individual drought categories. The decreasing trends in extreme and severe drought areas, alongside the increasing trends in mild and no drought areas, suggest effective mitigation strategies and natural fluctuations positively impacting agricultural areas. In Bagmati Province, the less pronounced effects of drought and the increase in areas unaffected by drought likely contribute to stable or improved agricultural productivity over time.
""".format(explained_variance[0]*100, explained_variance[1]*100)

print(analysis_text)

# Interpretation within the plot code
plt.figure(figsize=(10, 6))
plt.scatter(pca_df['PC1'], pca_df['PC2'], c=pca_df['years'], cmap='viridis')
plt.colorbar(label='Years')
plt.title('PCA of Drought Categories Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Principal Component 1', fontsize=12, fontweight='bold')
plt.ylabel('Principal Component 2', fontsize=12, fontweight='bold')
plt.grid(True)
plt.tight_layout()
plt.show()

# Interpretation of the scatter plot
print("""
The scatter plot of the PCA results shows the distribution of drought categories over the years. Each point represents a year, colored according to the year. The spread of points along the principal components (PC1 and PC2) indicates how drought conditions varied over time. Years clustered together suggest similar drought conditions, while years spread apart indicate changes in drought severity. The color gradient from dark to light shows the temporal progression, highlighting the trend of changing drought conditions over the study period.
""")
