import pickle
import json
import numpy as np 

__year = None
__car_mileage = None
__power = None
__brand = None
__model_ = None
__body = None
__fuel = None
__transmission = None

__model = None

def get_predict_price(year,car_mileage,power,brand,model_,body,fuel,transmission):    
	try:
	  brand_index = __data_column.index(brand.lower())
	except IndexError :
	  brand_index = 0
	try:
	  model_index = __data_column.index(model_.lower())
	except IndexError :
	  model_index = 0
	try:
	  body_index = __data_column.index(body.lower())
	except IndexError :
	  body_index = 0
	try:
	  fuel_index = __data_column.index(fuel.lower())
	except IndexError :
	  fuel_index = 0
	try:
	  transmission_index = __data_column.index(transmission.lower())
	except IndexError :
	  transmission_index = 0
	

	x = np.zeros(len(__data_column), dtype='float32')
	x[0] = year
	x[1] = car_mileage
	x[2] = power
	if brand_index > 0:
		x[brand_index] = 1
	if model_index > 0:
		x[model_index] = 1
	if body_index > 0:
		x[body_index] = 1
	if fuel_index > 0:
		x[fuel_index] = 1
	if transmission_index > 0:
		x[transmission_index] = 1
	pred = __model.predict([x])[0]
	return pred


def load_saved_artifacts():
	print("loading saved artifacts...start")
	global  __data_column

	global __brand
	global __model_ 
	global __body
	global __fuel 
	global __transmission 

	with open("./artifacts/columns.json", "r") as f:
		__data_column = json.load(f)['data_columns']
		__brand = __data_column[3:41]  # first 3 columns are year, car_mileage, power
		__model_ = __data_column[42:908]
		__body = __data_column[908:919]
		__fuel = __data_column[919:921]
		__transmission = __data_column[921:]
		
	global __model
	if __model is None:
		with open('./artifacts/vehicle_prices_model.pickle', 'rb') as f:
			__model = pickle.load(f)
	print("loading saved artifacts...done")

def get_brand_names():
	return __brand

def get_model_names():
    return __model_

def get_body_names():
	return __body

def get_fuel_names():
	return __fuel

def get_transmission_names():
	return __transmission

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
	load_saved_artifacts()
	print(get_transmission_names())
	# print(get_predict_price(2002, 297, 1.8, 'skoda', 'octavia', 'liftback', 'gas', 'manual'))
	# print(get_predict_price(2008, 189, 2.5, 'volkswagen', 't5', 'minivan', 'diesel', 'manual'))
	