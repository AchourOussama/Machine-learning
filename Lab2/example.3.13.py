from sklearn.datasets import load_iris
iris = load_iris()
import pandas as pd
import numpy as np
iris_nparray = iris.data
iris_dataframe = pd.DataFrame(iris.data,columns=iris.feature_names)
iris_dataframe['group'] = pd.Series([iris.target_names[k] for k in iris.target], dtype="category")
print("IRIS data values:")
print(iris_dataframe)
print("Mean value :")
print (iris_dataframe.mean(numeric_only=True))
print("Median value :")
print (iris_dataframe.median(numeric_only=True))
print("Discretization based on equal quantiles:")
print(iris_dataframe.drop(columns=['group']).quantile(np.array([0,0.25,0.50,0.75,1])))

#The binning transforms numerical variables to categorical variables
iris_binned = pd.DataFrame()
for column in iris_dataframe.columns[:-1]:  # Exclude the 'group' column
    iris_binned[column] = pd.cut(iris_dataframe[column], bins=3)
print("Binning IrisData")
print(iris_binned)
#Get the frequency of each categorical variable
print("frequency of each categorical variable:")
category_counts = iris_binned.apply(pd.value_counts).fillna(0)
print("Frequency for each range of values:")
range_counts = pd.concat([iris_binned[column].value_counts().sort_index() for column in iris_binned.columns])
print(range_counts)
