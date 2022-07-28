import pickle
from flask import Flask, jsonify, request
from flask_cors import CORS
# from invokes import invoke_http
import pandas as pd
import scipy.sparse as sparse
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

# Get recommendations via Client ID
@app.route("/getRecommendations/<string:clientID>")
def get_recommendations(clientID):
    sparse_matrix = create_sparse_matrix(flight_data)
    model = custom_load_model("model_files", "ALS.pkl")
    final_df = get_model_recommendations(clientID, sparse_matrix, model, flight_data)
    return jsonify(
        {
            "code": 200,
            "results": final_df
        }
    )

# Get customer churn status
@app.route("/getCustomerChurn")
def get_customer_churn():
    model = custom_load_model("model_files", "XGBoost_churn.pkl")
    to_predict = get_and_process_args()
    prediction = int(model.predict(to_predict)[0])
    return jsonify(
        {
            "code": 200,
            "results": prediction
        }
    )

# Get air passenger forecast (by month)
@app.route("/getAirPassengerForecast/<int:periods>")
def get_air_passenger_forecast(periods):
    model = load_model("model_files/lstm.h5")
    predictions = []
    x_input = np.array([[count] for count in passengers["#Passengers"].iloc[-6:]])
    for _ in range(periods):
        temp = x_input.reshape((1, 6, 1))
        yhat = model.predict(temp, verbose=0)[0][0]
        predictions.append(float(yhat))
        x_input = np.append(x_input[1:], [yhat])
    return jsonify(
        {
            "code": 200,
            "predictions": predictions
        }
    )
    
def create_sparse_matrix(df):
    return sparse.csr_matrix(sparse.csr_matrix((df['freq'].astype(float), (df['user_id'], df['dest_id']))))

def get_model_recommendations(clientID, sparse_matrix, model, df):
    destinations, score, clientID = [], [], int(clientID)
    indexes, scores = model.recommend(clientID, sparse_matrix[clientID])
    for i in range(len(indexes)):
        if not df.dest.loc[df.user_id == indexes[i]].empty:
            destinations.append(df.dest.loc[df.user_id == indexes[i]].iloc[0])
            # score.append(scores[i].round(3))
    recommendations = pd.DataFrame({"destination": destinations})
    final_df = pd.merge(recommendations, cities, on="destination", how="left")
    return final_df.values.tolist()

def custom_load_model(file_path, model_filename):
    return pickle.load(open(f"{file_path}/{model_filename}", "rb"))

def get_and_process_args():
    ticketCount = float(request.args.get("ticketCount"))
    flightPriceGo = float(request.args.get("flightPriceGo"))
    flightPriceReturn = float(request.args.get("flightPriceReturn"))
    flightDistance = float(request.args.get("flightDistance"))
    travelDays = float(request.args.get("travelDays"))
    hotelDays = float(request.args.get("hotelDays"))
    hotelPrice = float(request.args.get("hotelPrice"))
    combo = float(request.args.get("combo"))
    age = float(request.args.get("age"))
    comboFrequency = float(request.args.get("comboFrequency"))
    hotelStayDayAvg = float(request.args.get("hotelStayDayAvg"))
    return_df = pd.DataFrame({
        "ticketCount": [ticketCount],
        "flightPriceGo": [flightPriceGo],
        "flightPriceReturn": [flightPriceReturn],
        "flightDistance": [flightDistance],
        "travelDays": [travelDays],
        "hotelDays": [hotelDays],
        "hotelPrice": [hotelPrice],
        "combo": [combo],
        "age": [age],
        "comboFrequency": [comboFrequency],
        "hotelStayDayAvg": [hotelStayDayAvg],
    })
    return return_df

if __name__ == "__main__":
    flight_data = pd.read_csv("datasets/user_flight_data.csv")
    cities = pd.read_csv("datasets/city_codes.csv", encoding="latin-1")
    passengers = pd.read_csv("datasets/AirPassengers.csv")
    app.run(host="0.0.0.0", port=5000, debug=True)