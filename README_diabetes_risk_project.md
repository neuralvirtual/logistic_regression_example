# Diabetes Risk Prediction Using Logistic Regression

This project demonstrates a simple **Logistic Regression** model to predict the risk of diabetes based on basic health indicators: age, Body Mass Index (BMI), and blood pressure.

## Project Overview

- We use a small synthetic dataset with sample records containing age, BMI, and blood pressure.
- The target is binary:
  - `1` indicates the person is at risk of diabetes.
  - `0` indicates no risk.
- The logistic regression model is trained on this data.
- The user can input their own health data via the command line to get a prediction:
  - The model returns the probability of diabetes risk.
  - It classifies the user as "at risk" or "not at risk" based on a 0.5 probability threshold.

## Requirements

- Python 3.x  
- numpy  
- scikit-learn  

Install dependencies with:

```bash
pip install numpy scikit-learn
```

## How to Run

1. Run the Python script or notebook.
2. When prompted, enter your age, BMI, and blood pressure.
3. View the predicted probability and risk classification.

Example:

```
Enter your age: 45
Enter your BMI: 28.5
Enter your blood pressure: 92
```

Output:

```
Risk probability of diabetes: 0.85
Based on the data, you are at risk of diabetes.
```

## Explanation

- Logistic Regression is a classification algorithm used here to predict a binary outcome.
- The model calculates the probability that a user belongs to the "at risk" class.
- Based on the calculated probability, the user is classified accordingly.

## Notes

- This is a **simple example** with a small synthetic dataset for educational purposes.
- For real-world applications, use larger, more representative datasets and more robust validation.

---

Feel free to modify and expand this project for more features and data!
