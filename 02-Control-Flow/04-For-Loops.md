# 🎡 Lesson 4: The For Loop

While the `while` loop runs until a condition changes, the `for` loop is used when you want to repeat an action for every item in a list or a specific number of times.

## 1. The 5-Year-Old Spark ⚡
Imagine you have a bag of 5 apples. A `for` loop is like reaching into the bag, taking one apple, polishing it, and putting it down—then repeating that until the bag is empty. You know exactly how many times you will act.

## 2. The Deep Dive 🤿
In Python, we often use the `range()` function with a for loop to count.

```python
for i in range(5):
    print("Rotation number:", i)
```
* `range(5)` creates a sequence from 0 to 4.
* The loop runs **5 times**.
* This is perfect for moving a VEX robot arm a specific number of degrees or sending a signal to 3 different satellites.

## 3. Side-by-Side Mirror 🪞

**Python (Elegant):**
```python
for i in range(10):
    print(i)
```

**C++ (The "Standard" Loop):**
```cpp
for(int i = 0; i < 10; i++) {
    printf("%d\n", i);
}
// C++ requires you to set the start, the end, and the "step" manually.
```

## 4. The Quest: Satellite Scan ⚔️
Create a file named `04_for_task.py`.
1. Use a `for` loop and `range()` to simulate a satellite scanning 8 sectors of space.
2. For every sector, print: "Scanning Sector [Number]..."
3. After the loop ends, print: "Scan Complete. No aliens found."

---
*Next Lesson: 05-Logical-Operators.md*
