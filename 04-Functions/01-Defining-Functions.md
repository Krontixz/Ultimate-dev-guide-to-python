# 🛠️ Lesson 1: Defining Functions

A **Function** is a saved block of code that you can "call" whenever you need it. Think of it as a custom command you've added to Python.

## 1. The 5-Year-Old Spark ⚡
Imagine you have a pet robot. Instead of telling it: "Lift left leg, move it forward, put it down, lift right leg..." every single time you want it to move, you just teach it one word: **Walk**. A function is that one word that triggers a whole list of pre-saved instructions.

## 2. The Deep Dive 🤿
We use the `def` keyword to "define" a function. 

**The Golden Rules:**
1. Use `def` followed by the function name.
2. Always end the name with parentheses `()` and a colon `:`.
3. **Indentation Matters:** Everything indented under the `def` is part of that function.

```python
def system_startup():
    print("Core Temperature: Optimal")
    print("Booting Navigation System...")
    print("Welcome, Captain.")

# To run the code, you must "call" the function by name:
system_startup()
```

## 3. Side-by-Side Mirror 🪞

**Python (Clean & Simple):**
```python
def alarm():
    print("Beep!")
```

**JavaScript:**
```javascript
function alarm() {
    console.log("Beep!");
}
// JavaScript uses the word 'function' and curly braces {}.
// Python uses 'def' and whitespace/indentation.
```

## 4. The Quest: Action Commands ⚔️
Create a file named `01_function_task.py`.
1. Define a function called `deploy_landing_gear`.
2. Inside, print: "Unlocking gear locks..." and "Gear Deployed!"
3. Call the function twice (simulating a test run).

---
*Next Lesson: 02-Arguments.md*
