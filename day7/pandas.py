import pandas as pd

# Load CSV
df = pd.read_csv("students.csv")

print("Data:")
print(df)

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with column mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter Handling Missing Values:")
print(df)
