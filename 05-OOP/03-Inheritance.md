# 🧬 Lesson 3: Inheritance (Family Trees)

Sometimes you want a "Special" version of a robot. Instead of rewriting all the code, you can **Inherit** from an existing class.

## 1. The 5-Year-Old Spark ⚡
Imagine a "Basic Robot" blueprint. It can walk and talk. Now you want a "Chef Robot." You don't start from scratch; you take the "Basic Robot" blueprint and just add a "Cook" button. The Chef Robot *is* a Basic Robot, but with extra skills.

## 2. The Deep Dive 🤿
The new class (Child) gets everything from the old class (Parent).

```python
class BasicBot:
    def beep(self):
        print("Beep!")

class LaserBot(BasicBot): # Inherits from BasicBot
    def fire(self):
        print("Pew Pew!")

rob = LaserBot()
rob.beep() # It can beep!
rob.fire() # It can also fire lasers!
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
class Child(Parent):
```

**Java:**
```java
class Child extends Parent {
}
// Python's syntax is much more direct.
```

## 4. The Quest: Specialized Rovers ⚔️
Create a file named `03_inheritance_task.py`.
1. Create a parent class `Machine` with a method `turn_on()`.
2. Create a child class `Drill` that inherits from `Machine`.
3. Give the `Drill` a method called `spin()`.
4. Create a `Drill` object, turn it on, and make it spin.

---
*End of Phase 5: OOP.*
