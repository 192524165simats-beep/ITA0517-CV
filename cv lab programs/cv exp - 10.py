
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
result = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Rotated 90", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\10_rotate90.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
