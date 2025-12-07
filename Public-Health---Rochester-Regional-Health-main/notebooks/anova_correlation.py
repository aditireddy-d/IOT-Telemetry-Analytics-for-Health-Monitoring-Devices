# --------------------------------------------------------
# ANOVA and Correlation Analysis
# --------------------------------------------------------
# Goal: Compare obesity across inactivity quartiles & study variable relationships
# Tools: pandas, scipy, seaborn, matplotlib
# --------------------------------------------------------

import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('../data/obesity_usda_sample.csv')

# Create inactivity quartiles
data['Exercise_Quartile'] = pd.qcut(data['% Who do not exercise'], 4, labels=['Q1','Q2','Q3','Q4'])

# Perform ANOVA
groups = [group['Adult Obesity Rate'].values for _, group in data.groupby('Exercise_Quartile')]
f_stat, p_val = stats.f_oneway(*groups)
print(f"F-statistic: {f_stat:.2f}, p-value: {p_val:.4f}")

# Boxplot visualization
sns.boxplot(x='Exercise_Quartile', y='Adult Obesity Rate', data=data, palette='Set2')
plt.title('Obesity Rate by Inactivity Quartiles')
plt.show()

# Correlation matrix
corr = data[['Adult Obesity Rate', '% Who do not exercise', '% Smokers', 
             'Fast-food per 1k pop', '% Low-income receiving SNAP']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.3f')
plt.title('Correlation Matrix')
plt.show()

# Print correlation with obesity
print(corr['Adult Obesity Rate'].sort_values(ascending=False))

# Save correlation matrix
corr.to_csv('../reports/correlation_matrix.csv')
