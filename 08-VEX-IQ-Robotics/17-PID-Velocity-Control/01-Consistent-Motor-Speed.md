# 🏎️ Lesson 17: PID Velocity Control (Anti-Friction Logic)

In a basic robot, if a motor is rubbing against the frame, it slows down. In a Championship robot, the code detects the slow-down and pumps more power into the motor to keep the speed perfect.

## 1. The 5-Year-Old Spark ⚡
Imagine you are riding a bike. When you start going up a hill, it gets harder to pedal. If you want to keep the same speed, you have to push much harder with your legs. PID Velocity Control is the robot "pushing harder" the moment it feels a hill or some friction.



## 2. The Deep Dive 🤿
We compare the **Target Velocity** with the **Actual Velocity** (from the encoders) and adjust the voltage.

```python
target_vel = 50 # We want 50% speed
kP = 1.2        # Proportional gain

while True:
    actual_vel = left_motor.velocity(PERCENT)
    error = target_vel - actual_vel
    
    # Adjust power based on error
    current_power = left_motor.voltage() + (error * kP)
    left_motor.spin(FORWARD, current_power, VOLT)
    
    wait(20, MSEC)
```

## 3. The Quest: The Heavy Load ⚔️
1. Create `17_velocity_task.py`.
2. Run a motor at 30% speed.
3. Lightly press your finger against the wheel to create friction.
4. Watch how the PID loop increases voltage to fight your finger and keep the wheel spinning at 30%!
