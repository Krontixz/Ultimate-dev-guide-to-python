# 🛡️ Lesson 20: The Championship Shield (Zero-Failure Coding)

In the lab, you can just press "Reset." In a match, you have one shot. This file contains the "Pro Shields" used by world-class teams to ensure their code never dies.

## 1. The 5-Year-Old Spark ⚡
Imagine you are building a castle. It looks great, but what if a dragon breathes fire? Or what if a heavy rain starts? You need to build "Shields" like a moat and a stone roof. In code, we build shields to handle "Bad Luck."



## 2. The Deep Dive 🤿 (The 4 Shields)

### Shield 1: The "I'm Stuck" Timeout
**The Problem:** Your autonomous code says `drive_for(500, MM)`. Your robot hits a stray game piece and the wheels spin in place. The robot never reaches 500mm, so the code "hangs" and the robot does nothing for the rest of the match.
**The Shield:** Always use a `timeout`.

```python
# Instead of a blocking drive_for, use a timer
drivetrain.set_timeout(3, SECONDS) 
drivetrain.drive_for(FORWARD, 500, MM)
# If the robot isn't done in 3 seconds, it gives up and moves to the next line!
```

### Shield 2: The Optical "Sun-Glare" Filter
**The Problem:** The stadium lights are brighter than your classroom lights. Your "Line Follower" gets blinded and drives off the field.
**The Shield:** Calibrate at the start of every match.

```python
# At the start of user_autonomous:
white_value = eye.brightness() 
black_value = 0 # Assume black is near zero
threshold = (white_value + black_value) / 2
# Now your code adapts to the room's lighting!
```

### Shield 3: The Jiggled Cable (Try/Except)
**The Problem:** A motor cable gets pulled slightly during a collision. The Brain loses connection for a millisecond, and the Python script crashes with an "Error."
**The Shield:** Use `try/except` for critical systems.

```python
try:
    arm_motor.spin_to_position(90, DEGREES)
except:
    brain.screen.print("MOTOR ERROR - BYPASSING")
    # This keeps the REST of the code running even if the arm fails
```

### Shield 4: The "Watchdog" Thread
**The Problem:** Your main loop gets stuck in a complex calculation.
**The Shield:** A background thread that "pokes" the robot to make sure it's alive.

```python
def watchdog():
    while True:
        if brain.timer.time(MSEC) > 60000: # Match is over
            all_motors_off()
        wait(1, SECONDS)

# Start this in your main setup
Thread(watchdog)
```

## 3. The Quest: The Stress Test ⚔️
1. Create `20_shield_test.py`.
2. Write an autonomous routine that drives toward a wall.
3. **The Test:** While it's driving, pick the robot up so the wheels spin in the air.
4. If you have the **Timeout Shield** active, the robot should stop trying after a few seconds and move to the next task.
5. If it doesn't, your code is "vulnerable"—add the timeout!
