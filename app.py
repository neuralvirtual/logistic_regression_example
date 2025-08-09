from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

X = np.array([
    [25, 22, 80],
    [45, 28, 90],
    [35, 30, 85],
    [50, 32, 95],
    [23, 24, 70],
    [40, 27, 88]
])

y = np.array([0, 1, 1, 1, 0, 1])


model = LogisticRegression()
model.fit(X, y)

age = int(input("Enter your age: "))
bmi = float(input("Enter your BMI: "))
bp = int(input("Enter your blood pressure: "))

user_data = np.array([[age, bmi, bp]])
risk_prob = model.predict_proba(user_data)[0, 1]
risk_class = model.predict(user_data)[0]

print(f"\nRisk probability of diabetes: {risk_prob:.2f}")
if risk_class == 1:
    print("Based on the data, you are at risk of diabetes.")
else:
    print("Based on the data, you are not at risk of diabetes.")