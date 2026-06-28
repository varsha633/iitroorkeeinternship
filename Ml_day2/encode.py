#task 2 
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# 1. Load and clean the dataset (from previous step)
df = sns.load_dataset('titanic')
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

print("--- Data Before Label Encoding ---")
print(df[['sex', 'embarked']].head())

# 2. Initialize the LabelEncoder
le_sex = LabelEncoder()
le_embarked = LabelEncoder()

# 3. Fit and transform the columns
df['sex_encoded'] = le_sex.fit_transform(df['sex'])
df['embarked_encoded'] = le_embarked.fit_transform(df['embarked'])

print("\n--- Data After Label Encoding ---")
print(df[['sex', 'sex_encoded', 'embarked', 'embarked_encoded']].head())

# 4. View the class mapping
print("\n--- Encoder Mappings ---")
print("Sex mapping:", dict(zip(le_sex.classes_, le_sex.transform(le_sex.classes_))))
print("Embarked mapping:", dict(zip(le_embarked.classes_, le_embarked.transform(le_embarked.classes_))))
