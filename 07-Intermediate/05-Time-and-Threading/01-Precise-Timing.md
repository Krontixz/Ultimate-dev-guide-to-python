# ⏱️ Lesson 1: Precise Timing (The Heartbeat)

In Phase 1, we used `time.sleep()`. But `sleep` is "Lazy"—it stops everything. For a robot, we need `time.perf_counter()`, which is like a high-speed stopwatch that never stops.

## 1. The 5-Year-Old Spark ⚡
Imagine you are cooking. If you close your eyes and nap for 10 minutes (sleep), you might burn the kitchen down. If you keep your eyes open and look at the clock (perf_counter), you can do other things while you wait for the timer to beep.



## 2. The Deep Dive 🤿
`time.perf_counter()` gives you the time in seconds with incredible precision (nanoseconds). It is used to measure exactly how long a loop takes or to trigger an event every 0.5 seconds without stopping the code.

```python
import time

start_time = time.perf_counter()

# Do a complex calculation
sum(range(1000000))

end_time = time.perf_counter()
duration = end_time - start_time

print(f"Calculation took: {duration:.6f} seconds")
```

## 3. The Quest: The Pulse ⚔️
Create a file named `01_pulse_task.py`.
1. Use a `while` loop.
2. Inside the loop, check the time continuously.
3. Every time 1 second passes, print "Bleep!"
4. **Challenge:** Do NOT use `time.sleep()`. Use an `if` statement to check the difference between the current time and the start time.
