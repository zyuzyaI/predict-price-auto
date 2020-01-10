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

def get_predict_price(year,car_mileage,power,brand,model_,body,fuel,transmission):    
    try:
      brand_index = __data_columns.index(brand.lower())
    except IndexError :
      brand_index = 0
    try:
      model_index = __data_columns.index(model_.lower())
    except IndexError :
      model_index = 0
    try:
      body_index = __data_columns.index(body.lower())
    except IndexError :
      body_index = 0
    try:
      fuel_index = __data_columns.index(fuel.lower())
    except IndexError :
      fuel_index = 0
    try:
      transmission_index = __data_columns.index(transmission.lower())
    except IndexError :
      transmission_index = 0
    

    x = np.zeros(len(__data_columns), dtype='float32')
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
    pred = model.predict([x])[0]
    return pred

