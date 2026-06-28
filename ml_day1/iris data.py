import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df.hist(figsize=(10, 6), bins=15, color='steelblue', edgecolor='white')
plt.suptitle("Feature Histograms")
plt.tight_layout()
plt.show()
sns.pairplot(df, hue='species')
plt.suptitle("Pair Plot", y=1.02)
plt.show()
