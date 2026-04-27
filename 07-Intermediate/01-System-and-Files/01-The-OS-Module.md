# 🖥️ Lesson 1: The OS Module (System Control)

In intermediate programming, your script needs to know about the world outside of Python. The `os` module allows you to talk to your computer's operating system.

## 1. The 5-Year-Old Spark ⚡
Imagine your Python script is a person inside a house. The `os` module is like the person opening the windows, checking which room they are in, or creating a new closet to store toys. It lets the script interact with the "House" (the computer).

## 2. The Deep Dive 🤿
The `os` module is essential for robotics because you often need to check if a data folder exists or get the "Path" to a configuration file.

```python
import os

# Get the current folder you are working in
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# List all files in the current folder
files = os.listdir()
print(f"Files found: {files}")

# Create a new folder for Robot Logs
if not os.path.exists("logs"):
    os.makedirs("logs")
```

## 3. The Quest: Directory Scout ⚔️
Create a file named `01_os_task.py`.
1. Import the `os` module.
2. Print the name of your operating system (use `os.name`).
3. Create a new folder called `Mission_Data`.
4. Inside that folder, create a sub-folder called `Snapshots`.

---
*Next Lesson: 02-File-IO.md*
