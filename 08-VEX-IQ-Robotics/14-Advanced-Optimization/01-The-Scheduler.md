# ⚡ Lesson 1: Custom Schedulers (Optimized Brains)

The VEX Brain is powerful, but if you have 20 sensors and 6 motors all running in one `while True` loop, the robot will lag. We build a **Scheduler** to prioritize the most important tasks.

## 1. The 5-Year-Old Spark ⚡
Imagine a plate-spinner at the circus. He doesn't look at every plate at once. He checks the wobbly ones more often than the stable ones. A scheduler tells the robot: "Check the distance sensor every 10ms, but only check the battery every 5000ms."

## 2. The Deep Dive 🤿
We use the `timer` to create different "frequencies" for our code.

```python
next_sensor_check = 0
next_battery_check = 0

while True:
    current_time = brain.timer.time(MSEC)
    
    # High Priority: Collision Detection (Every 20ms)
    if current_time > next_sensor_check:
        check_collisions()
        next_sensor_check = current_time + 20
        
    # Low Priority: Battery & Temp (Every 2 seconds)
    if current_time > next_battery_check:
        update_ui_stats()
        next_battery_check = current_time + 2000
        
    wait(5, MSEC) # Smallest possible wait
```

## 3. The Quest: The Resource Monitor ⚔️
1. Create `01_scheduler_task.py`.
2. Create three "Tasks" with different timers:
   - Task 1: Flash a light every 100ms.
   - Task 2: Print "Scanning..." every 500ms.
   - Task 3: Calculate a complex math equation every 1000ms.
3. Watch how smooth the robot runs when it isn't trying to do everything at 1000mph!
