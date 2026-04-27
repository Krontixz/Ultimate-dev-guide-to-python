# 📊 Lesson 2: Statistics (Filtering Sensor Noise)

Real-world sensors are "noisy." If a robot is standing still, a distance sensor might jump between 10.1cm and 9.9cm. We use statistics to find the "Truth."

## 1. The 5-Year-Old Spark ⚡
Imagine five friends guess how many jellybeans are in a jar. One might guess way too high, but if you take the **Average**, you'll be much closer to the right answer.

## 2. The Deep Dive 🤿
The `statistics` module helps us clean up messy data.
* **mean():** The average.
* **median():** The middle number. This is the "shield" against glitches, because it ignores extreme high/low spikes.

```python
import statistics

# Messy readings from a sensor
readings = [12.2, 12.1, 11.9, 12.5, 12.1]

# Using median to find the most stable center point
filtered_val = statistics.median(readings) 
print(f"Filtered Sensor Reading: {filtered_val}")
```

## 3. The Quest: Sensor Filter ⚔️
Create a file named `02_stats_task.py`.
1. Create a list called `sonar_data` with 10 numbers close to 100.
2. Add one "Glitch" number like `999` to the list.
3. Calculate the `mean` and the `median` using the `statistics` module. 
4. Print both. Notice how the `median` ignores the glitch while the `mean` gets ruined by it!
