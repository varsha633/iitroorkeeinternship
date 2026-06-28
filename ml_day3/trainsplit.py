from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = (iris.target == 0).astype(int)   # Setosa vs Non-Setosa

# Different split ratios
splits = [0.2, 0.3, 0.4]

for test_size in splits:
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print(f"Test Size = {test_size}")
    print(f"Accuracy = {accuracy:.4f}")
    print("-" * 30)
