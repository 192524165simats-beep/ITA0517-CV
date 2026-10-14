
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
colors = ("b", "g", "r")

for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

plt.title("Color Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.savefig(r"C:\Users\harsh\OneDrive\Desktop\CV\05_histogram.png")
plt.show()
