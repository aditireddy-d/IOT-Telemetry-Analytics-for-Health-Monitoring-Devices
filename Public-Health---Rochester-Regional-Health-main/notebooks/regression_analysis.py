# --------------------------------------------------------
# Multiple Linear Regression Analysis
# --------------------------------------------------------
# Goal: Identify predictors of Adult Obesity Rate
# Tools: pandas, statsmodels, seaborn, matplotlib
# --------------------------------------------------------

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('../data/obesity_usda_sample.csv')

# Define predictors and target
X = data[['% Smokers', 'Fast-food per 1k pop', '% Low-income receiving SNAP', '% Who do not exercise']]
y = data['Adult Obesity Rate']

# Add constant for intercept
X = sm.add_constant(X)

# Fit regression model
model = sm.OLS(y, X).fit()
print(model.summary())

# Residual visualization
sns.residplot(x=model.fittedvalues, y=model.resid)
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

# Save summary to file
with open('../reports/regression_summary.txt', 'w') as f:
    f.write(model.summary().as_text())
