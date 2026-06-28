import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# 1. Simulate dataset loading
# In a real environment, you would use: df = pd.read_csv('train.csv')
# Here we generate a mock subset representing the House Prices structure
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

# Separate Target (y) and Features (X)
X = df.drop(columns=['SalePrice'])
y = df['SalePrice']

# 2. Separate column names by structural data types
numerical_cols = ['LotFrontage', 'GrLivArea', 'GarageCars']
categorical_cols = ['MSZoning', 'KitchenQual']

# 3. Design the Numerical Transformer Pipeline
numerical_transformer = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='median')),  # Handle missing values
        ('scaler', StandardScaler()),  # Feature Scaling
    ]
)

# 4. Design the Categorical Transformer Pipeline
categorical_transformer = Pipeline(
    steps=[
        (
            'imputer',
            SimpleImputer(strategy='most_frequent'),
        ),  # Mode Imputation
        (
            'encoder',
            OneHotEncoder(handle_unknown='ignore', sparse_output=False),
        ),  # Encode
    ]
)

# 5. Combine transformers into a unified ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols),
    ]
)

# 6. Split the data before processing to prevent data leakage
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# 7. Execute the entire pipeline on the feature arrays
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# 8. Retrieve updated feature headers for validation mapping
encoded_cat_cols = (
    preprocessor.named_transformers_['cat']
    .named_steps['encoder']
    .get_feature_names_out(categorical_cols)
)
all_feature_names = list(numerical_cols) + list(encoded_cat_cols)

# Convert processed matrix back to DataFrame for clean visualization
X_train_final = pd.DataFrame(X_train_processed, columns=all_feature_names)

print("--- Original Sample Raw Data ---")
print(X_train.head(3))
print("\n--- Pipeline Preprocessed Data Shape ---")
print(f"Processed Train Shape: {X_train_final.shape}")
print("\n--- Pipeline Preprocessed Sample Output ---")
print(X_train_final.head(3).round(3))
