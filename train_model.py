"""Train a linear-regression model on mtcars and save it as model.pkl."""
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# path to run locally
#BASE = Path.cwd() # current working dir (not __file__)
#DATA = BASE /"mtcars.csv"

# Paths
BASE = Path(__file__).resolve().parent          # .../app
DATA = BASE.parent / "mtcars.csv"      # .../data/mtcars.csv
MODEL_OUT = BASE / "model.pkl"                  # model output

print("🔄  Loading data …")
df = pd.read_csv(DATA)

# X = all columns except the response (mpg) and the car name
X = df.drop(columns=["mpg", "model"])
y = df["mpg"]

print("🔧  Fitting linear model …")
model = LinearRegression().fit(X, y)

# Save the fitted model to disk
joblib.dump(model, MODEL_OUT, compress=3)
print(f"✅  Model saved to {MODEL_OUT}")
