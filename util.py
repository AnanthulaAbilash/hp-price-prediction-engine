import pickle
import json
import numpy as np


house_locations = None
feature_columns = None
model = None

def load_artifacts():
    global house_locations
    global model
    global feature_columns
    
    if model is None:
        with open('./artifacts/ML_house_price_model.pickle', 'rb') as f:
            model = pickle.load(f)
    print('model is loaded')

    with open('./artifacts/house_features.json', 'r') as f:
        feature_columns = json.load(f)['features']
        house_locations = feature_columns[4:]
        

def predict_hprice(location, total_sqft, balcony, bath, bhk_no):
       #loc_index = np.where(house_features.columns == location)[0][0]
       global feature_columns
       global model
       
       try:       
            loc_index = feature_columns.index(location.lower())
       except: 
           loc_index = -1
       print('loc_index', loc_index)
       new_features = np.zeros(len(feature_columns))
       new_features[feature_columns.index('total_sqft')] = total_sqft
       new_features[feature_columns.index('bath')] = bath
       new_features[feature_columns.index('balcony')] = balcony
       new_features[feature_columns.index('bhk_no')] = bhk_no
       new_features[loc_index] = 1
       
       if loc_index>=0 and total_sqft>=0 and balcony>=0 and bath>=0 and bhk_no>=0: 
              return np.round(model.predict([new_features])[0], 3)
       else: return None 
       #return np.round(model.predict([new_features])[0], 3)

def get_house_locations():
    return house_locations

def get_house_features():
    return feature_columns

if __name__ == '__main__':
    load_artifacts()
    #print(predict_hprice('1st block jayanagar',1800, 2, 2, 2))
    #print(get_house_features())

