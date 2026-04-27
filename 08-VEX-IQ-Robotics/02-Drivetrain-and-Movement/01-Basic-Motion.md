# 🏎️ Lesson 1: Driving and Turning

This is the Python version of the "Drive Forward" and "Turn Right" blocks. In Python, we have much more control over speed and "blocking."

## 1. The 5-Year-Old Spark ⚡
Driving a robot is like giving directions to a friend who is blindfolded. You don't just say "Go!" You have to say "Go forward exactly 10 steps and then stop."

## 2. The Deep Dive 🤿
VEX Python uses "Blocking" commands. This means the code waits for the robot to finish driving before moving to the next line.

* `dt.drive_for(FORWARD, 200, MM)` - Drives exactly 200mm.
* `dt.turn_for(RIGHT, 90, DEGREES)` - Turns exactly 90 degrees.
* `dt.set_drive_velocity(50, PERCENT)` - Sets the speed (1-100).

```python
# Simple Square Pattern
for i in range(4):
    dt.drive_for(FORWARD, 300, MM)
    dt.turn_for(RIGHT, 90, DEGREES)
```

## 3. The Quest: The Slalom ⚔️
Create a file named `01_movement_task.py`.
1. Drive forward 500mm.
2. Turn left 45 degrees.
3. Drive forward 200mm.
4. Turn right 45 degrees.
5. Reverse back to the starting spot.
