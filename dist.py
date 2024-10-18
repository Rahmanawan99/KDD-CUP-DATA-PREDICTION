import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#this file does the exploraty Data Analysis

# Load data
df = pd.read_csv('.csv')

# Get the summary statistics for numerical columns
summary_stats = df.describe()

# Save the stats CSV file since there are many colums to read from terminal
summary_stats.to_csv('summary_statistics.csv')
print("Summary statistics saved to summary_statistics.csv.")

# Select a specific categorical column to viz its distribution as a bar chart
column = 'Attack' #change columns as needed

plt.figure(figsize=(12, 6))
sns.countplot(y=df[column], order=df[column].value_counts().index[:10])  # Top 10 most frequent values
plt.title(f'Count Plot of {column}')
plt.show()
