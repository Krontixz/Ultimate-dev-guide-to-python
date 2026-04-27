# 📦 Lesson 2: Custom Modules (Multi-File Projects)

Professional code is never just one giant file. NASA's software has millions of files. We use **Modules** to split our code into organized pieces.

## 1. The 5-Year-Old Spark ⚡
Imagine your room is your project. If you put your clothes, your toys, and your schoolbooks all in one giant pile, you'll never find anything. A module is like a "Drawer." You put all the "Movement" code in one drawer and all the "Math" code in another.

## 2. The Deep Dive 🤿
Any `.py` file can be a module. You use the `import` keyword to bring code from one file into another.

**File: `robot_tools.py`**
```python
def beep():
    print("Beep boop!")
```

**File: `main.py`**
```python
import robot_tools

robot_tools.beep()
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
import math
```

**C++:**
```cpp
#include <cmath>
// Python 'imports' the library at runtime. 
// C++ 'includes' the code physically before it compiles.
```

## 4. The Quest: Modular Rover ⚔️
1. Create a file named `engine.py`. Inside, define a function `start_engine()` that prints "Vroom!"
2. Create a second file named `main_mission.py`.
3. Import `engine` and call `start_engine()`.

---
*Next Lesson: 03-The-Standard-Library.md*
