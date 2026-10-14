
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
result = img.copy()
h, w = result.shape[:2]

cv2.circle(result, (w//2, h//2), min(w, h)//4, (0, 0, 255), 3)

cv2.imshow("Circle", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\34_circle.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
