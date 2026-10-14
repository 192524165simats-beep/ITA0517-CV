
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
result = cv2.convertScaleAbs(abs(x) + abs(y))

cv2.imshow("Sobel Edges", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\16_sobel.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
