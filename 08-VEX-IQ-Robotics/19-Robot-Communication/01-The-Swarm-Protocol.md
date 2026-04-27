# 📡 Lesson 19: Communication (Teamwork)

In some advanced competitions, you might have two robots on the field. If they can "talk," they can coordinate. One robot can say "I have the ball!" so the other robot moves out of the way.

## 1. The 5-Year-Old Spark ⚡
It’s like playing soccer. If you don't talk to your teammates, you will all run for the ball at the same time and bump heads. If you shout "I got it!", your teammate can go stand by the goal to wait for a pass.



## 2. The Deep Dive 🤿
VEX IQ can use the `radio` or `link` modules to send small packets of data between two Brains.

```python
# Setup a link with a specific ID
robot_link = Link("TEAM_1234_LINK")

def sync_data():
    # Send our current X, Y position to our partner
    message = f"{curr_x},{curr_y}"
    robot_link.send(message)

# On the OTHER robot
def receive_data(msg):
    partner_x, partner_y = msg.split(",")
    # Logic to avoid driving into the partner's spot
```

## 3. The Quest: The Shadow ⚔️
1. Create `19_comm_task.py`.
2. This requires two VEX Brains.
3. Make "Robot A" send its joystick position to "Robot B."
4. "Robot B" should mirror the movements of "Robot A" perfectly with zero wires connected!
