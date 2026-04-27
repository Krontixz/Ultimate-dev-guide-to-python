# 🚀 Lesson 1: Your First Web Server

A "Server" is just a Python script that stays awake 24/7, waiting for someone to talk to it. When a robot (or a browser) sends a message, the server responds.

## 1. The 5-Year-Old Spark ⚡
Imagine your computer is a lemonade stand. You sit there waiting. When a customer (a user) comes and asks for a drink, you give it to them. A backend server is just a digital lemonade stand that serves **data** instead of juice.



## 2. The Deep Dive 🤿
We use **FastAPI**. It handles the "plumbing" of the internet for us.

* **Uvicorn:** This is the "Engine" that keeps the server running.
* **Routes (@app.get):** These are like different windows at a bank. One window for "Check Balance," one for "Withdraw."

```python
# Save this as main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mission Control Online"}

@app.get("/status")
def get_status():
    return {"battery": "85%", "location": "Sector 7G"}
```

## 3. The Quest: Launch the Server ⚔️
1.  Install the tools: `pip install "fastapi[all]"`
2.  Create `main.py` with the code above.
3.  In your terminal, run: `uvicorn main:app --reload`
4.  Open your browser and go to `http://127.0.0.1:8000/status`
5.  **Challenge:** Add a new "Route" called `/telemetry` that returns the robot's speed and heading.
