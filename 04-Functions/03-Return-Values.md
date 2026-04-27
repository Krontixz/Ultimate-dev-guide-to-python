# 📤 Lesson 3: Return Values

A function doesn't just have to *do* things; it can also *calculate* things and give the answer back to you. This is called a **Return**.

## 1. The 5-Year-Old Spark ⚡
Imagine you give a friend two numbers and ask, "What's the total?" Your friend does the math in their head and then hands you a piece of paper with the answer. That piece of paper is the **Return Value**.

## 2. The Deep Dive 🤿
We use the `return` keyword. Once a function returns something, it stops running immediately.

```python
def calculate_weight_on_mars(earth_weight):
    return earth_weight * 0.38

my_mars_weight = calculate_weight_on_mars(150)
print(f"On Mars, I would weigh {my_mars_weight} lbs.")
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
def get_status():
    return "OK"
```

**Java:**
```java
public String getStatus() {
    return "OK";
}
// In Java, you have to declare that you are returning a "String".
// Python is smart enough to know what it is.
```

## 4. The Quest: The Math Specialist ⚔️
Create a file named `03_return_task.py`.
1. Create a function called `calc_battery_life`.
2. It should take two arguments: `current_voltage` and `drain_rate`.
3. Return the result of `current_voltage / drain_rate`.
4. Call the function and print: "Estimated time remaining: [Result] hours."

---
*End of Phase 4: Functions.*
