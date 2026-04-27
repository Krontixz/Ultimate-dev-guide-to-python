# 🧠 Lesson 2: State Machines (Complex Behavior)

How does a robot know to switch from "Searching for a ball" to "Picking up the ball" to "Driving to the goal"? We use a **State Machine**.

## 1. The 5-Year-Old Spark ⚡
Think of a traffic light. It is either Green, Yellow, or Red. It has "Rules" for when to change. A State Machine is just a list of "Modes" your robot can be in.



## 2. The Deep Dive 🤿
We use a variable to keep track of the "Current State" and a `while` loop to execute the logic for that state.

```python
STATE_SEARCHING = 0
STATE_PICKUP = 1
STATE_DELIVER = 2

current_state = STATE_SEARCHING

while True:
    if current_state == STATE_SEARCHING:
        drivetrain.drive(FORWARD)
        if distance_sensor.object_distance(MM) < 100:
            current_state = STATE_PICKUP
            
    elif current_state == STATE_PICKUP:
        arm_motor.spin_for(FORWARD, 90, DEGREES)
        current_state = STATE_DELIVER
        
    elif current_state == STATE_DELIVER:
        # Drive to a specific coordinate or color
        pass
        
    wait(20, MSEC)
```

## 3. The Quest: The Security Guard ⚔️
1. Create `02_state_task.py`.
2. Define three states: `PATROL`, `CHASE`, and `RETURN`.
3. Patrol: Drive in a square.
4. Chase: If the distance sensor sees something, drive toward it.
5. Return: If the object is gone, drive back to the start.
