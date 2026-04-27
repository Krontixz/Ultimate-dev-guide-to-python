# 🛡️ Lesson 1: Error Handling (Try / Except)

Error handling is how we prevent our program from "dying" when something unexpected happens. We call this "failing gracefully."

## 1. The 5-Year-Old Spark ⚡
Imagine you are a robot instructed to "Go through the door." If the door is locked, a dumb robot will just keep hitting its head against the door until its motor burns out. A smart robot will **Try** to open the door, and if it **Excepts** (finds) a lock, it will stop and alert the human instead of crashing.

## 2. The Deep Dive 🤿
In Python, we use the `try` and `except` blocks.
* **Try:** The code you *hope* will work.
* **Except:** The code that runs only if an error happens.

```python
try:
    number = int(input("Enter a divisor: "))
    result = 100 / number
    print(f"Result is {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero! Mission aborted safely.")
except ValueError:
    print("Error: That wasn't a number!")
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
try:
    # code
except Exception as e:
    print(e)
```

**C++:**
```cpp
try {
    // code
} catch (const std::exception& e) {
    std::cerr << e.what();
}
// Very similar logic, but Python's syntax is much lighter.
```

## 4. The Quest: Sensor Recovery ⚔️
Create a file named `01_error_task.py`.
1. Create a dictionary called `sensors` with `{"temp": 25}`.
2. Wrap a piece of code in a `try` block that tries to print `sensors["radiation"]` (which doesn't exist).
3. Use an `except KeyError:` block to print "Warning: Radiation sensor not found. Continuing with backup sensors."

---
*Next Lesson: 02-Custom-Modules.md*
