
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
h, w = img.shape[:2]

src = np.float32([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]])
dst = np.float32([[50, 50], [w-50, 50], [30, h-30], [w-30, h-30]])

matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (w, h))

cv2.imshow("Perspective", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\14_perspective.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
