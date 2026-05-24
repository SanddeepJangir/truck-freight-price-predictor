🚛 Truck Freight Price Predictor

A Machine Learning web application that predicts truck freight prices in real time based on route, cargo, and vehicle details.

📌 Problem Statement
In the Indian road freight industry, pricing is largely informal and inconsistent. There is no standardized system for estimating freight costs, causing financial uncertainty for both transporters and fleet owners. This project addresses the problem by developing an end-to-end ML pipeline using a Decision Tree Regressor model trained on synthetic but domain-realistic data. The solution covers data generation, preprocessing using ColumnTransformer and Pipeline, model training with 94.34% R² accuracy, and deployment via a Flask web API with an HTML frontend — providing an accessible tool for real-time freight price prediction.

⚙️ Tech Stack
LayerTechnologyLanguagePython 3.xML ModelDecision Tree RegressorLibrariesPandas, NumPy, Scikit-learnPipelineColumnTransformer + PipelineEncodingOneHotEncoder + StandardScalerBackendFlask REST APIFrontendHTML, CSS, JavaScript

📊 Model Performance
MetricValueR² Score94.34%MAE₹2,241.21RMSE₹2,932.10Dataset Size1000 rowsTrain/Test80% / 20%

📁 Project Structure
truck-freight-price-predictor/
│
├── generate_dataset.py     # Generate synthetic dataset (1000 rows)
├── train_model.py          # Preprocessing pipeline + model training + save
├── app.py                  # Flask web application (REST API)
├── truck_freight.csv       # Generated dataset
├── model.pkl               # Trained and saved ML model
├── requirements.txt        # Python dependencies
├── screenshots/            # UI screenshots
└── templates/
    └── index.html          # Frontend form UI

🔢 Input Features
FeatureTypeDescriptionExampledistance_kmNumericalRoute distance in kilometres500load_weight_tonNumericalCargo weight in tons10.5fuel_price_literNumericalDiesel price per litre (₹)90.5toll_chargesNumericalEstimated toll charges (₹)800driver_experienceNumericalDriver experience in years5num_stopsNumericalNumber of stops on route2route_typeCategoricalHighway / City / MixedHighwayvehicle_typeCategoricalSmall / Medium / LargeMediumcargo_typeCategoricalGeneral / Fragile / HazardousGeneral

🎯 Target Variable
freight_price — Estimated freight cost in Indian Rupees (₹)

🔄 ML Pipeline
Raw Data
   ↓
ColumnTransformer
   ├── Numerical Columns  → StandardScaler
   └── Categorical Columns → OneHotEncoder
   ↓
Decision Tree Regressor
   ↓
Predicted Freight Price (₹)

🚀 How to Run
Step 1 — Clone the Repository
bashgit clone https://github.com/SanddeepJangir/truck-freight-price-predictor.git
cd truck-freight-price-predictor
Step 2 — Install Dependencies
bashpip install -r requirements.txt
Step 3 — Generate Dataset
bashpython generate_dataset.py
Step 4 — Train Model
bashpython train_model.py
Step 5 — Run Flask App
bashpython app.py
Step 6 — Open in Browser
http://127.0.0.1:5000

💡 Project Highlights

Built complete end-to-end ML pipeline from data generation to deployment
Used ColumnTransformer to handle mixed numerical and categorical features
Achieved 94.34% R² accuracy using Decision Tree Regressor
Deployed as REST API using Flask with clean HTML/CSS frontend
Domain knowledge applied from logistics industry experience


📸 Screenshots

Add screenshots here after running the project locally


👨‍💻 Author
Sandeep Jangir

🔗 GitHub: github.com/SanddeepJangir
💼 LinkedIn: linkedin.com/in/sanddeep-jangir11
📧 Email: sjangir1208@gmail.com
📍 Jaipur, Rajasthan, India


📄 License
This project is open source and available under the MIT License.