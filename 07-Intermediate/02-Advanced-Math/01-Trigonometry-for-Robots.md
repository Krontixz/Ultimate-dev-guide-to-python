# 📐 Lesson 1: Trigonometry (Angles and Arms)

If you want a robot arm to move to a specific (X, Y) coordinate, or if you want a rover to turn exactly 45 degrees, you need Trigonometry. Python’s `math` module handles this for us.

## 1. The 5-Year-Old Spark ⚡
Imagine your robot arm is a giant clock hand. To know exactly where the tip of the hand is, you need to know how long the hand is and the angle it's pointing at. Sines and Cosines are the math tools that give us those (X, Y) coordinates.



## 2. The Deep Dive 🤿
Computers usually think in **Radians**, not Degrees. 

* **math.radians(deg):** Converts degrees to radians.
* **math.sin():** Finds the Vertical (Y) position.
* **math.cos():** Finds the Horizontal (X) position.

```python
import math

angle_deg = 30
angle_rad = math.radians(angle_deg)

# Calculate the position of a 10-inch robot arm
x = 10 * math.cos(angle_rad)
y = 10 * math.sin(angle_rad)

print(f"Arm Tip Position: ({x}, {y})")
```

## 3. The Quest: Target Lock ⚔️
Create a file named `01_trig_task.py`.
1. A drone is 50 meters away (hypotenuse) at a 30-degree angle from the ground.
2. Use `math.sin()` to find how high (altitude) the drone is. 
3. **Note:** Remember to convert 30 degrees to radians first!
4. Print: "Drone Altitude: [Result] meters."
