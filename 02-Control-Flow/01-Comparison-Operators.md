# ⚖️ Lesson 1: Comparison Operators

Before a computer can make a choice, it needs to compare two things. Is the battery low? Is the sensor touching a wall? We use Comparison Operators to get a `True` or `False` answer.

## 1. The 5-Year-Old Spark ⚡
Imagine you are a bouncer at a club for robots. You have a ruler. If a robot is taller than 5 feet, you let them in. If not, they stay out. You are comparing their `height` to `5`.

## 2. The Deep Dive 🤿
Comparison operators always result in a **Boolean** (`True` or `False`).

**The Logic Symbols:**
* `==` : Equal to (Note the double equals! Single `=` is for assigning, `==` is for asking).
* `!=` : Not equal to.
* `>`  : Greater than.
* `<`  : Less than.
* `>=` : Greater than or equal to.
* `<=` : Less than or equal to.

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
is_full = (fuel == 100)
```

**JavaScript:**
```javascript
let isFull = (fuel === 100); 
// JS often uses three equals (===) to be extra safe. 
// Python keeps it simple with two.
```

## 4. The Quest: Sensor Check ⚔️
Create a file named `01_compare_task.py`.
1. Create a variable `distance_to_wall` and set it to `15`.
2. Create a variable `safe_distance` and set it to `20`.
3. Print the result of: `is_collision_likely = distance_to_wall < safe_distance`.
4. Run the code and see if it tells you `True` or `False`.

---
*Next Lesson: 02-If-Statements.md*
