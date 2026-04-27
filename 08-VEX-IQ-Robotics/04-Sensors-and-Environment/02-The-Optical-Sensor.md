# 🌈 Lesson 2: Optical Sensor (Color & Light)

The Optical Sensor detects colors, brightness, and even how much light is reflecting off the floor. This is how robots "see" lines on the ground.

## 1. The 5-Year-Old Spark ⚡
Imagine the robot has a tiny flashlight and a tiny camera. It shines the light on the floor and asks: "Is this white paper or black tape?" Because black tape absorbs light, the robot knows exactly where the line is.



## 2. The Deep Dive 🤿
The sensor returns a `color()` or a `brightness()` value.

```python
eye = Optical(Ports.PORT3)

while True:
    if eye.color() == Color.RED:
        brain.screen.print("Target Found: RED")
        brain.set_timer_value(0, MSEC) # Start a timer
    elif eye.color() == Color.BLUE:
        brain.screen.print("Target Found: BLUE")
    
    # Check for reflective brightness (0-100)
    if eye.brightness() < 20:
        print("I am over a dark line!")
```

## 3. The Quest: Traffic Light ⚔️
1. Create `02_optical_task.py`.
2. The robot should drive forward.
3. If it sees **RED**, it must stop for 3 seconds, then continue.
4. If it sees **GREEN**, it should double its speed.
5. If it sees **BLUE**, it should spin in a circle once.
