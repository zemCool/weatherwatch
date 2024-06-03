# WeatherWatch

WeatherWatch is a weather forecasting application that provides real-time weather data for various locations. It offers an easy-to-use API to get weather information, including temperature, humidity, and other atmospheric conditions.

## Features

- Real-time weather data
- Multiple location support
- Easy-to-use API
- Accurate weather forecasting

## Installation

To install and set up the project, follow these steps:

## Clone the repository

```bash
git clone https://github.com/zemCool/weatherwatch.git
cd weatherwatch
```
## Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
## Install dependencies
```bash
pip install -r requirements.txt
```
## Set up environment variables
Create a .env file in the root directory and add the necessary environment variables:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
WEATHER_API_KEY=your_weather_api_key
```
## Run migrations
```bash

python manage.py migrate
```
## Collect static files
```bash

python manage.py collectstatic
```
## Run the development server
```bash

python manage.py runserver
```
## API Usage
### Get Current Weather
- Endpoint: /api/weather/current/

Method: GET

Parameters:

- location (required): The name of the location for which you want the weather data.
- Example Request:

```bash

curl -X GET "http://localhost:8000/api/weather/current/?location=London"
```
Example Response:

```json

{
  "location": "London",
  "temperature": "15°C",
  "humidity": "77%",
  "condition": "Cloudy"
}
```
### Get Weather Forecast
- Endpoint: /api/weather/forecast/

Method: GET

Parameters:

- location (required): The name of the location for which you want the weather forecast.
- days (optional): Number of days for the forecast (default is 7).
Example Request:

```bash

curl -X GET "http://localhost:8000/api/weather/forecast/?location=London&days=5"
```
Example Response:

```json

{
  "location": "London",
  "forecast": [
    {
      "date": "2024-06-01",
      "temperature": "16°C",
      "condition": "Partly Cloudy"
    },
    {
      "date": "2024-06-02",
      "temperature": "18°C",
      "condition": "Sunny"
    },
    ...
  ]
}
```
## Contributing
If you would like to contribute to the project, please follow these steps:

- Fork the repository
- Create a new branch (git checkout -b feature-branch)
- Make your changes
- Commit your changes (git commit -m 'Add some feature')
- Push to the branch (git push origin feature-branch)
- Create a new Pull Request
