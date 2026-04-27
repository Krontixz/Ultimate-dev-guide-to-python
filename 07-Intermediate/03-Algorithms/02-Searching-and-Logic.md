# 🔍 Lesson 2: Searching (Finding the Needle)

Once your data is sorted, or even if it isn't, you need to be able to find specific information quickly. If a robot is looking for a "Red Ball" in a list of 100 objects, it needs a search strategy.

## 1. The 5-Year-Old Spark ⚡
If you are looking for your favorite book on a shelf, you don't look at every single book one by one if you already know it's a blue book. You "filter" your eyes to only see blue. Searching in Python is like using a magnifying glass to find exactly what you need.

## 2. The Deep Dive 🤿
We use the `in` keyword for simple searches, and "List Comprehensions" for advanced filtering.

```python
inventory = ["Gear", "Motor", "Sensor", "Cable"]

# Simple Search
if "Sensor" in inventory:
    print("Parts available for build.")

# Advanced Filtering (Finding all numbers over 50)
sensor_readings =
high_readings = [num for num in sensor_readings if num > 50]

print(f"Danger levels detected at: {high_readings}")
```

## 3. The Quest: Object Detector ⚔️
Create a file named `02_search_task.py`.
1. Create a list of objects: `["Red Ball", "Blue Cube", "Red Pyramid", "Green Sphere"]`.
2. Use a loop or a list comprehension to find only the objects that have the word "Red" in them.
3. Print the new list: `["Red Ball", "Red Pyramid"]`.
