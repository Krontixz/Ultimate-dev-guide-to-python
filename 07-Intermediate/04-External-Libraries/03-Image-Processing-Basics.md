# 📷 Lesson 3: Pillow (The Robot's Eyes)

Before we do "Computer Vision" (Advanced), we need to understand how computers see images. They see them as a massive grid of numbers (Pixels).

## 1. The 5-Year-Old Spark ⚡
If you look really closely at a TV screen, you see tiny dots of Red, Green, and Blue. A computer sees an image as a giant spreadsheet where every cell tells it exactly what color that dot should be.



## 2. The Deep Dive 🤿
We use the `Pillow` (PIL) library to open, resize, and flip images.

```python
from PIL import Image

# Open a photo of your robot
img = Image.open("robot.jpg")

# Get info
print(f"Size: {img.size}") # Width and Height

# Edit the image
gray_img = img.convert("L") # Turn it black and white
gray_img.save("robot_bw.jpg")

# Resize for faster processing
small_img = img.resize((100, 100))
small_img.show()
```

## 3. The Quest: Thumbnail Maker ⚔️
1. Install the library: `pip install Pillow`.
2. Create `03_image_task.py`.
3. Take any image on your computer and write a script that:
   * Flips it upside down.
   * Prints the "Format" of the image (PNG, JPEG, etc.).
   * Saves it as `modified_image.png`.
