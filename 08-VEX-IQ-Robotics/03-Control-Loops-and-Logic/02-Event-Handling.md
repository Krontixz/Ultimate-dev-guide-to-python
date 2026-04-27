# 🔔 Lesson 2: Events (Don't Wait, React!)

Most code runs line-by-line. **Events** allow the robot to "listen" for things (like a bumper press) in the background and jump to a function instantly.

## 1. The 5-Year-Old Spark ⚡
Imagine you are reading a book. If the doorbell rings, you don't wait until you finish the chapter to answer it; you stop immediately, handle the door, and then go back to your book. That is an "Event."

## 2. The Deep Dive 🤿
We use "Callbacks." We tell Python: "When this button is pressed, run THIS function."

```python
bumper = Bumper(Ports.PORT2)

def emergency_stop():
    drivetrain.stop()
    brain.screen.clear_screen()
    brain.screen.print("BUMPER HIT: STOPPED")
    # This function runs the INSTANT the bumper is touched

# Register the event (This is the 'Listener')
bumper.pressed(emergency_stop)

# Main code continues here
drivetrain.drive(FORWARD, 50, PERCENT)
while True:
    wait(20, MSEC) # Keeping the program alive
```

## 3. The Quest: The Panic Button ⚔️
1. Create `02_event_task.py`.
2. Set up an event where pressing the `Controller.buttonUp` increases the robot's speed.
3. Set up another event where `Controller.buttonDown` decreases it.
4. Make the robot drive forward in the `while True` loop and test your "on-the-fly" speed adjustments.
