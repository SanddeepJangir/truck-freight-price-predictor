from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form

        input_data = pd.DataFrame([{
            'distance_km'      : float(data['distance_km']),
            'load_weight_ton'  : float(data['load_weight_ton']),
            'fuel_price_liter' : float(data['fuel_price_liter']),
            'route_type'       : data['route_type'],
            'vehicle_type'     : data['vehicle_type'],
            'toll_charges'     : float(data['toll_charges']),
            'driver_experience': float(data['driver_experience']),
            'cargo_type'       : data['cargo_type'],
            'num_stops'        : float(data['num_stops']),
        }])

        prediction = model.predict(input_data)[0]

        return jsonify({
            'status' : 'success',
            'freight_price': round(prediction, 2)
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
