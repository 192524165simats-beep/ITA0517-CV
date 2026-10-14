
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
kernel = np.ones((3, 3), np.uint8)
result = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Morphological Dilation", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\20_morph_dilation.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
