from flask import Flask, jsonify
from sklearn.linear_model import LinearRegression
import pandas as pd
app = Flask(__name__)

input_data = pd.DataFrame({'x': range(20),
                           'y': [  0.32797344,   0.24651086,   2.48196793,   2.15542269,
                                   3.85308687,   5.34399642,   6.20893099,   5.67906586,
                                   9.18233268,   9.44169552,  10.33510592,  11.75765219,
                                   12.46384419,  12.48009362,  14.39153645,  15.12273801,
                                   16.24443402,  16.54217248,  17.49921914,  18.613513  ]})

@app.route("/data.json")
def get_json_data():
    return jsonify(input_data.to_dict())

@app.route("/predict.json")
def predict():
    model = LinearRegression().fit(input_data[['x']], input_data['y'])
    future_vals = [[20], [21], [22]]
    return jsonify(list(model.predict(future_vals)))
    

if __name__ == "__main__":
    app.run()
