# 🗂️ Lesson 1: Sorting and Priorities

In robotics, you often have a list of tasks or targets. You need to know which one is the most important or the closest. Sorting allows your robot to organize its "thoughts" before it acts.

## 1. The 5-Year-Old Spark ⚡
Imagine you have a messy pile of toy cars. If you want to find the fastest one, you line them up from slowest to fastest. Sorting in Python is just lining up your data so the most important piece is always at the front of the line.



## 2. The Deep Dive 🤿
Python uses a very fast built-in tool called `sort()` for lists. You can sort numbers, words, or even complex "Dictionaries" (like a list of robot targets).

* **.sort():** Changes the original list to be in order.
* **sorted():** Creates a *new* ordered list without touching the original.
* **Reverse:** You can sort from highest to lowest by using `reverse=True`.

```python
# Sorting simple numbers (Distances to objects)
distances = [45.2, 10.5, 99.0, 5.1]
distances.sort() 
print(f"Closest object is: {distances} units away")

# Sorting a list of Dictionaries (Pro Level)
# Let's say we have targets with different 'threat' levels
targets = [
    {"name": "Drone A", "threat": 5},
    {"name": "Drone B", "threat": 9},
    {"name": "Drone C", "threat": 2}
]

# Sort by threat level (Highest to Lowest)
targets.sort(key=lambda x: x["threat"], reverse=True)
print(f"Highest Priority Target: {targets['name']}")
```

## 3. The Quest: Task Manager ⚔️
Create a file named `01_sort_task.py`.
1. Create a list of 5 numbers representing "Battery Levels" of different robots.
2. Sort them from **Lowest to Highest** (so you know which robot needs a charger first).
3. Create a second list of names: `["Rover", "Drone", "Submarine"]`.
4. Sort them alphabetically and print the result.
