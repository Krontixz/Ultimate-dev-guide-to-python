# 💾 Lesson 1: SD Card Logging (Black Box)

If your robot crashes during a competition, you need to know why. We can save sensor data to an SD card inside the VEX Brain to read it later on a computer.

## 1. The 5-Year-Old Spark ⚡
This is the "GoPro" of data. While the robot is driving, it is constantly writing down its speed and sensor values in a tiny notebook (the SD card). If the robot fails, you "read the notebook" to find the mistake.

## 2. The Deep Dive 🤿
VEX Python uses standard Python file handling (`open`, `write`, `close`).

```python
# Note: Requires an SD Card inserted into the Brain
def log_event(message):
    with open("robot_log.txt", "a") as f:
        f.write(message + "\n")

# Log a collision
if bumper.pressing():
    log_event("COLLISION DETECTED AT 5.2 SECONDS")
    drivetrain.stop()
```

## 3. The Quest: Flight Recorder ⚔️
1. Create `01_logging_task.py`.
2. Write a loop that records the `Distance Sensor` value every 100ms.
3. Run the robot for 10 seconds while moving your hand in front of the sensor.
4. Take the SD card out, plug it into your computer, and open `robot_log.txt` to see your data "played back."
