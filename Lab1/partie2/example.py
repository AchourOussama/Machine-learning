# import pandas as pd
# lst = ['GL', 'RT', 'IMI', 'MPI', 'IIA', 'CBA', 'CH', 'BIO']
# data = {'Nom':['Ali', 'Mohamed', 'Salah', 'Fatma'],'Age':[20, 21, 19, 18]}
# df1 = pd.DataFrame(lst)
# print(df1)
# df2 = pd.DataFrame(data)
# print(df2)



import pandas as pd
data = {'Nom':['Ali', 'Salah', 'Fatma', 'Mohamed'],
        'Age':[27, 24, 22, 32],
        'Addresse':['Sfax', 'Tunis', 'Gabes', 'Sousse'],
        'Filière':['MPI', 'RT', 'GL', 'IMI']}
df = pd.DataFrame(data)
print(df[['Nom', 'Filière']])   