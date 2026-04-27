# 💾 Lesson 2: Databases (Memory That Never Forgets)

Variables in Python disappear when the program stops. A **Database** is a permanent file where your robot can save its history (logs, sensor data, mission maps).

## 1. The 5-Year-Old Spark ⚡
Imagine you have a diary. Every time something happens, you write it down. Even if you go to sleep (turn off the computer), the words are still there when you wake up. A database is a robot's diary.



## 2. The Deep Dive 🤿
We use **SQLite**. It’s perfect because it doesn't require a giant server; it's just a single file that lives in your folder.

```python
import sqlite3

# Connect to the 'diary' file
connection = sqlite3.connect("robot_data.db")
cursor = connection.cursor()

# Create a table for mission logs
cursor.execute("CREATE TABLE IF NOT EXISTS logs (timestamp TEXT, event TEXT)")

# Insert a new log
cursor.execute("INSERT INTO logs VALUES ('12:00PM', 'Robot Started')")

connection.commit()
connection.close()
```

## 3. The Quest: Persistent Logs ⚔️
Create a file named `db_test.py`.
1.  Create a table called `sensor_history`.
2.  Write a script that asks the user for a sensor reading and saves it to the database.
3.  Close the script, run it again, and have it print out *everything* currently saved in the database.
