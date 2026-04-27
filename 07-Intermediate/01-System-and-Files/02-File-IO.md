# 📂 Lesson 2: File I/O (Read and Write)

"I/O" stands for **Input/Output**. This is how we save data permanently. If your robot shuts down, variables are lost. If you save data to a file, it stays there forever.

## 1. The 5-Year-Old Spark ⚡
If you learn something at school but don't write it in your notebook, you might forget it by tomorrow. Saving to a file is like the robot writing in its notebook so it can read it again later, even after it has been turned off.

## 2. The Deep Dive 🤿
We use the `with open()` statement. This is the "Professional Way" because it automatically closes the file for you, preventing memory leaks.

**Modes:**
* `'w'`: Write (Overwrites everything in the file).
* `'a'`: Append (Adds to the end of the file—perfect for logs).
* `'r'`: Read (Opens the file to look at it).

```python
# Writing to a log
with open("telemetry.txt", "a") as file:
    file.write("Status: Nominal | Battery: 95%\n")

# Reading from a log
with open("telemetry.txt", "r") as file:
    content = file.read()
    print(content)
```

## 3. Side-by-Side Mirror 🪞

**Python (Safe Way):**
```python
with open("test.txt", "w") as f:
    f.write("Hi")
```

**Old Way / Other Languages:**
```python
f = open("test.txt", "w")
f.write("Hi")
f.close() 
# If you forget .close(), the file might get corrupted!
```

## 4. The Quest: Black Box Recorder ⚔️
Create a file named `02_file_task.py`.
1. Ask the user to input a "Mission Objective."
2. Open a file named `mission_log.txt` in **Append** mode.
3. Write the objective to the file with a timestamp (you can just type the date for now).
4. Close the script, run it again, and check the text file to see both entries!

---
*Next Lesson: 03-JSON-Data.md*
