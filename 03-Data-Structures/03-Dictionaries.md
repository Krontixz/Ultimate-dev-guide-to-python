# 📖 Lesson 3: Dictionaries (Key-Value Pairs)

Dictionaries allow you to label your data. Instead of remembering that "Index 0" is the battery, you can just ask for the `"battery"`.

## 1. The 5-Year-Old Spark ⚡
Imagine a real dictionary. You don't count pages to find a word; you look up the "Key" (the word) to find the "Value" (the definition). 

## 2. The Deep Dive 🤿
Dictionaries use curly braces `{}`. They are the standard way to handle "Telemetry" (data sent from a robot to a computer).

```python
rover_status = {
    "battery": 92,
    "temp": 24.5,
    "online": True
}

print(rover_status["battery"]) # Output: 92
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
robot = {"id": 101}
```

**JSON (Space Industry Standard):**
```json
{
  "id": 101
}
```
*Python dictionaries are almost identical to JSON, which is how satellites talk to ground control.*

## 4. The Quest: Rover Telemetry ⚔️
Create a file named `03_dict_task.py`.
1. Create a dictionary called `telemetry`.
2. Add keys for `"altitude"`, `"velocity"`, and `"fuel"`.
3. Update the `"fuel"` value to a lower number.
4. Add a new key `"mission_status"` and set it to `"Active"`.
5. Print the formatted dictionary.

---
*End of Phase 3: Data Structures.*
