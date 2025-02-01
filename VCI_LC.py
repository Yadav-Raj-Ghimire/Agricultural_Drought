import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


# Assuming your Excel file has a sheet named 'Sheet1' containing your data
file_path = r"D:\Working\Working2\New_Output\LC\ExcelSheet\VCI_LC.csv"
df = pd.read_csv(file_path)

# Display the first few rows to verify data loading
print(df.head())

# Define independent variables (predictors) and dependent variable (response)
X = df[['Years', 'Agricultural_Area(Sq.Km)', 'Others_LC_Area(Sq. Km)']]
y = df['VCI_Mean']

#This is necessary because statsmodels regression models do not include an intercept by default.
X = sm.add_constant(X)

# Use sm.OLS (Ordinary Least Squares) from statsmodels to fit the regression model.
model = sm.OLS(y, X).fit()

# Display detailed statistics and results of the regression model.
print(model.summary())

# Save summary table to an Excel file
summary_df = pd.DataFrame({'Coef': model.params, 'Std Err': model.bse, 't': model.tvalues, 'P>|t|': model.pvalues})
summary_df.index = ['const', 'Years', 'Agricultural_Area(Sq.Km)', 'Others_LC_Area(Sq. Km)']

summary_df.to_excel('multiple_regression_summary.xlsx', index=True)


# Scatter plot of Years vs. VCI_Mean
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.scatter(df['Years'], df['VCI_Mean'], alpha=0.8)
plt.title('Changes in VCI over the years', weight ='bold')
plt.xlabel('Years', weight ='bold')
plt.ylabel('VCI_Mean', weight ='bold')
plt.grid(True)
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')

# Scatter plot of Agricultural_Area vs. VCI_Mean
plt.subplot(1, 3, 2)
plt.scatter(df['Agricultural_Area(Sq.Km)'], df['VCI_Mean'], alpha=0.8)
plt.title('Agricultural Area Variations with VCI', weight ='bold')
plt.xlabel('Agricultural Area (km²)', weight = 'bold')
plt.ylabel('VCI_Mean', weight='bold')
plt.grid(True)
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')
# Scatter plot of Others_LC_Area vs. VCI_Mean
plt.subplot(1, 3, 3)
plt.scatter(df['Others_LC_Area(Sq. Km)'], df['VCI_Mean'], alpha=0.8,  edgecolors='w', s=100)
plt.title('Others LC Area Variation with VCI', weight ='bold')
plt.xlabel('Others_LC_Area(km²)',weight ='bold')
plt.ylabel('VCI_Mean',weight='bold')
plt.grid(True)
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('scatter_plots_high_quality.png', dpi=300)
plt.show()

