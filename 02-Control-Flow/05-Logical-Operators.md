# 🧠 Lesson 5: Logical Operators (AND, OR, NOT)

Real-world decisions are rarely simple. A NASA lander shouldn't just deploy its parachute if it's "close to the ground"; it should deploy if it's "close to the ground" **AND** its "speed is correct."

## 1. The 5-Year-Old Spark ⚡
Imagine you can go outside only if it is **NOT** raining **AND** you have finished your homework. If even one of those is false, you stay inside.

## 2. The Deep Dive 🤿
We use these operators to combine multiple `if` conditions:

* **`and`**: Returns `True` only if **both** sides are true.
* **`or`**: Returns `True` if **at least one** side is true.
* **`not`**: Flips the result (`True` becomes `False`).

```python
if battery > 20 and connection == True:
    print("Rover is operational.")
```

## 3. Side-by-Side Mirror 🪞

**Python (Literal Words):**
```python
if hungry and tired:
    sleep()
```

**JavaScript / C++ (Symbols):**
```javascript
if (hungry && tired) {
    sleep();
}
// Python uses actual English words, making it much easier to read!
```

## 4. The Quest: Launch Protocol ⚔️
Create a file named `05_logic_task.py`.
1. Create two variables: `fuel_level` (number) and `weather_clear` (boolean).
2. Write an `if` statement that checks if `fuel_level` is greater than 75 **and** `weather_clear` is `True`.
3. If both are true, print: "Launch initiated!"
4. Otherwise, print: "Launch scrubbed. Check systems."

---
*End of Phase 2: Control Flow.*
