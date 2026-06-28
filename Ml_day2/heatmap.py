#task 2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Recreate the pipeline dataset
np.random.seed(42)
n_samples = 1000
data = {
    'LotFrontage': np.random.choice(
        [60.0, 70.0, 80.0, np.nan], size=n_samples, p=[0.4, 0.3, 0.2, 0.1]
    ),
    'GrLivArea': np.random.randint(800, 3500, size=n_samples),
    'GarageCars': np.random.choice(
        [1.0, 2.0, 3.0, np.nan], size=n_samples, p=[0.3, 0.5, 0.18, 0.02]
    ),
    'MSZoning': np.random.choice(
        ['RL', 'RM', 'C (all)', np.nan], size=n_samples, p=[0.7, 0.2, 0.08, 0.02]
    ),
    'KitchenQual': np.random.choice(
        ['Gd', 'TA', 'Ex', 'Fa'], size=n_samples, p=[0.4, 0.4, 0.1, 0.1]
    ),
    'SalePrice': np.random.randint(100000, 400000, size=n_samples),
}
df = pd.DataFrame(data)

# Quick fill-in for numeric missing rows before correlation step
df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].median())
df['GarageCars'] = df['GarageCars'].fillna(df['GarageCars'].median())

# One-hot encode the categorical values
df_encoded = pd.get_dummies(
    df, columns=['MSZoning', 'KitchenQual'], drop_first=False
)

# 2. Compute Pearson correlation matrix
corr_matrix = df_encoded.corr()

# 3. Identify top 5 features correlated with SalePrice (excluding itself)
# We take the absolute values because negative correlations are equally predictive
top_5_features = (
    corr_matrix['SalePrice']
    .drop('SalePrice')
    .abs()
    .sort_values(ascending=False)
    .head(5)
)

print("--- Top 5 Features Correlated with SalePrice ---")
print(top_5_features.round(4))

# 4. Generate and plot the correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    linewidths=0.5,
    square=True,
)
plt.title('Correlation Heatmap - House Prices Dataset Features')
plt.tight_layout()
plt.show()
