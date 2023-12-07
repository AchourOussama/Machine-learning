import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/cpu-performance/machine.data'
names=['constructor','Model','MYCT','MMIN','MMAX','CACH','CHMIN','CHMAX','PRP','ERP']
dataset = pd.read_csv(url, names=names)
print("data:")
print(dataset)
# Z-Score standardisation
std_scaler = StandardScaler()
data_to_std=dataset[['MYCT', 'MMAX']]
df_std = std_scaler.fit_transform(data_to_std)
print('\n********** Standardisation*********\n')
print('Mean and std value of the MYCT feature  after the standardisation:\nmean{:.2f}\nstd{:.2f}'.format(df_std[:,0].mean(),df_std[:,0].std()))
print('\n')
print('Mean and std value of the MMAX feature  after the standardisation:\nmean{:.2f}\nstd{:.2f}'.format(df_std[:,1].mean(),df_std[:,1].std()))
print('\n')
print('Minimal and Maximal value of the MYCT feature after standardisation: \nMIN={:.2f}, MAX={:.2f}'.format(df_std[:,0].min(), df_std[:,0].max()))
print('\n')
print('Minimal and Maximal value of the MMAX feature after standardisation: \nMIN={:.2f}, MAX={:.2f}'.format(df_std[:,1].min(), df_std[:,1].max()))
print('Values after standardisation')
print(df_std)