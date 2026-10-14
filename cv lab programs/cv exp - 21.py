
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
kernel = np.ones((5, 5), np.uint8)
result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow("Opening", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\21_opening.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
