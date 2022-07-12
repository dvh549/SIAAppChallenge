from flask import Flask, jsonify
from flask_cors import CORS
# from invokes import invoke_http
import pandas as pd
import implicit
import scipy.sparse as sparse

app = Flask(__name__)
CORS(app)

# Get recommendations via Client ID
@app.route("/getRecommendations/<string:clientID>")
def get_recommendations(clientID):
    sparse_matrix = create_sparse_matrix(flight_data)
    model = fit_als_model(sparse_matrix)
    final_df = get_model_recommendations(clientID, sparse_matrix, model, flight_data)
    return jsonify(
        {
            "code": 200,
            "results": final_df
        }
    )

def create_sparse_matrix(df):
    return sparse.csr_matrix(sparse.csr_matrix((df['freq'].astype(float), (df['user_id'], df['dest_id']))))

def fit_als_model(sparse_matrix):
    model = implicit.als.AlternatingLeastSquares(factors = 20, regularization = 0.1, iterations = 20)
    alpha_val = 15
    data_conf = (sparse_matrix * alpha_val).astype('double')
    model.fit(data_conf)
    return model

def get_model_recommendations(clientID, sparse_matrix, model, df):
    destinations, score, clientID = [], [], int(clientID)
    indexes, scores = model.recommend(clientID, sparse_matrix[clientID])
    for i in range(len(indexes)):
        if not df.dest.loc[df.user_id == indexes[i]].empty:
            destinations.append(df.dest.loc[df.user_id == indexes[i]].iloc[0])
            score.append(scores[i].round(3))
    recommendations = pd.DataFrame({"destination": destinations})
    final_df = pd.merge(recommendations, cities, on="destination", how="left")
    return final_df.values.tolist()

if __name__ == "__main__":
    flight_data = pd.read_csv("../ml_models/datasets/recommender/user_flight_data.csv")
    cities = pd.read_csv("../ml_models/datasets/recommender/city_codes.csv", encoding="latin-1")
    app.run(host="0.0.0.0", port=5000, debug=True)