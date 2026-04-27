# 📡 Lesson 1: Kalman Filters (Sensor Fusion)

Sometimes the Distance Sensor gives a "fake" reading because it hit a weird angle. A **Kalman Filter** is a mathematical way to guess the "Truth" by combining what the sensor says with what the motors are doing.

## 1. The 5-Year-Old Spark ⚡
Imagine you are walking and close your eyes. You "guess" you’ve moved 5 feet. Then you open your eyes and see you’ve moved 6 feet. You combine your "guess" and your "sight" to know exactly where you are.

## 2. The Deep Dive 🤿
We use a weighted average. If we trust the "Prediction" (Math) 70% and the "Measurement" (Sensor) 30%, we get a much smoother result.

```python
estimated_dist = 0
prediction_weight = 0.7

def update_estimate(sensor_reading, motor_speed, dt):
    global estimated_dist
    # Predict where we SHOULD be
    predicted_dist = estimated_dist + (motor_speed * dt)
    
    # Update based on actual sensor measurement
    estimated_dist = (prediction_weight * predicted_dist) + ((1 - prediction_weight) * sensor_reading)
    return estimated_dist
```

## 3. The Quest: The Ghost Wall ⚔️
1. Create `01_filter_task.py`.
2. Move your hand quickly in front of the sensor to create "spiky" data.
3. Print the raw sensor data vs. the filtered data.
4. Notice how the filtered data doesn't "jump" as much!
