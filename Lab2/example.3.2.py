import pandas as pd
df = pd.DataFrame({'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie','Indomie'],
                    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
                    'rating': [4, 4, 3.5, 15, 5]})

#original data 
print("Data : \n")
print (df)

#seeing for each row whether is it duplicated or not  
search = pd.DataFrame.duplicated(df)
print(search)
print("\n duplicated data (duplicated rows)\n")

#search for only duplicated rows
print (search[search == True])

#number of duplicated data 
print (search.sum())

#removing duplicated data 
print("\n removing duplicated data (duplicated rows) \n")
unique_data=df.drop_duplicates()
print(unique_data)