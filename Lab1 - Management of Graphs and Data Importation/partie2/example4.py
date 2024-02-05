import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("partie2/Automobile.csv", index_col ="company")
desc = data.describe()
print(desc) 