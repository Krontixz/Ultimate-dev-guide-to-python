# 📥 Lesson 2: Arguments (Inputs)

Functions become "smart" when you can give them information to work with. These inputs are called **Arguments**.

## 1. The 5-Year-Old Spark ⚡
Think of a microwave. The microwave is a **Function**. But you have to tell it *what* to cook (an argument) and for *how long* (another argument). Without arguments, the microwave wouldn't know if it's heating up pizza or popcorn!

## 2. The Deep Dive 🤿
Arguments go inside the parentheses. You can have one, many, or none.

```python
def set_thrusters(power_level):
    print(f"Adjusting thrusters to {power_level}%")

set_thrusters(50)  # "50" is the argument
set_thrusters(100) # "100" is the argument
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
def move(speed, direction):
    # Python handles any data type here automatically.
```

**C++ (NASA/Hardware Standard):**
```cpp
void move(int speed, string direction) {
    // You MUST tell C++ exactly what data type each argument is.
}
```

## 4. The Quest: Command Center ⚔️
Create a file named `02_args_task.py`.
1. Create a function called `send_message` that takes two arguments: `username` and `message_text`.
2. Inside, print: "[username] says: [message_text]".
3. Call the function three times with different names and messages.

---
*Next Lesson: 03-Return-Values.md*
