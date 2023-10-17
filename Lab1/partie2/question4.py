import pandas as pd
data = pd.read_csv("partie2/Automobile.csv", index_col ="company")
data_first = data.head(5)


print(" 5 first lines ")
print(data_first)

print(" 5 last lines ")
data_last = data.tail(5)

print(data_last)