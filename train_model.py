import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ── 1. Load Data ──────────────────────────────────────────
df = pd.read_csv('/home/claude/freight_project/truck_freight.csv')
print("=== Dataset Info ===")
print(f"Shape: {df.shape}")
print(df.dtypes)

# ── 2. Features & Target ──────────────────────────────────
X = df.drop('freight_price', axis=1)
y = df['freight_price']

numerical_cols   = ['distance_km', 'load_weight_ton', 'fuel_price_liter',
                    'toll_charges', 'driver_experience', 'num_stops']
categorical_cols = ['route_type', 'vehicle_type', 'cargo_type']

# ── 3. Train-Test Split ───────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTrain size: {X_train.shape[0]} | Test size: {X_test.shape[0]}")

# ── 4. Preprocessing Pipeline ─────────────────────────────
numerical_transformer   = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

preprocessor = ColumnTransformer(transformers=[
    ('num', numerical_transformer, numerical_cols),
    ('cat', categorical_transformer, categorical_cols)
])

# ── 5. Full Pipeline with Model ───────────────────────────
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor',    DecisionTreeRegressor(
        max_depth=8,
        min_samples_split=10,
        min_samples_leaf=5,
        random_state=42
    ))
])

# ── 6. Train ──────────────────────────────────────────────
model_pipeline.fit(X_train, y_train)
print("\n=== Model Trained Successfully ===")

# ── 7. Evaluate ───────────────────────────────────────────
y_pred = model_pipeline.predict(X_test)

mae  = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2   = r2_score(y_test, y_pred)

print("\n=== Model Performance ===")
print(f"MAE  (Mean Absolute Error) : ₹{mae:,.2f}")
print(f"RMSE (Root Mean Sq Error)  : ₹{rmse:,.2f}")
print(f"R²   Score                 : {r2:.4f}  ({r2*100:.2f}%)")

# ── 8. Sample Predictions ─────────────────────────────────
print("\n=== Sample Predictions vs Actual ===")
sample = pd.DataFrame({
    'Actual'   : y_test.values[:5],
    'Predicted': np.round(y_pred[:5], 2)
})
print(sample.to_string(index=False))

# ── 9. Save Model ─────────────────────────────────────────
with open('/home/claude/freight_project/model.pkl', 'wb') as f:
    pickle.dump(model_pipeline, f)

print("\n✅ Model saved as model.pkl")
