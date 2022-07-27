import unittest
import flask_testing
from app import app

class TestMain(flask_testing.TestCase):
    app.config["TESTING"] = True

    def create_app(self):
        return app

class TestApp(TestMain):
    def test_get_recommendations(self):
        response = self.client.get("/getRecommendations/6")
        self.assertEqual(response.json, {
            "code": 200,
            "results": [
                [
                    "GIG",
                    "Rio De Janeiro",
                    "Brazil"
                ],
                [
                    "IAH",
                    "Houston",
                    "United States"
                ],
                [
                    "TPA",
                    "Tampa",
                    "United States"
                ],
                [
                    "KIX",
                    "Osaka",
                    "Japan"
                ],
                [
                    "LAX",
                    "Los Angeles",
                    "United States"
                ],
                [
                    "DEN",
                    "Denver",
                    "United States"
                ],
                [
                    "MIA",
                    "Miami",
                    "United States"
                ],
                [
                    "HKG",
                    "Hong Kong",
                    "China"
                ],
                [
                    "SIN",
                    "Singapore",
                    "Singapore"
                ],
                [
                    "LHR",
                    "London",
                    "United Kingdom"
                ]
            ]
        })

    def test_get_customer_churn(self):
        response = self.client.get("/getCustomerChurn?ticketCount=52.000000&flightPriceGo=45139.750000&flightPriceReturn=44700.990000&flightDistance=22195.940000&travelDays=122.000000&hotelDays=33.000000&hotelPrice=6589.800000&combo=15.000000&age=57.000000&comboFrequency=0.288462&hotelStayDayAvg=2.200000")
        self.assertEqual(response.json, {
            "code": 200,
            "results": 0
        })

    def test_get_air_passenger_forecast(self):
        response = self.client.get("/getAirPassengerForecast/12")
        self.assertEqual(response.json, {
            "code": 200,
            "predictions": [
                423.80023193359375,
                408.63861083984375,
                462.3076477050781,
                416.0666809082031,
                350.91363525390625,
                326.6575927734375,
                360.26025390625,
                387.0815734863281,
                342.5498962402344,
                316.3879699707031,
                275.7266845703125,
                307.06256103515625
            ]
        })

if __name__ == "__main__":
    unittest.main()