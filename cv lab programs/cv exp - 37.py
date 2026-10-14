
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([35, 40, 40])
upper = np.array([85, 255, 255])
mask = cv2.inRange(hsv, lower, upper)

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Green Foreground", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\37_green_foreground.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
