# 🌤️ Weather API

A FastAPI-powered REST API that provides real-time weather information for cities around the world.

The API uses the OpenWeatherMap API to retrieve current weather conditions and requires both a country and city to ensure accurate results. Users can retrieve temperature, weather descriptions, humidity, pressure, and wind speed in either metric or imperial units.

## 🚀 Live Demo

API Documentation (Swagger UI):

https://weather-api-production-90cd.up.railway.app/docs

## ✨ Features

- 🌍 Real-time weather data for cities worldwide
- 🏙️ Country and city-based weather lookup
- 🌡️ Temperature in Celsius or Fahrenheit
- ☁️ Weather description
- 💨 Wind speed
- 💧 Humidity
- 📊 Atmospheric pressure
- ⚠️ Graceful error handling
- 🚀 Deployed on Railway

## 🛠️ Tech Stack

- Python
- FastAPI
- OpenWeatherMap API
- httpx
- pycountry
- Railway

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/sannibabalola/weather-api.git
cd weather-api
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` File

```env
OPENWEATHER_API_KEY=your_api_key_here
```

### Run the Application

```bash
uvicorn main:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000/docs
```

## 📖 API Usage

### Endpoint

```http
GET /weather/
```

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| country | string | ✅ Yes | Country name |
| city | string | ✅ Yes | City name |
| units | string | No | `metric` (default) or `imperial` |

### Example Request

```http
GET /weather/?country=Nigeria&city=Lagos&units=metric
```

### Example Response

```json
{
  "country": "Nigeria",
  "city": "Lagos",
  "temperature": 27.4,
  "description": "few clouds",
  "humidity": 83,
  "pressure": 1012,
  "wind_speed": 3.6,
  "units": "metric"
}
```

## ⚠️ Error Handling

### Invalid City

```json
{
  "detail": "City not found"
}
```

### Invalid Units

```json
{
  "detail": "Units must be 'metric' or 'imperial'"
}
```

## 📂 Project Structure

```text
weather-api/
│
├── main.py
├── weather.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🎯 What I Learned

This project helped me gain hands-on experience with:

- FastAPI development
- REST API design
- API integration
- Query parameters
- Error handling
- Environment variables
- Asynchronous HTTP requests with httpx
- Deployment using Railway

## 🔮 Future Improvements

- Add 5-day weather forecasts
- Add geolocation support
- Implement caching
- Add API rate limiting
- Add automated tests
- Dockerize the application

## 👨‍💻 Author

**Babalola Sanni**

- GitHub: https://github.com/sannibabalola
- X (Twitter): https://instagram.com/debabzzy

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

## 📄 License

This project is licensed under the MIT License.
