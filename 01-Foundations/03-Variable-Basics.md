# 📦 Lesson 3: Variable Basics

Before a robot can move, it needs to remember things—like its speed, its name, or how much battery it has left. We use **Variables** to store this information.

## 1. The 5-Year-Old Spark ⚡
Imagine you have a row of empty boxes. You put a piece of paper inside one that says `100`, and on the outside of the box, you write the word `Speed`. Whenever you ask the computer for "Speed," it looks in that box and tells you `100`.

## 2. The Deep Dive 🤿
In Python, creating a variable is called **Assignment**. We use the `=` sign to assign a value to a name.

**Rules for Naming Variables:**
* Must start with a letter or underscore (`_`).
* Cannot start with a number.
* Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
* **Case-sensitive:** `Battery` and `battery` are two different boxes!

## 3. Side-by-Side Mirror 🪞

**Python (Clean):**
```python
power_level = 80
```

**C++ (Strict):**
```cpp
int power_level = 80; 
// In C++, you MUST say 'int' to prove it's a whole number. 
// Python figures it out for you!
```

## 4. The Quest: Rover Specs ⚔️
Create a file named `03_variable_task.py`. 
1. Create a variable called `rover_name` and set it to a string (e.g., "Discovery").
2. Create a variable called `max_speed` and set it to a number.
3. Use `print()` to show the name and speed on the screen.

---
*Next Lesson: 04-Numbers-And-Math.md*
