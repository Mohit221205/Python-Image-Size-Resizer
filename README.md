# Python Image Size Resizer

A simple and efficient Python utility that dynamically resizes an image down until it meets a user-specified target file size in Kilobytes (KB). It uses OpenCV to iteratively scale down the dimensions of the image until the file size threshold is satisfied.

---

## Features

*   **Target-Driven Compression:** Automatically shrinks the image iteratively to fit an exact file size limit.
*   **Aspect Ratio Preservation:** Uses uniform scaling (`fx` and `fy`) so your images don't stretch or warp.
*   **Real-time Feedback:** Prints the final file size in KB once the compression target is achieved[cite: 1].

---

## Visual Comparison

Here is an example of the utility in action, shrinking a high-resolution image down to a highly compressed target file size.

### Original Image (`download.jpg`)
![Original Image](download.jpg)

### Resized Output (`output.jpg`)
![Resized Output](output.jpg)

---

## Prerequisites

Before running the script, make sure you have the required dependency installed:

```bash
pip install opencv-python
