# 🚛 Truck Freight Price Predictor

A Machine Learning web application that predicts truck freight prices in real time based on route, cargo, and vehicle details.

---

# 📌 Problem Statement

In the Indian road freight industry, pricing is largely informal and inconsistent. There is no standardized system for estimating freight costs, causing financial uncertainty for both transporters and fleet owners.

This project solves that problem by building a complete end-to-end Machine Learning pipeline using a Decision Tree Regressor trained on domain-realistic synthetic data.

The solution covers:
- Data generation
- Data preprocessing
- Feature engineering
- Model training
- Flask REST API deployment
- Frontend integration using HTML/CSS/JavaScript

---

# 🛠 Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.x |
| ML Model | Decision Tree Regressor |
| Libraries | Pandas, NumPy, Scikit-learn |
| Pipeline | ColumnTransformer + Pipeline |
| Backend | Flask REST API |
| Frontend | HTML, CSS, JavaScript |

---

# 📊 Model Performance

| Metric | Value |
|---|---|
| R² Score | 94.34% |
| MAE | ₹2,241.21 |
| RMSE | ₹2,932.10 |
| Dataset Size | 1000 Rows |
| Train/Test Split | 80/20 |

---

# 📂 Project Structure

```bash
truck-freight-price-predictor/
│
├── generate_dataset.py
├── train_model.py
├── app.py
├── model.pkl
├── truck_freight.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
    ├── homepage-ui.png
    └── prediction-result.png
🧠 Input Features
Feature	Type	Description
distance_km	Numerical	Route distance in kilometers
load_weight_ton	Numerical	Cargo weight in tons
fuel_price_liter	Numerical	Diesel price per liter
toll_charges	Numerical	Estimated toll charges
driver_experience_years	Numerical	Driver experience
num_stops	Numerical	Number of stops
route_type	Categorical	Highway / City / Mixed
vehicle_type	Categorical	Small / Medium / Large
cargo_type	Categorical	General / Fragile / Hazardous
🎯 Target Variable
freight_price

Estimated freight cost in Indian Rupees (₹)

⚙️ ML Pipeline
Raw Data
   │
   ├── Numerical Columns
   │      └── StandardScaler
   │
   ├── Categorical Columns
   │      └── OneHotEncoder
   │
   └── ColumnTransformer
            │
            └── Decision Tree Regressor
                     │
                     └── Predicted Freight Price
🚀 How to Run
1️⃣ Clone Repository
git clone https://github.com/SandeepJangir/truck-freight-price-predictor.git

cd truck-freight-price-predictor
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Generate Dataset
python generate_dataset.py
4️⃣ Train Model
python train_model.py
5️⃣ Run Flask App
python app.py
6️⃣ Open in Browser
http://127.0.0.1:5000
📸 Screenshots
🏠 Main Prediction Dashboard
<img width="100%" alt="Truck Freight Price Predictor UI" src="screenshots/homepage-ui.png">
Features
Clean responsive UI
Freight estimation form
Vehicle and cargo selection
Route configuration
Real-time prediction system
📊 Prediction Result Example
<img width="100%" alt="Freight Prediction Result" src="screenshots/prediction-result.png">
Example Output

The system predicts freight price dynamically based on:

Distance
Load weight
Fuel price
Toll charges
Vehicle type
Cargo type
Route type
Driver experience
✨ Project Highlights
Complete end-to-end ML pipeline
Real-world logistics pricing use case
Flask REST API integration
Feature engineering using ColumnTransformer
Clean frontend UI
High prediction accuracy
Synthetic domain-realistic dataset generation
👨‍💻 Author

Sandeep Jangir

GitHub: https://github.com/SandeepJangir
LinkedIn: https://linkedin.com/in/sanddeep-jangir11
Email: sjangir1208@gmail.com
Location: Jaipur, Rajasthan, India
📜 License

This project is open source and available under the MIT License