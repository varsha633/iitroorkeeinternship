import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. Reconstruct our clean pipeline DataFrame
df = sns.load_dataset('titanic')

# Fill missing records
df['age'] = df['age'].fillna(df['age'].median())
df['fare'] = df['fare'].fillna(df['fare'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# Encode Categorical
le = LabelEncoder()
df['sex_encoded'] = le.fit_transform(df['sex'])
df['embarked_encoded'] = le.fit_transform(df['embarked'])

# Scale Numerical
scaler = StandardScaler()
df[['age_scaled', 'fare_scaled']] = scaler.fit_transform(df[['age', 'fare']])

# 2. Define Features (X) and Target (y)
# We select our processed numerical columns as predictors
feature_cols = ['pclass', 'sex_encoded', 'embarked_encoded', 'age_scaled', 'fare_scaled']
X = df[feature_cols]
y = df['survived']

# 3. Perform the 80/20 Train/Test Split
# test_size=0.20 sets the test pool to exactly 20%
# random_state ensures reproducibility so your split matches this output exactly
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 4. Verify Shapes
print("--- Full Dataset Shape ---")
print(f"Total Features (X): {X.shape}")
print(f"Total Target   (y): {y.shape}")

print("\n--- Split Shapes (80/20 Partition) ---")
print(f"X_train Shape: {X_train.shape} (80% of rows)")
print(f"X_test Shape : {X_test.shape} (20% of rows)")
print(f"y_train Shape: {y_train.shape}")
