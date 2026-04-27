# 🔄 Lesson 3: The While Loop (The Heartbeat)

In robotics, your program shouldn't just run once and stop. It needs to keep checking sensors and moving motors forever. This is where the `while` loop comes in.

## 1. The 5-Year-Old Spark ⚡
Imagine your mom tells you: "**While** you are hungry, keep eating." You take a bite, check if you're still hungry, and take another bite. You only stop when "hungry" becomes `False`.

## 2. The Deep Dive 🤿
A `while` loop repeats as long as a condition is `True`. 

**The Infinite Loop:** In VEX or NASA rovers, we often use `while True:`. This creates a loop that never ends, which is perfect for a robot that needs to stay "awake" and listen for commands.

```python
while True:
    print("Monitoring sensors...")
    # This will print forever until you stop the program!
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
while power > 0:
    power -= 1
```

**JavaScript:**
```javascript
while (power > 0) {
    power--;
}
```

## 4. The Quest: Countdown to Launch ⚔️
Create a file named `03_while_task.py`.
1. Create a variable `countdown` and set it to `10`.
2. Use a `while` loop to print the countdown number.
3. Inside the loop, subtract `1` from the countdown each time.
4. When the loop finishes, print "Blast off! 🚀"

---
*Next Lesson: 04-For-Loops.md*
