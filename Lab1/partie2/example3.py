import pandas as pd
data = pd.read_csv("Automobile.csv", index_col ="company")
first = data.loc["honda"]
second = data.loc["mazda"]
third = data["price"]
print(first, "\n\n\n", second, "\n\n\n", third)