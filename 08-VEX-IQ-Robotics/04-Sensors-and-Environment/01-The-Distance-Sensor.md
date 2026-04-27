# 📏 Lesson 1: The Distance Sensor (Eyes of the Robot)

The Distance Sensor uses ultrasonic waves (sonar) to see how far away an object is. This is the foundation of "Object Avoidance."

## 1. The 5-Year-Old Spark ⚡
Imagine your robot is a bat. It screams a tiny sound (that humans can't hear), waits for the sound to hit a wall and bounce back, and then calculates how long it took. If the sound comes back fast, the wall is close!



## 2. The Deep Dive 🤿
In Python, we can get the distance in `MM` or `INCHES`. We use this to create "Stop Conditions."

```python
from vex import *

# Setup
brain = Brain()
dist_sensor = Distance(Ports.PORT7)
drivetrain = SmartDrive(Motor(Ports.PORT1), Motor(Ports.PORT6))

# The "Safety Wall" Logic
while True:
    # Get the current distance
    current_dist = dist_sensor.object_distance(MM)
    
    if current_dist < 100:
        # Emergency Stop if closer than 100mm
        drivetrain.stop()
        brain.screen.print("OBJECT DETECTED!")
    else:
        drivetrain.drive(FORWARD)
    
    wait(20, MSEC)
```

## 3. The Quest: The Wall Follower ⚔️
1. Create `01_distance_task.py`.
2. Write a script where the robot drives forward until it is exactly 150mm from a wall.
3. Once it hits 150mm, have it turn 90 degrees and stop.
4. **Ultimate Challenge:** Can you make it drive in a circle around an object, always staying exactly 200mm away? (This requires constant adjustment!)
