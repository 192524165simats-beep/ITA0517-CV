
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
h, w = img.shape[:2]

src = np.float32([[0, 0], [w-1, 0], [0, h-1]])
dst = np.float32([[50, 50], [w-50, 30], [30, h-50]])

matrix = cv2.getAffineTransform(src, dst)
result = cv2.warpAffine(img, matrix, (w, h))

cv2.imshow("Affine Transformation", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\13_affine.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
