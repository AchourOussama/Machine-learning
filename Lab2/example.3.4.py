import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer as Imputer

# Create an empty dataset
df = pd.DataFrame()

# Create two variables called x0 and x1. Make the first value of x1 a missing value
df['x0'] =[0.3051,0.4949,0.6974,0.3769,0.2231,0.341,0.4436,0.5897,0.6308,0.5]
df['x1'] =[np.nan,0.2654,0.2615,0.5846,0.4615,0.8308,0.4962,0.3269,0.5346,0.6731]

# View the dataset
print("Data before imputation :")
print(df)

# Create an imputer object that looks for 'Nan' values, then replaces them with the mean value of the feature by columns (axis=0)
print("chercher les valeurs manquantes par la moyenne de la colonne")
mean_imputer = Imputer(missing_values=np.nan, strategy='mean')

# Apply the imputer on the df dataset
mean_imputed_df = pd.DataFrame(mean_imputer.fit_transform(df), columns=df.columns)
print("data after imputation : mean")
print(mean_imputed_df)

#Change the imputer's strategy
print("data after imputation : median") 
median_imputer = Imputer(missing_values=np.nan, strategy='median')
median_imputed_df=pd.DataFrame(median_imputer.fit_transform(df), columns=df.columns)
print(median_imputed_df)