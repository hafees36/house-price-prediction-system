import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("dataset/Housing.csv")

# ==========================
# Data Preprocessing
# ==========================

binary_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

for col in binary_columns:
    df[col] = df[col].map({"yes": 1, "no": 0})

# One-Hot Encoding
df = pd.get_dummies(df, columns=["furnishingstatus"], drop_first=True)

# ==========================
# Split Features & Target
# ==========================

X = df.drop("price", axis=1)
y = df["price"]

print("Features Shape :", X.shape)
print("Target Shape   :", y.shape)

# ==========================
# Train-Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(f"\nTraining Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# ==========================
# Train Model
# ==========================

model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# ==========================
# Predictions
# ==========================

predictions = model.predict(X_test)

# ==========================
# Evaluation
# ==========================

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print(f"\nR2 Score : {r2:.4f}")
print(f"Mean Absolute Error : {mae:.2f}")

# ==========================
# Save Model
# ==========================

joblib.dump(model, "models/house_price_model.pkl")

print("\nModel Saved Successfully!")