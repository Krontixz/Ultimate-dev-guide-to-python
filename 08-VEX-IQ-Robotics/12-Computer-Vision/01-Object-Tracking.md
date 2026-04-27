# 👁️ Lesson 1: The Vision Sensor (AI Eyes)

The Vision Sensor doesn't just see light; it recognizes **Shapes** and **Colors**. It can tell the difference between a "Blue Cube" and a "Blue Robot" based on size and signatures.

## 1. The 5-Year-Old Spark ⚡
Imagine your robot has a "Wanted" poster. You show it a picture of a yellow ball. Now, whenever the robot looks around, it ignores everything else until it sees that specific yellow shape. When it finds it, it points and says, "There it is!"



## 2. The Deep Dive 🤿
You must first "Train" the sensor in the VEX Utility to recognize a color signature (e.g., `SIG_1`). In Python, we ask the sensor for the "Largest Object" of that type.

```python
from vex import *

vision_sensor = Vision(Ports.PORT4, 50) # 50 is the brightness setting

while True:
    # Look for objects with Signature 1 (The Yellow Ball)
    vision_sensor.take_snapshot(SIG_1)
    
    if vision_sensor.largest_object.exists:
        # Find the center of the object
        obj_x = vision_sensor.largest_object.centerX
        
        # If it's to the left (center is 157), turn left
        if obj_x < 140:
            drivetrain.turn(LEFT)
        elif obj_x > 175:
            drivetrain.turn(RIGHT)
        else:
            brain.screen.print("TARGET LOCKED")
            drivetrain.stop()
    else:
        brain.screen.print("SEARCHING...")
    
    wait(100, MSEC)
```

## 3. The Quest: The Heat-Seeker ⚔️
1. Create `01_vision_task.py`.
2. Set up a signature for a bright green object.
3. Write a script that makes the robot "Follow" the green object. As you move the object, the robot should drive forward/backward to keep the object a specific size on the screen.
