import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/cpu-performance/machine.data'
names=['constructor','Model','MYCT','MMIN','MMAX','CACH','CHMIN','CHMAX','PRP','ERP']

dataset = pd.read_csv(url, names=names)
print("data:")
print(dataset)
# Apply MIN MAX SCALING on MYCT et MMAX
data_to_scale = dataset[['MYCT', 'MMAX']]
minmax_scale = MinMaxScaler().fit(data_to_scale)
df_minmax = minmax_scale.transform(data_to_scale)
print("df_minmax")
print(df_minmax)
print('\n********** Normalisation*********\n')
print('Mean value after the Min max Scaling :\nMYCT={:.2f},MMAX={:.2f}'.format(df_minmax[:,0].mean(), df_minmax[:,1].mean()))
print('\n')
print('Minimal and Maximal value of the MYCT feature after minmax scaling: \nMIN={:.2f}, MAX={:.2f}'.format(df_minmax[:,0].min(), df_minmax[:,0].max()))
print('\n')
print('Minimal and Maximal value of the MMAX feature after minmax scaling: \nMIN={:.2f}, MAX={:.2f}'.format(df_minmax[:,1].min(), df_minmax[:,1].max()))
print("data after normalisation")
print(df_minmax)