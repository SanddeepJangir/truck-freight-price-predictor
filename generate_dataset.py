import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

# --- Features ---
distance_km        = np.random.randint(100, 2001, n)
load_weight_ton    = np.round(np.random.uniform(1, 30, n), 2)
fuel_price_liter   = np.round(np.random.uniform(85, 95, n), 2)
route_type         = np.random.choice(['Highway', 'City', 'Mixed'], n, p=[0.5, 0.2, 0.3])
vehicle_type       = np.random.choice(['Small', 'Medium', 'Large'], n, p=[0.3, 0.4, 0.3])
toll_charges       = np.random.randint(100, 3001, n)
driver_experience  = np.random.randint(1, 21, n)   # years
cargo_type         = np.random.choice(['General', 'Fragile', 'Hazardous'], n, p=[0.6, 0.25, 0.15])
num_stops          = np.random.randint(0, 6, n)

# --- Route type multiplier ---
route_map  = {'Highway': 1.0, 'Mixed': 1.15, 'City': 1.30}
route_mult = np.array([route_map[r] for r in route_type])

# --- Vehicle base rate per km per ton ---
vehicle_map  = {'Small': 8, 'Medium': 12, 'Large': 16}
vehicle_rate = np.array([vehicle_map[v] for v in vehicle_type])

# --- Cargo surcharge ---
cargo_map      = {'General': 0, 'Fragile': 500, 'Hazardous': 1200}
cargo_surcharge = np.array([cargo_map[c] for c in cargo_type])

# --- Freight price formula (realistic) ---
base_cost     = distance_km * load_weight_ton * vehicle_rate * 0.05
fuel_cost     = distance_km * fuel_price_liter * 0.08
stop_cost     = num_stops * 300
noise         = np.random.normal(0, 500, n)

freight_price = (
    base_cost * route_mult
    + fuel_cost
    + toll_charges
    + stop_cost
    + cargo_surcharge
    + noise
)
freight_price = np.round(np.clip(freight_price, 500, None), 2)

# --- Build DataFrame ---
df = pd.DataFrame({
    'distance_km'       : distance_km,
    'load_weight_ton'   : load_weight_ton,
    'fuel_price_liter'  : fuel_price_liter,
    'route_type'        : route_type,
    'vehicle_type'      : vehicle_type,
    'toll_charges'      : toll_charges,
    'driver_experience' : driver_experience,
    'cargo_type'        : cargo_type,
    'num_stops'         : num_stops,
    'freight_price'     : freight_price
})

df.to_csv('/home/freight_project/truck_freight.csv', index=False)
print("Dataset saved: truck_freight.csv")
print(f"Shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic Stats:")
print(df.describe())
print("\nNull values:")
print(df.isnull().sum())
