# 🦾 Lesson 2: Multi-Joint Coordination (The SCARA Logic)

Moving one motor is easy. Moving a "Shoulder" and an "Elbow" at the same time so the hand moves in a perfectly straight line is hard. This is called **Coordinate Geometry**.

## 1. The 5-Year-Old Spark ⚡
Imagine trying to draw a straight line on a piece of paper, but you can only move your shoulder and your elbow. If you move them at the same speed, your hand will draw a big curve. To draw a straight line, your elbow has to move at a different speed than your shoulder.



## 2. The Deep Dive 🤿
To make the "Hand" move from Point A to Point B, we use **Interpolation**. We break the big movement into 100 tiny "micro-steps."

```python
import math

def move_arm_linear(start_x, start_y, end_x, end_y, steps=20):
    for i in range(steps + 1):
        # Calculate the intermediate point
        target_x = start_x + (end_x - start_x) * (i / steps)
        target_y = start_y + (end_y - start_y) * (i / steps)
        
        # Calculate angles for this specific micro-step
        # (Using the Inverse Kinematics function from Lesson 1)
        angle_shoulder, angle_elbow = calculate_ik(target_x, target_y)
        
        # Move motors to these precise positions
        shoulder_motor.spin_to_position(angle_shoulder, DEGREES, wait=False)
        elbow_motor.spin_to_position(angle_elbow, DEGREES, wait=True)
```

## 3. The Quest: The Perfect Square ⚔️
1. Create `02_multi_joint_task.py`.
2. Write a script that makes the arm "draw" a 100mm square in the air.
3. If you don't use interpolation, the "lines" of your square will be curved!
4. **Championship Tip:** Use this to move your claw perfectly vertical so you don't knock over stacks of blocks!
