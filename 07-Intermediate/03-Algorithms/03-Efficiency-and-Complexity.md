# ⚡ Lesson 3: Efficiency (Speed Matters)

In a lab, your code can be slow. On a robot, slow code is dangerous. If your robot takes 2 seconds to calculate "Should I stop?", it has already hit the wall. This lesson is about writing "Lean" code.

## 1. The 5-Year-Old Spark ⚡
Imagine you are looking for a specific LEGO piece in a huge bucket.
* **Inefficient:** You pick up every single piece one by one until you find it.
* **Efficient:** You dump the bucket out and only look at the pieces that are the right color.
In Python, we want our "search" to be as fast as dumping the bucket.



## 2. The Deep Dive 🤿
Professional coders talk about **Big O Notation**. This is just a fancy way of saying "How much slower does this get if I add more data?"

* **O(1) - Constant:** The speed never changes (e.g., checking the first item in a list).
* **O(n) - Linear:** If you have 10x more data, it takes 10x more time (e.g., a simple `for` loop).
* **O(n²) - Quadratic:** If you have 10x more data, it takes 100x more time! (e.g., a loop inside a loop). **Avoid these in robotics!**

**Pro-Tip: Use Sets for Speed**
If you are checking if an item exists in a collection, a `set` is thousands of times faster than a `list`.

```python
import time

# Inefficient: Searching a List
huge_list = list(range(1000000))
start = time.perf_counter()
print(999999 in huge_list)
print(f"List Search: {time.perf_counter() - start:.6f} seconds")

# Efficient: Searching a Set
huge_set = set(range(1000000))
start = time.perf_counter()
print(999999 in huge_set)
print(f"Set Search: {time.perf_counter() - start:.6f} seconds")
```

## 3. The Quest: The Speed Test ⚔️
Create a file named `03_speed_test.py`.
1. Create a list of 10,000 numbers.
2. Write a "Nested Loop" (a loop inside a loop) that compares every number to every other number.
3. Time how long it takes using `time.perf_counter()`.
4. Now, try to find a way to do the same task with just one loop. 
5. Notice the massive difference in time!
