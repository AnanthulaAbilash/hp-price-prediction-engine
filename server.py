from flask import Flask, request, jsonify
import util
from waitress import serve
import os

app = Flask(__name__)

@app.route('/get_locations', methods = ['GET'])
def get_locations():
    response = jsonify({
        'locations': util.get_house_locations()
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response



@app.route('/predict_house_price', methods = ['GET', 'POST'])
def predict_house_price():
    
    total_sft = float(request.form['total_sft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    
    
    response = jsonify({
        'housePrice_estimate': util.predict_hprice(location, total_sft, balcony, bath, bhk )
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    """ print("response is......", util.predict_hprice(location, total_sft, balcony, bath, bhk )) """
    return response


PORT = os.environ.get('PORT', 5000)

if __name__ == '__main__':
    print('Server ready..')
    util.load_artifacts()
    """ app.run(port=5000) """
    serve(app, port=PORT)