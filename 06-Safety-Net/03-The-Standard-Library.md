# 🧰 Lesson 3: The Standard Library (Built-in Power)

Python comes with "Batteries Included." This means there are hundreds of professional tools already installed—you just have to ask for them.

## 1. The 5-Year-Old Spark ⚡
Imagine you bought a toolkit. You know how to use the hammer and screwdriver, but you didn't realize there was a hidden compartment with a laser level and a GPS inside. The **Standard Library** is that hidden compartment.

## 2. The Deep Dive 🤿
Here are the most important modules for VEX and NASA:
* **`math`:** For advanced trigonometry (angles for robot arms).
* **`random`:** For simulating unpredictable environments.
* **`time`:** For adding delays (e.g., `time.sleep(1)` to wait 1 second).
* **`os`:** For interacting with the computer's files.

```python
import math
import time

print("Calculating trajectory...")
time.sleep(2) # Wait 2 seconds
print(f"The Square Root of 144 is {math.sqrt(144)}")
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
import random
num = random.randint(1, 10)
```

**C:**
```c
#include <stdlib.h>
#include <time.h>
srand(time(NULL));
int num = rand() % 10 + 1;
// Python makes generating random numbers much simpler!
```

## 4. The Quest: Timed Launch ⚔️
Create a file named `03_library_task.py`.
1. Import `time` and `math`.
2. Print "Searching for exoplanet..."
3. Use `time.sleep(3)` to make the program wait.
4. Calculate the floor of `3.99` using `math.floor()`.
5. Print: "Exoplanet found in Sector [Result]!"

---
*End of Phase 6: The Safety Net.*
