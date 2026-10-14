
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
result = cv2.resize(img, (300, 300))

cv2.imshow("Resized Image", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\09_resized.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
