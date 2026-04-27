# 📍 Lesson 2: Odometry (Where am I?)

Odometry is the math of tracking your (X, Y) position on the field at all times. If the robot knows it is at `(1200, 800)`, it can drive back to `(0, 0)` perfectly without needing to see a line.

## 1. The 5-Year-Old Spark ⚡
Imagine walking across a dark room. You count your steps and remember every turn you made. Even with your eyes closed, you can guess where you are in the room. This is "Dead Reckoning."

## 2. The Deep Dive 🤿
This combines the **Inertial Sensor** (Heading) and **Motor Encoders** (Distance).

```python
import math

curr_x = 0
curr_y = 0

def update_position(distance_moved, current_heading):
    global curr_x, curr_y
    # Convert heading to radians for math
    rad = math.radians(current_heading)
    
    # Use Trig to find change in X and Y
    curr_x += distance_moved * math.cos(rad)
    curr_y += distance_moved * math.sin(rad)

# In your drive loop:
last_pos = drivetrain.position(MM)
while True:
    change = drivetrain.position(MM) - last_pos
    update_position(change, gyro.heading())
    last_pos = drivetrain.position(MM)
    wait(20, MSEC)
```

## 3. The Quest: The Home Button ⚔️
1. Create `02_odometry_task.py`.
2. Drive the robot in a random "squiggle" using the controller.
3. Have the robot track its X and Y the whole time.
4. Press Button B to make the robot use those coordinates to drive straight back to `(0,0)`.
