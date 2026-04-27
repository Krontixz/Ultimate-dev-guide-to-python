# 🎤 Lesson 5: The Input

A robot that only talks is just a speaker. A robot that *listens* is a computer. We use `input()` to get information from the user.

## 1. The 5-Year-Old Spark ⚡
Imagine your robot stops you and asks, "What is your name?" You tell it, and then the robot remembers it to use later. `input()` is the robot's ears.

## 2. The Deep Dive 🤿
The `input()` function always pauses the program and waits for the user to type something and press Enter.

**CRITICAL NOTE:** Everything received by `input()` comes in as a **String** (text). If you want to use it for math, you have to convert it using `int()` or `float()`.

```python
age = input("How old are you? ")
age_in_ten_years = int(age) + 10  # We must convert to int to do math!
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
name = input("Enter Name: ")
```

**Java:**
```java
Scanner myObj = new Scanner(System.in);
String name = myObj.nextLine();
// Python does in 1 line what Java does in 3!
```

## 4. The Quest: User Authentication ⚔️
Create a file named `05_input_task.py`.
1. Ask the user for their `Pilot Name`.
2. Ask the user for their `Destination`.
3. Print a message saying: "Pilot [Name], we are cleared for landing at [Destination]."

---
*End of Phase 1: Foundations.*
