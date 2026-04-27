# 🧵 Lesson 2: Multi-threading (Doing Two Things at Once)

Normally, Python is "Single-Threaded" (it has one brain). `threading` allows us to give the robot a "Second Brain" to handle background tasks.

## 1. The 5-Year-Old Spark ⚡
Imagine trying to pat your head and rub your tummy at the same time. It's hard for one brain! Multi-threading is like having a twin brother stand next to you; you pat your head, and he rubs your tummy. Teamwork!



## 2. The Deep Dive 🤿
We use the `threading` module to start a function in the background while the rest of our code keeps running.

```python
import threading
import time

def background_music():
    while True:
        print("🎵 Playing Background Music...")
        time.sleep(2)

# Start the 'Second Brain'
thread = threading.Thread(target=background_music, daemon=True)
thread.start()

# The 'Main Brain' keeps working here
for i in range(5):
    print(f"Main robot logic: Step {i}")
    time.sleep(1)

print("Main task finished!")
```

## 3. The Quest: The Guard Dog ⚔️
Create a file named `02_threading_task.py`.
1. Create a function called `sensor_monitor` that prints "Scanning for obstacles..." every 0.5 seconds.
2. Start that function as a separate thread.
3. In the main part of your code, ask the user for their name using `input()`.
4. Notice how the scanner keeps printing even while the computer is waiting for you to type!
