import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [2,1,2,3,3,5,4],'B': [1,2,3,5,4,2,5],'C': [5,3,4,1,1,2,3]})
print(df)

#sorting data based on the column 'A'
print("sorting data based on the column 'A' ")
df = df.sort_values(by='A')
print (df)

#shuffling data
print("shuffling data")
index = df.index.tolist()
np.random.shuffle(index)
df = df.iloc[index]
df.reset_index(inplace=True,drop=True)
print (df)