# 🎮 Lesson 1: Manual Control (Tele-Op)

This is how you turn your VEX Controller into a remote for the robot. We mirror the "Joystick" blocks here.

## 1. The 5-Year-Old Spark ⚡
Imagine the joystick is a gas pedal. The further you push it, the faster the motor spins. We just need a loop that constantly asks: "Where is the stick pointing right now?"



## 2. The Deep Dive 🤿
We use a `while True` loop to keep the robot responsive. We map the `position()` of the joystick (which is -100 to 100) directly to the motor velocity.

```python
while True:
    # Tank Drive Style
    # Left stick (Axis 3) controls left motor
    # Right stick (Axis 2) controls right motor
    left_motor.set_velocity(controller.axis3.position(), PERCENT)
    right_motor.set_velocity(controller.axis2.position(), PERCENT)
    
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)
    
    wait(20, MSEC) # Don't hog the brain's CPU!
```

## 3. The Quest: Arcade Drive ⚔️
Create a file named `01_controller_task.py`.
1. Modify the loop so that Axis 3 controls forward/backward.
2. Use Axis 1 to control turning (Left motor speed + turn, Right motor speed - turn).
3. Add a button command: If `controller.buttonA.pressing()`, spin a third motor (an intake or arm).
