import pandas as pd
import scipy.io as sio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import missingno as mano

#Code to see the stats of the main file

#file_path = 'kddcup 4.data_10_percent.gz'
#file_path = 'alldata.mat'
file_path = 'all_data.csv'
df = pd.read_csv(file_path)
#df_cleaned = df.drop_duplicates()


attack_distribution = df['Attack'].value_counts()
symbol_distribution = df['protocol_typesymbolic'].value_counts().nunique()
protocol_distribution = df['protocol_typesymbolic'].value_counts()
flag_distribution = df['flagsymbolic'].value_counts()
flag_count = df['flagsymbolic'].value_counts().nunique()

# print(df_cleaned.isnull().sum())
# df_cleaned.to_csv('cleaned_data.csv', index=False)

# print("Duplicates removed and data saved.")

print (df_cleaned.shape)
print (df.dtypes)
print (df_cleaned.columns)
print (df_cleaned.head)
print (attack_distribution)
print (symbol_distribution)
print (protocol_distribution)
print (flag_distribution)
print (flag_count)