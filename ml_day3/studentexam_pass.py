import numpy as np
from sklearn.linear_model import LogisticRegression

# Features (Hours Studied)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)

# Target (Fail=0, Pass=1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# Predict for a student who studied 5.5 hours
hours = np.array([[5.5]])

prediction = model.predict(hours)
probability = model.predict_proba(hours)

print("Prediction:", prediction[0])
print("Probability:", probability)
