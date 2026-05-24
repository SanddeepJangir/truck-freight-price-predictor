# 🚛 Truck Freight Price Predictor

A Machine Learning web application that predicts truck freight prices based on route, cargo, and vehicle details.

---

## 📁 Project Structure

```
truck_freight_predictor/
│
├── generate_dataset.py     # Generate synthetic dataset (1000 rows)
├── train_model.py          # Preprocess data, train model, save model.pkl
├── app.py                  # Flask web application (backend API)
├── truck_freight.csv       # Generated dataset
├── model.pkl               # Trained Decision Tree Regressor model
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # Frontend UI
```

---

## ⚙️ Tech Stack

| Layer        | Technology                        |
|--------------|-----------------------------------|
| Language     | Python 3.x                        |
| ML Model     | Decision Tree Regressor           |
| Libraries    | Pandas, NumPy, Scikit-learn       |
| Pipeline     | ColumnTransformer + Pipeline      |
| Backend      | Flask                             |
| Frontend     | HTML, CSS, JavaScript             |
| Database     | MySQL (optional integration)      |

---

## 📊 Model Performance

| Metric | Value      |
|--------|------------|
| R² Score | 94.34%   |
| MAE    | ₹2,241.21  |
| RMSE   | ₹2,932.10  |

---

## 🚀 How to Run

### Step 1 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Generate Dataset
```bash
python generate_dataset.py
```

### Step 3 — Train Model
```bash
python train_model.py
```

### Step 4 — Run Flask App
```bash
python app.py
```

### Step 5 — Open in Browser
```
http://127.0.0.1:5000
```

---

## 🔢 Input Features

| Feature            | Description                        | Example     |
|--------------------|------------------------------------|-------------|
| distance_km        | Route distance in km               | 500         |
| load_weight_ton    | Cargo weight in tons               | 10.5        |
| fuel_price_liter   | Diesel price per litre (₹)        | 90.5        |
| route_type         | Highway / City / Mixed             | Highway     |
| vehicle_type       | Small / Medium / Large             | Medium      |
| toll_charges       | Estimated toll charges (₹)        | 800         |
| driver_experience  | Driver experience in years         | 5           |
| cargo_type         | General / Fragile / Hazardous      | General     |
| num_stops          | Number of stops on route           | 2           |

---

## 🎯 Target Variable

- **freight_price** — Estimated freight cost in Indian Rupees (₹)

---

## 👨‍💻 Author

**Sandeep Jangir**
- GitHub: [github.com/SanddeepJangir](https://github.com/SanddeepJangir)
- LinkedIn: [linkedin.com/in/sanddeep-jangir11](https://linkedin.com/in/sanddeep-jangir11)
- Email: sjangir1208@gmail.com
