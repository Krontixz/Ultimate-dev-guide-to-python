# 💨 Lesson 1: Pneumatics (Instant Force)

Motors take time to spin. **Pneumatics** use compressed air to move a cylinder instantly. This is perfect for high-speed "Flippers" or "Claws" that need to snap shut in a millisecond.

## 1. The 5-Year-Old Spark ⚡
It's like a party popper! You build up pressure, and then—*POP*—it moves instantly. Instead of a motor slowly turning a gear, the air pushes a metal rod out at super speed.



## 2. The Deep Dive 🤿
In Python, we control the **Solenoid** (the electronic valve). It is either `EXTENDED` or `RETRACTED`.

```python
# Setup Pneumatic Cylinder on a 3-wire Port
claw = Pneumatics(brain.three_wire_port.a)

def toggle_claw():
    if controller.buttonR1.pressing():
        claw.extend()
    elif controller.buttonR2.pressing():
        claw.retract()

while True:
    toggle_claw()
    wait(20, MSEC)
```

## 3. The Quest: The Rapid Launcher ⚔️
1. Create `01_pneumatics_task.py`.
2. Build a mechanism that uses a pneumatic cylinder to "kick" a ball.
3. Use the `Inertial Sensor` to detect when the robot is hit, and trigger the pneumatic kick as an automatic "Counter-attack."
