# 🛤️ Lesson 2: The If Statement

The `if` statement is the most important tool in programming. it allows the code to branch. If "A" is true, do this; otherwise, do that.

## 1. The 5-Year-Old Spark ⚡
Imagine you are walking. **If** there is a puddle in front of you, you jump over it. **Else**, you just keep walking normally. You only jump if the condition (the puddle) is there.

## 2. The Deep Dive 🤿
Python uses **Indentation** (whitespace) to know which code belongs to the `if` statement.

```python
if battery < 20:
    print("Warning: Low Battery!") # This only runs if battery is < 20
print("System Check Complete.")   # This runs no matter what
```

* **elif:** Short for "else if." Use this to check multiple conditions.
* **else:** The "catch-all." If none of the above are true, do this.

## 3. Side-by-Side Mirror 🪞

**Python (Clean):**
```python
if temperature > 100:
    print("Too hot!")
```

**C++ (Uses Brackets):**
```cpp
if (temperature > 100) {
    std::cout << "Too hot!";
}
// C++ uses { } to group code. Python uses 4 spaces (Tab).
```

## 4. The Quest: Shield Logic ⚔️
Create a file named `02_if_task.py`.
1. Ask the user to input the `shield_energy` level (0 to 100).
2. If energy is `100`, print "Shields at maximum."
3. If energy is between `50` and `99`, print "Shields stable."
4. If energy is below `50`, print "Warning: Emergency Power!"

---
*Next Lesson: 03-While-Loops.md*
