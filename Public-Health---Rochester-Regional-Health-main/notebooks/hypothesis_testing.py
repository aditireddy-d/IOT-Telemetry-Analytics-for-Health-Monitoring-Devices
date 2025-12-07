# --------------------------------------------------------
# Hypothesis Testing
# --------------------------------------------------------
# Goal: Test group differences using median splits (t-tests)
# Tools: pandas, scipy
# --------------------------------------------------------

import pandas as pd
from scipy import stats

# Load dataset
data = pd.read_csv('../data/obesity_usda_sample.csv')

def median_split_test(column):
    median_val = data[column].median()
    low = data[data[column] <= median_val]['Adult Obesity Rate']
    high = data[data[column] > median_val]['Adult Obesity Rate']
    t_stat, p_val = stats.ttest_ind(low, high)
    return median_val, t_stat, p_val

factors = ['Fast-food per 1k pop', '% Smokers', 'Low income & >1 mile to store']

print("T-Test Results for Obesity Rate Differences by Median Split:\n")
for factor in factors:
    median, t, p = median_split_test(factor)
    print(f"{factor}: Median={median:.2f}, T={t:.2f}, P={p:.4f}")

# Save results
with open('../reports/hypothesis_test_results.txt', 'w') as f:
    for factor in factors:
        median, t, p = median_split_test(factor)
        f.write(f"{factor}: Median={median:.2f}, T={t:.2f}, P={p:.4f}\n")
