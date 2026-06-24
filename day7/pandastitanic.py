import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris(as_frame=True)

df = iris.frame

print(df.head())
