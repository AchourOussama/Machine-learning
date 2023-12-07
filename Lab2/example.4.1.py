import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import f_classif, chi2,mutual_info_classif
from sklearn.datasets import load_iris

iris = load_iris()
X,y = iris.data, iris.target
chi2_score, chi_2_p_value = chi2(X,y)
f_score, f_p_value = f_classif(X,y)
mut_info_score = mutual_info_classif(X,y)
print("correlation scores of the features :")
print('chi2 score ', chi2_score)
print('F - score score ', f_score)
print('mutual info ', mut_info_score)
dataframe = pd.DataFrame(iris.data, columns=iris.feature_names)
corr = dataframe.corr()

# Print heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

#Defining a dataset with a reduced dimension
selected_features = ['petal length (cm)', 'sepal width (cm)']
reduced_data = dataframe[selected_features]
print("Reduced dataset based on selected features:")
print(reduced_data)