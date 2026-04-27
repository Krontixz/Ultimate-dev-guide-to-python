# 🔋 Lesson 18: Battery-Aware Strategy

As the battery dies, motors get weaker and sensors get noisier. A "Smart" robot changes its behavior to save energy or compensate for the power drop.

## 1. The 5-Year-Old Spark ⚡
When your phone gets to 5%, it dims the screen and turns off background apps to stay alive. Your robot should do the same! If the battery is low, maybe it drives slower so it doesn't "brown out" and restart in the middle of a match.

## 2. The Deep Dive 🤿
We check the `brain.battery.capacity()` and use it to scale our motor limits.

```python
def get_power_multiplier():
    cap = brain.battery.capacity()
    if cap < 20:
        return 0.5 # Half speed to save life
    elif cap < 50:
        return 0.8 # 80% speed
    return 1.0     # Full power!

while True:
    multiplier = get_power_multiplier()
    speed = controller.axis3.position() * multiplier
    left_motor.set_velocity(speed, PERCENT)
    # ... rest of drive code
```

## 3. The Quest: The Economy Mode ⚔️
1. Create `18_battery_task.py`.
2. Create a "Low Power" mode that triggers when the battery hits a certain point.
3. In this mode, change the Brain Screen to RED and rumble the controller to warn the driver.
