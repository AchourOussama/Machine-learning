import pandas as pd
import numpy as np
import copy
s = pd.DataFrame([1, 2, 3, np.NaN, 5, 6, None])

df = pd.DataFrame({'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', None],
                   'style': ['cup', None, 'cup', 'pack', 'pack'],
                   'rating': [4, 4, np.NaN, 15, 5]})

df1=df.copy()
#visualizing missing values : true means a detection of a missing data
print("visualizing missing values : true means a detection of a missing data")

### using loops :

# n=0
# for index, row in df.iterrows():
#     for column in df.columns:
#         cell_value = row[column]
#         if pd.isnull( cell_value):
#             print(f"value missed at :\ncolumn:{column}\nrow:{index} \n")
#             n+=1

### using dataframe built-in functions   
      
#creating a boolean mask of the dataframe to identify rows of missing values
mask =df.isnull()

#isolating missing values
print ("isolating missing values")
print(df[mask.any(axis=1)])

#number of missing values per column and in total
print("total number of  missing values:",mask.any(axis=1).sum())
print("number of missing values per column:\n",mask.sum())

#filling the missing data with the mean value 
print("filling the missing data with the mean value")
mean=df['rating'].mean()
for column in df.columns:
    df[column].fillna(value=mean,inplace=True)
print(df)

#removing rows containing missing values
print ("removing rows containing missing values")
print(df1.dropna())