from flask import Flask, request, jsonify
import pandas as pd
import util

app = Flask(__name__)

@app.route('/get_brand_names', methods=['GET'])
def get_location_names():
	response = jsonify({
		'brand': util.get_brand_names()
	})
	response.headers.add('Access-Control-Allow-Origin', '*')

	return response

@app.route('/get_model_names', methods=['GET'])
def get_model_names():
	response = jsonify({
		'model': util.get_model_names()
	})
	response.headers.add('Access-Control-Allow-Origin', '*')

	return response

@app.route('/get_body_names', methods=['GET'])
def get_body_names():
	response = jsonify({
		'body': util.get_body_names()
	})
	response.headers.add('Access-Control-Allow-Origin', '*')

	return response

@app.route('/get_fuel_names', methods=['GET'])
def get_fuel_names():
	response = jsonify({
		'fuel': util.get_fuel_names()
	})
	response.headers.add('Access-Control-Allow-Origin', '*')

	return response

@app.route('/get_transmission_names', methods=['GET'])
def get_transmission_names():
	response = jsonify({
		'transmission': util.get_transmission_names()
	})
	response.headers.add('Access-Control-Allow-Origin', '*')

	return response

@app.route('/predict_price', methods=['GET', 'POST'])
def predict_price():
	year = float(request.form['year'])
	car_mileage = float(request.form['car_mileage'])
	power = float(request.form['power'])
	brand = request.form['brand']	
	model_ = request.form['model_']
	body = request.form['body']
	fuel = request.form['fuel']
	transmission = request.form['transmission']

	response = jsonify({
		'estimated_price': util.get_predict_price(year, car_mileage, power, brand, model_, body, fuel, transmission)
	})
	response.headers.add('Access-Control-Allow-Origin', '*')

	return response

if __name__ == "__main__":
	print("Starting Python Flask Server For Home Price Prediction...")
	util.load_saved_artifacts()
	app.run(debug=True)