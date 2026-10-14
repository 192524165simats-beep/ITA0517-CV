
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
result = img.copy()
h, w = result.shape[:2]
s = 60

cv2.rectangle(result, (0, 0), (s, s), (0, 0, 255), -1)
cv2.rectangle(result, (w-s, 0), (w, s), (0, 255, 0), -1)
cv2.rectangle(result, (0, h-s), (s, h), (255, 0, 0), -1)
cv2.rectangle(result, (w-s, h-s), (w, h), (0, 255, 255), -1)

cv2.imshow("Corner Boxes", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\32_corner_boxes.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
