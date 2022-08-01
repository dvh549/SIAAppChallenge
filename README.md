# SIAAppChallenge

## How to run backend server

1. Install python (latest version) and then navigate to the "backend" folder. 
2. Open a new terminal.
3. Run command "pip install -r requirements.txt" to install the necessary libraries.
4. Run command "python app.py".
5. Call endpoints: <br/>
a. Call endpoint "/getRecommendations/6" to get destination recommendations (where 6 is the clientID and it ranges from 1-98). <br/>
b. Call endpoint "/getCustomerChurn" to get churn status of a customer (if 0 = no churn, 1 = churn). <br/>
c. Call endpoint "/getAirPassengerForecast/3" to get monthly airline passengers predictions (where 3 is the number of months to forecast for).

## How to run frontend server
1. Open terminal under "SIAAppChallenge/frontend" directory.
2. Run "npm install".
3. Once done, run "nodemon start".

## Running both the frontend and backend servers (Docker Compose)
1. [Get & Install Docker] (https://docs.docker.com/get-docker/)
2. Run command "docker-compose up -d" to start and run servers.
3. Run command "docker-compose down" to stop and remove servers.
