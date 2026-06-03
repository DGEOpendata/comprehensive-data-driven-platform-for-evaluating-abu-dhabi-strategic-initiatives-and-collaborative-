python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_excel('2026 - Sub Awards Nomination Open Data.xlsx')

# Example Analysis: Budget planned vs actual
# Group data by initiative and calculate total planned and actual budgets
budget_analysis = data.groupby('Initiative')['Planned Budget', 'Actual Budget'].sum()

# Plotting the planned vs actual budgets
plt.figure(figsize=(12, 8))
budget_analysis.plot(kind='bar', stacked=True, color=['skyblue', 'orange'])
plt.title('Planned vs Actual Budget by Initiative')
plt.xlabel('Initiative')
plt.ylabel('Budget Amount (AED)')
plt.legend(['Planned Budget', 'Actual Budget'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the processed data for further analysis
budget_analysis.to_csv('budget_analysis_summary.csv')

# Example of generating a summary report
def generate_summary(data):
    total_initiatives = data['Initiative'].nunique()
    total_budget_planned = data['Planned Budget'].sum()
    total_budget_actual = data['Actual Budget'].sum()
    
    summary = {
        'Total Initiatives': total_initiatives,
        'Total Planned Budget (AED)': total_budget_planned,
        'Total Actual Budget (AED)': total_budget_actual,
        'Budget Utilization (%)': (total_budget_actual / total_budget_planned) * 100
    }
    
    return summary

summary = generate_summary(data)
print('Summary Report:', summary)
