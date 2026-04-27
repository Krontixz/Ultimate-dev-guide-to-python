# 🧭 Lesson 3: The Inertial Sensor (Perfect Turns)

In basic coding, you turn for "90 Degrees," but the wheels might slip, leaving you at 85 degrees. The Inertial Sensor (Gyro) uses Earth's gravity and motion to ensure every turn is pixel-perfect.

## 1. The 5-Year-Old Spark ⚡
Imagine you are spinning in a circle with your eyes closed. You might get dizzy and lose track of where you started. The Inertial Sensor is like a built-in compass that always knows exactly which way the robot is facing, even if the wheels slip on a slippery floor.



## 2. The Deep Dive 🤿
The Inertial sensor needs to "Calibrate" (sit still for 2 seconds) when the program starts. Once it's ready, we use the `rotation` value to stop our turns.

```python
from vex import *

brain = Brain()
gyro = Inertial(Ports.PORT12)

# 1. Calibration is MANDATORY
gyro.calibrate()
while gyro.is_calibrating():
    wait(50, MSEC)

# 2. The Perfect 90-Degree Turn
def gyro_turn(target_angle):
    # Reset current heading to 0
    gyro.set_rotation(0, DEGREES)
    
    # Start spinning
    left_motor.spin(FORWARD, 30, PERCENT)
    right_motor.spin(REVERSE, 30, PERCENT)
    
    # Wait until the gyro says we hit the target
    while gyro.rotation(DEGREES) < target_angle:
        wait(5, MSEC)
        
    left_motor.stop()
    right_motor.stop()

gyro_turn(90)
```

## 3. The Quest: The Compass ⚔️
1. Create `03_gyro_task.py`.
2. Write a script that prints the robot's `heading()` to the brain screen constantly.
3. Physically turn the robot with your hand and watch the numbers change from 0 to 359.
4. **Ultimate Challenge:** Make the robot drive in a perfect hexagon (6 sides) using the gyro for every 60-degree turn.
