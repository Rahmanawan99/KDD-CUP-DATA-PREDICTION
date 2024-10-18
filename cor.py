import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#We re dropping non related columns here

file_path = 'cleaned_data.csv'
df = pd.read_csv(file_path)
#Droping these columns as they are not corellated
df_cleaned = df.drop(columns=['root_shellcontinuous', 'num_file_creationscontinuous', 'num_rootcontinuous', 'root_shellcontinuous',
'num_compromisedcontinuous', 'num_failed_loginscontinuous', 'wrong_fragmentcontinuous'])

print (df_cleaned.shape)

# Save the updated dataset
df_cleaned.to_csv('cleaned_data_drop.csv', index=False)
print("Column dropped and data saved.")
