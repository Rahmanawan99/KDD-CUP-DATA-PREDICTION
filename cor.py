import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'cleaned_data.csv'
df = pd.read_csv(file_path)
#Droping these columns as they are not corellated
df_cleaned = df.drop(columns=['root_shellcontinuous', 'num_file_creationscontinuous', 'num_rootcontinuous', 'root_shellcontinuous',
'num_compromisedcontinuous', 'num_failed_loginscontinuous', 'wrong_fragmentcontinuous'])

print (df_cleaned.shape)

# Save the updated DataFrame
df_cleaned.to_csv('cleaned_data_drop.csv', index=False)
print("Column dropped and data saved.")

# # Remove the comments to see the correlation for yourseld

# float_cols = df_cleaned.select_dtypes(include=['float64'])

# corr_matrix = float_cols.corr()

# plt.figure(figsize=(12, 8))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
# plt.title('Correlation Matrix of Continuous Variables')
# plt.tight_layout()
# plt.show()
