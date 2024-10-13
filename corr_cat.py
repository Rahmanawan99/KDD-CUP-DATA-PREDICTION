# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.utils import class_weight
import numpy as np
from tensorflow.keras.optimizers import SGD

#Here i made a corellation graph to see categotical values, not required but if you want to see
modified_df = pd.read_csv('cleaned_data_drop.csv')

#Encode target variable
label_encoder = LabelEncoder()
modified_df['Attack'] = label_encoder.fit_transform(modified_df['Attack'])

# encode the other categortical columns
modified_df = pd.get_dummies(modified_df, columns=['protocol_typesymbolic', 'servicesymbolic', 'flagsymbolic'])

# Select only the categorical columns from the dataset
categorical_columns = modified_df.filter(regex='protocol_typesymbolic|servicesymbolic|flagsymbolic|Attack')

corr_matrix = categorical_columns.corr()


plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=False, cmap='coolwarm')
plt.title("Correlation Matrix of Categorical Columns")
plt.show()
