# 🏗️ Lesson 1: Classes and Objects (The Blueprint)

In the real world, a robot isn't just a variable; it is a "thing" that has data (properties) and can do things (actions). In Python, we use **Classes** to define these things.

## 1. The 5-Year-Old Spark ⚡
Imagine you have a cookie cutter. The cookie cutter is the **Class**. It’s not a cookie itself, but it’s the shape and the plan. The actual cookies you bake are the **Objects**. Every cookie has the same shape, but one might have sprinkles (data) and another might have chocolate chips.

## 2. The Deep Dive 🤿
A **Class** wraps variables and functions together into one package.
* **Attributes:** Variables inside a class (e.g., `color`, `battery_level`).
* **Methods:** Functions inside a class (e.g., `drive()`, `scan()`).

```python
class Satellite:
    def __init__(self, name):
        self.name = name
        self.status = "Orbiting"

# Creating an 'Instance' of the class
my_sat = Satellite("Hubble")
print(my_sat.name) # Output: Hubble
```

## 3. Side-by-Side Mirror 🪞

**Python (Clean):**
```python
class Robot:
    def __init__(self):
        self.type = "Drone"
```

**C++ (Heavy):**
```cpp
class Robot {
  public:
    string type;
    Robot() {
      type = "Drone";
    }
};
// C++ requires 'public' keywords and semicolons everywhere.
```

## 4. The Quest: Rover Factory ⚔️
Create a file named `01_class_task.py`.
1. Create a class called `Rover`.
2. Inside the `__init__` method, give it a `model` and a `battery` (set battery to 100).
3. Create two different objects: `rover1` (model "Explorer") and `rover2` (model "Tank").
4. Print the models of both rovers.

---
*Next Lesson: 02-Methods.md*
