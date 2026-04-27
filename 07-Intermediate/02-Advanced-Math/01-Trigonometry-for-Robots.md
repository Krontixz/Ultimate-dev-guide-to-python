# 📐 Lesson 1: Trigonometry (Angles and Arms)

If you want a robot arm to move to a specific (X, Y) coordinate, or if you want a rover to turn exactly 45 degrees, you need Trigonometry. Python’s `math` module handles this for us.

## 1. The 5-Year-Old Spark ⚡
Imagine you have a giant clock hand. To know exactly where the tip of the hand is, you need to know how long the hand is and what time (the angle) it is pointing to. Sines and Cosines are just the "map coordinates" for the tip of that arm.

## 2. The Deep Dive 🤿
Computers don't usually think in Degrees (0-360); they think in **Radians**. 

**Key Functions:**
* `math.radians(deg)`: Converts degrees to radians (Crucial!).
* `math.sin()` / `math.cos()`: Finds the X and Y positions.
* `math.hypot(x, y)`: Finds the direct distance from the robot to a point.

```python
import math

angle_deg = 90
angle_rad = math.radians(angle_deg)

# Calculate the position of a 10-inch robot arm
x = 10 * math.cos(angle_rad)
y = 10 * math.sin(angle_rad)

print(f"Arm Tip Position: ({x}, {y})")
