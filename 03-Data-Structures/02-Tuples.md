# 🔒 Lesson 2: Tuples (Fixed Data)

A Tuple is similar to a list, but with one major difference: it is **Immutable**. Once it is created, it cannot be changed.

## 1. The 5-Year-Old Spark ⚡
A Tuple is like a message written in stone. You can read it, but you can't erase words or add new ones. This is perfect for things that *should* stay the same, like the coordinates of a landing site.

## 2. The Deep Dive 🤿
Tuples use parentheses `()` instead of square brackets `[]`. 

**Why use a Tuple instead of a List?**
1. **Safety:** You can't accidentally overwrite important mission data.
2. **Speed:** Python processes tuples slightly faster than lists because their size is fixed in memory.

```python
landing_coords = (28.57, -80.64) # Latitude and Longitude
```

## 3. Side-by-Side Mirror 🪞

**Python:**
```python
const_data = (3.14, 9.8)
# const_data = 5  <-- This would cause an ERROR!
```

**JavaScript:**
```javascript
const data = [3.14, 9.8];
// JS 'const' prevents reassignment of the variable, 
// but you can often still change the items inside! 
```

## 4. The Quest: Satellite Constants ⚔️
Create a file named `02_tuple_task.py`.
1. Create a tuple called `earth_specs` with two numbers: `6371` (Radius) and `5.97` (Mass).
2. Try to change the first number to `7000` and watch Python block you.
3. Comment out the error line and print the tuple.

---
*Next Lesson: 03-Dictionaries.md*
