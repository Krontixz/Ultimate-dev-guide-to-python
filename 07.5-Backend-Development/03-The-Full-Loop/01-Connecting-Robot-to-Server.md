# 🔗 Lesson 3: The Full Loop (Robot ➡️ Server ➡️ DB)

This is the "Holy Grail." We are going to make a Python script (the Robot) send data to our FastAPI server, which then saves it to the SQLite database.

## 1. The 5-Year-Old Spark ⚡
Think of a walkie-talkie. The robot talks into it, the server hears it, and writes it down in a notebook. Later, you can look at the notebook to see what the robot said two hours ago.



## 2. The Deep Dive 🤿
You will use the `requests` library we learned in the Intermediate section to "POST" data to your server.

**Server Side (FastAPI):**
```python
@app.post("/log-data")
def save_data(item: dict):
    # (Logic to save 'item' into SQLite goes here)
    return {"status": "Received and Saved"}
```

**Robot Side (Client):**
```python
import requests
data = {"sensor": "Ultrasonic", "value": 45.5}
requests.post("[http://127.0.0.1:8000/log-data](http://127.0.0.1:8000/log-data)", json=data)
```

## 3. The Quest: Black Box Recorder ⚔️
1.  Set up a FastAPI server that accepts a POST request.
2.  Write a second script that simulates a robot driving and sending its "Distance" every 2 seconds.
3.  Verify that your server is receiving the data and printing it to the console!
