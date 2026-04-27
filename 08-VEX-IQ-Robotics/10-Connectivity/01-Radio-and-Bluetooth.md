# 📡 Lesson 1: Radio and Bluetooth Management

Robots can "talk" to the Controller via 2.4GHz radio or Bluetooth. Advanced teams use this for **Live Telemetry**—sending data from the robot back to the controller screen so the driver knows if a motor is overheating.

## 1. The 5-Year-Old Spark ⚡
It’s like a secret walkie-talkie. The robot can whisper to the driver's hand: "Hey, my arm is stuck!" or "Battery is at 10%!" This helps the driver make better choices during the game.

## 2. The Deep Dive 🤿
You can print messages directly to the **Controller's tiny screen** (not just the Brain).

```python
while True:
    temp = arm_motor.temperature(PERCENT)
    
    # Only update if the motor is getting hot to save battery
    if temp > 70:
        controller.screen.clear_line(1)
        controller.screen.set_cursor(1, 1)
        controller.screen.print("MOTOR HOT: " + str(temp) + "%")
        controller.rumble("-.-") # Makes the controller vibrate!
    
    wait(1, SECONDS)
```

## 3. The Quest: Feedback Loop ⚔️
1. Create `01_radio_feedback.py`.
2. Write a script that "Rumbles" the controller when the Distance Sensor sees something closer than 100mm.
3. This creates a "Haptic" sensor for the driver, so they "feel" the wall before they hit it!
