"""Train a linear-regression model on mtcars."""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("mtcars.csv")

# X = all columns except the response (mpg) and the car name
X = df.drop(columns=["mpg", "model"])
y = df["mpg"]

print("🔧  Fitting linear model …")
model = LinearRegression().fit(X, y)

# Prediction
def predict(dict_values, features = X, model = model):
    x = np.array([float(dict_values[col]) for col in features])
    x = x.reshape(1, -1)
    y_pred = model.predict(x)[0]
    return y_pred
