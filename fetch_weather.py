import requests
import json

# 第一步：取得目前 IP 推估位置
location_url = "https://ipapi.co/json/"
location_response = requests.get(location_url)
location_response.raise_for_status()
location_data = location_response.json()

latitude = location_data["latitude"]
longitude = location_data["longitude"]
city = location_data["city"]
timezone = location_data["timezone"]

# 第二步：用經緯度查天氣
weather_url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&current=temperature_2m,weather_code"
    f"&daily=temperature_2m_max,temperature_2m_min"
    f"&timezone={timezone}"
)

weather_response = requests.get(weather_url)
weather_response.raise_for_status()
weather_data = weather_response.json()

# 第三步：整理成一份輸出 JSON
output = {
    "location": {
        "city": city,
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone
    },
    "weather": weather_data
}

with open("weather.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("已根據目前定位取得天氣資料，並儲存為 weather.json")