import cv2
import os

target_kb = int(input("Enter target size (KB): "))

img = cv2.imread(r"D:\mohit\python for AIML\download.jpg")
scale = 1.0

while True:
    resized = cv2.resize(img, (0, 0), fx=scale, fy=scale)
    cv2.imwrite("output.jpg", resized)

    size_kb = os.path.getsize("output.jpg") / 1024

    if size_kb <= target_kb:
        print("Done!")
        print(f"Final Size: {size_kb:.2f} KB")
        break

    scale -= 0.1