#task 1 
import pandas as pd
import seaborn as sns

# 1. Load the dataset
# We use the built-in Titanic dataset from the Seaborn library
df = sns.load_dataset('titanic')

print("--- Initial Missing Values Count ---")
print(df.isnull().sum())

# 2. Fill missing values for numerical columns
# Replace missing Age values with the median age of the passengers
df['age'] = df['age'].fillna(df['age'].median())

# 3. Fill missing values for categorical columns
# Replace missing Embarked town values with the most frequent town (mode)
mode_embark_town = df['embark_town'].mode()[0]
df['embark_town'] = df['embark_town'].fillna(mode_embark_town)

# Also fill the abbreviated 'embarked' column matching the town
mode_embarked = df['embarked'].mode()[0]
df['embarked'] = df['embarked'].fillna(mode_embarked)

# 4. Handle columns with excessive missing data
# 'deck' has too many missing values; it is safer to drop it or create an 'Unknown' category
df['deck'] = df['deck'].astype(object).fillna('Unknown')

print("\n--- Missing Values Count After Imputation ---")
print(df.isnull().sum())
