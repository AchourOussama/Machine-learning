import pandas as pd
car_colors = pd.Series(['Blue', 'Green', 'Red'],dtype='category')
car_data = pd.Series(pd.Categorical(['Blue', 'Green', 'Red', 'Green', 'Red', 'Green'],categories=car_colors, ordered=False))
car_data.cat.categories = ["Blue_Red", "Green", "Red"]
print (car_data.loc[car_data.isin(['Red'])])
car_data.loc[car_data.isin(['Red'])] = 'Blue_Red'
print (car_data)