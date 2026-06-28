#task 3 
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# 1. Load data and handle missing values (required before scaling)
df = sns.load_dataset('titanic')
df['age'] = df['age'].fillna(df['age'].median())
df['fare'] = df['fare'].fillna(df['fare'].median())

print("--- Descriptive Statistics Before Scaling ---")
print(df[['age', 'fare']].describe().loc[['mean', 'std', 'min', 'max']])

# 2. Initialize the StandardScaler
scaler = StandardScaler()

# 3. Fit and transform the columns
# We use double brackets [['age', 'fare']] because StandardScaler expects a 2D array / DataFrame
df[['age_scaled', 'fare_scaled']] = scaler.fit_transform(df[['age', 'fare']])

print("\n--- Sample Scaled Data ---")
print(df[['age', 'age_scaled', 'fare', 'fare_scaled']].head())

print("\n--- Descriptive Statistics After Scaling ---")
print(df[['age_scaled', 'fare_scaled']].describe().loc[['mean', 'std', 'min', 'max']].round(4))
