# 🏎️ Lesson 1: PID Line Following (The Pro Way)

Most students use "If/Else" to follow a line. It's jerky and slow. Professionals use **PID** (Proportional, Integral, Derivative) to make the robot move like a smooth racing car.

## 1. The 5-Year-Old Spark ⚡
If you are driving a car and you drift a *little* bit off the road, you don't yank the steering wheel all the way to the side. You turn it just a little. If you drift a *lot*, you turn it more. PID is just "Turning the wheel only as much as you need to."



## 2. The Deep Dive 🤿
We calculate the **Error** (how far we are from the edge of the line) and use that to set our turn speed.

```python
target_brightness = 50  # The "edge" of the line
kP = 0.6               # How "aggressive" the steering is

while True:
    current_val = eye.brightness()
    error = target_brightness - current_val
    
    # Turn based on the error
    turn_velocity = error * kP
    
    left_motor.set_velocity(50 + turn_velocity, PERCENT)
    right_motor.set_velocity(50 - turn_velocity, PERCENT)
    
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)
    wait(10, MSEC)
```

## 3. The Quest: The Smooth Racer ⚔️
1. Create `01_pid_line_task.py`.
2. Tune the `kP` value. If the robot wobbles too much, make it smaller. If it doesn't turn enough, make it bigger.
3. Can you reach a speed of 70% without falling off the line?
