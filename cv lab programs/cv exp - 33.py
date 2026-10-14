
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
result = img.copy()
h, w = result.shape[:2]

cv2.rectangle(result, (20, 20), (w-20, h-20), (0, 255, 0), 3)

cv2.imshow("Rectangle", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\33_rectangle.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
