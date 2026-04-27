# 📋 Lesson 1: Lists (The Inventory)

A List is an ordered collection of items. In robotics, we use lists to store sequences—like a series of waypoints for a drone or a queue of motor commands.

## 1. The 5-Year-Old Spark ⚡
Imagine a train with several cars. Each car holds something different—one has a robot arm, one has a battery, and one has a camera. You can add new cars to the end of the train, remove cars, or look inside a specific car by counting from the front.

## 2. The Deep Dive 🤿
Lists in Python are **Mutable**, meaning you can change them after they are created. They are indexed starting at **0**.

```python
# Creating a list
tools = ["Wrench", "Screwdriver", "Multimeter"]

# Accessing by index
print(tools)  # Output: Wrench

# Adding items
tools.append("Soldering Iron")
```

**Memory Note:** Python lists are dynamic. Unlike C++, you don't have to tell the computer how big the list will be ahead of time; Python expands the memory automatically as you add items.

## 3. Side-by-Side Mirror 🪞

**Python (Dynamic):**
```python
sensors = ["Gyro", "Lidar"]
sensors.append("GPS") 
```

**C++ (Static Array):**
```cpp
string sensors = {"Gyro", "Lidar"};
sensors = "GPS";
// In C++, you usually have to define the size (3) at the start!
```

## 4. The Quest: Waypoint Navigation ⚔️
Create a file named `01_list_task.py`.
1. Create a list called `waypoints` containing three strings: `"Base"`, `"Crater"`, and `"Mountain"`.
2. Add a fourth destination, `"Valley"`, to the end of the list using `.append()`.
3. Change the second item (`"Crater"`) to `"Deep_Crater"`.
4. Print the entire list and then print the length of the list using `len()`.

---
*Next Lesson: 02-Tuples.md*
