import pandas as pd

df = pd.read_csv("/kaggle/input/datasets/tamimm91437/mhealth/Before_After_Intervention_Comparison.csv")

df.head()
df.info()
df.isnull().sum()
df.describe()
