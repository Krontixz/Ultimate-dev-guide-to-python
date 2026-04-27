# 🌐 Lesson 2: APIs (How Robots Talk to the Web)

An **API** is a "waiter" for data. Your robot asks the waiter for information (like the weather or GPS data), and the waiter brings it back in a format called **JSON**.

## 1. The 5-Year-Old Spark ⚡
Imagine your robot is at a restaurant. It can't go into the kitchen to cook the food. It tells the waiter (the API) what it wants. The waiter brings a plate (the JSON) with exactly what was asked for.



## 2. The Deep Dive 🤿
The most popular library for this is `requests`. JSON data looks exactly like a Python **Dictionary**, which makes it super easy to use.

```python
import requests

# Let's ask a public API for the current location of the ISS
url = "[http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]
    print(f"The ISS is currently at Lat: {lat}, Lon: {lon}")
else:
    print("Connection lost to Ground Control.")
```

## 3. The Quest: Weather Scout ⚔️
1. Install the requests library: `pip install requests`.
2. Create `02_api_task.py`.
3. Search for a "Free Weather API" or use a mock URL.
4. Try to pull the "Temperature" out of a JSON response and print it.
