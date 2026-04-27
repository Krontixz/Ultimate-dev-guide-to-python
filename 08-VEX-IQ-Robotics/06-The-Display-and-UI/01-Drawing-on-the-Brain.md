# 🎨 Lesson 1: Brain Screen UI (The Dashboard)

A pro robot doesn't just print text; it shows graphs, status bars, and buttons. This allows you to "debug" your robot without needing to plug it into a laptop.

## 1. The 5-Year-Old Spark ⚡
Imagine the VEX Brain is like a tiny iPad. Instead of just reading boring words, you can draw a battery bar that changes color or a "Start" button you can actually tap on the screen!



## 2. The Deep Dive 🤿
The `brain.screen` class has functions for shapes and colors. The screen is a grid of pixels: **0 to 159 (Y-axis)** and **0 to 175 (X-axis)**.

```python
from vex import *

brain = Brain()

def draw_dashboard(battery_level, motor_temp):
    # Clear screen and set background
    brain.screen.clear_screen(Color.BLACK)
    
    # Draw a Battery Bar (Rectangle)
    brain.screen.set_fill_color(Color.GREEN)
    # draw_rectangle(x, y, width, height)
    brain.screen.draw_rectangle(10, 10, battery_level, 20)
    
    # Draw a Warning Circle if motor is too hot
    if motor_temp > 50:
        brain.screen.set_fill_color(Color.RED)
        brain.screen.draw_circle(140, 30, 10)
        
    brain.screen.set_cursor(3, 1)
    brain.screen.print("SYSTEM STATUS: NOMINAL")

# Test it
draw_dashboard(80, 25)
```

## 3. The Quest: The Digital Speedometer ⚔️
1. Create `01_ui_task.py`.
2. Write a loop that gets the `velocity` of a motor.
3. Draw a line on the screen that gets longer as the motor spins faster.
4. If the motor stops, make the screen turn bright RED.
