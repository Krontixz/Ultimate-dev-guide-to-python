# 🏆 Lesson 1: The Official Competition Template

In a real VEX IQ tournament, the "Field Controller" tells your robot when to start and stop. If you don't use the official template, your robot might sit still while the match starts, or keep driving after the buzzer (which gets you disqualified!).

## 1. The 5-Year-Old Spark ⚡
Imagine a race where the referee has a remote control. They press "Go" for the 15-second Autonomous period, then "Stop." Then they press "Go" for the Driver period. The template is like a set of ears that listens for the referee's remote.



## 2. The Deep Dive 🤿
The template splits your code into three distinct "Buckets."

```python
from vex import *

competition = Competition(user_driver, user_autonomous)
brain = Brain()

def user_autonomous():
    # Everything here runs for the first 15 seconds
    # No controller input allowed!
    drivetrain.drive_for(FORWARD, 500, MM)

def user_driver():
    # Everything here runs when the referee enables the joysticks
    while True:
        left_motor.set_velocity(controller.axis3.position(), PERCENT)
        left_motor.spin(FORWARD)
        wait(20, MSEC)

# The 'Main' setup only runs once when the brain turns on
brain.screen.print("WAITING FOR MATCH...")
```

## 3. The Quest: The Match Simulation ⚔️
1. Create `01_comp_template.py`.
2. Add a special light sequence to `user_autonomous` (flashing the Brain screen).
3. Add your Joystick logic to `user_driver`.
4. **Test:** In the VEXcode software, use the "Competition Project" preview to see if you can switch between modes.
