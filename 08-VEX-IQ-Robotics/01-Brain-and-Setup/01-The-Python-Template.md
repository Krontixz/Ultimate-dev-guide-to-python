# 🤖 Lesson 1: The Brain and the Template

Every VEX Python project starts with a "Header." This is the code that tells the Brain which motors are plugged into which ports.

## 1. The 5-Year-Old Spark ⚡
Imagine your robot is a body. Before it can move, the brain needs to know where the arms and legs are. Port 1 might be the "Left Leg," and Port 6 might be the "Right Leg." If you don't tell the brain this, it's just a plastic box!



## 2. The Deep Dive 🤿
In VEX Python, we import the `vex` library. We then "assign" motors to ports.

```python
from vex import *

# Brain and Controller Setup
brain = Brain()
controller = Controller()

# Motor Setup: Port, Gear Ratio, Reversed?
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True)

# The Drivetrain (The 'Block' equivalent of a Drivetrain device)
dt = SmartDrive(left_motor, right_motor, 200, 320, 176, mm)
```

## 3. The Quest: System Check ⚔️
1. Create a file named `01_setup.py`.
2. Write the code to initialize the Brain and one Motor on Port 10.
3. Add a line to print "System Online" to the **Brain's LCD Screen** using `brain.screen.print("System Online")`.
