
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
kernel = np.ones((5, 5), np.uint8)
result = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Erosion", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\06_erosion.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
