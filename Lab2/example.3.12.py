import pandas as pd
import numpy as np
df = pd.DataFrame({'Map': [0,0,0,1,1,2,2], 'Values':
[1,2,3,5,4,2,5]})
df['Sum'] = df.groupby('Map')['Values'].transform('sum')
df['Moy'] = df.groupby('Map')['Values'].transform('mean')
print (df)