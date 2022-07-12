# SIAAppChallenge

## How to run backend server

1. Install python (latest version) and then navigate to the "backend" folder. 
2. Open a new terminal.
3. Run command "pip install -r requirements.txt" to install the necessary libraries.
4. Run command "python app.py".
5. Call endpoint "localhost:5000/getRecommendations/6" to get destination recommendations (where 6 is the clientID and it ranges from 1-98).
6. Call endpoint "localhost:5000/getCustomerChurn" to get churn status of a customer.

## How to run frontend server
1. open terminal under "SIAAppChallenge/frontend" directory
2. run "npm install"
3. once done, run "nodemon start"