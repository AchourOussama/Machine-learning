import pandas as pd
df = pd.DataFrame({'A': [2,3,1],'B': [1,2,3],'C': [5,3,4]})
print(df)
print("remove data using row index")
#remove data using row index
df=df.drop(df.last_valid_index())
print (df)
print("remove data using column name")
#remove data using column name
df=df.drop(columns='A')
print (df)