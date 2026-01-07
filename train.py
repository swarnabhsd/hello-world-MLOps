
from sklearn.datasets import load_iris
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.head())
print(df)
print("Target_Names: ",iris.target_names)
print(load_iris())
