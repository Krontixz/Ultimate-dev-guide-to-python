# 🗺️ Lesson 1: Pure Pursuit (Driving Like a Pro)

Basic robots drive: *Forward -> Stop -> Turn -> Stop -> Forward*. 
Championship robots drive in **Smooth Curves**. **Pure Pursuit** is an algorithm where the robot "looks ahead" to a point on a path and constantly steers toward it.

## 1. The 5-Year-Old Spark ⚡
Imagine you are running through a forest. You don't look at your feet. You look at a tree 10 feet ahead of you and run toward it. As you get closer, you pick a new tree further away. This keeps your path smooth and fast.



## 2. The Deep Dive 🤿
This requires the **Odometry** (X, Y tracking) we built earlier. The robot calculates the steering angle needed to hit a "Look-Ahead" point.

```python
path = [(0,0), (500, 200), (1000, 0)] # A list of (X, Y) coordinates
look_ahead_dist = 200 # How far ahead the robot 'looks'

def get_steering_dir(curr_x, curr_y, path):
    # 1. Find the point on the path that is 'look_ahead_dist' away
    target = find_target_on_path(curr_x, curr_y, path, look_ahead_dist)
    
    # 2. Calculate angle to that target
    angle_to_target = math.atan2(target.y - curr_y, target.x - curr_x)
    
    # 3. Steering is the difference between current heading and target angle
    return math.degrees(angle_to_target) - gyro.heading()

# Apply this to your motor speeds
```

## 3. The Quest: The S-Curve ⚔️
1. Create `01_path_task.py`.
2. Define a path that looks like an "S" shape.
3. Use your Odometry logic to track the robot's position.
4. Implement a simple "Look-Ahead" logic where the robot tries to stay on the S-curve without ever stopping.
