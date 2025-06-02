import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import joblib

# Load the CSV and select only the specified columns
df = pd.read_csv('csv/StudentsPerformance.csv')[[
    "gender",
    "race/ethnicity",
    "lunch",
    "test preparation course",
    "math score",
    "reading score",
    "writing score"
]]

# Features and targets
X = df[["gender", "race/ethnicity", "lunch", "test preparation course"]]
y = df[["math score", "reading score", "writing score"]]

# Preprocessing: One-hot encode all categorical columns
categorical_columns = X.columns.tolist()
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)
])

# Models to train
models = {
    "student_rf.pkl": RandomForestRegressor(n_estimators=100, random_state=42),
    "student_lr.pkl": LinearRegression(),
    "student_gb.pkl": GradientBoostingRegressor(n_estimators=100, random_state=42),
}

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and save each model
for filename, regressor in models.items():
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", regressor)
    ])
    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, filename)
    print(f"✅ Model saved: {filename}")

