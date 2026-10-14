
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)

cv2.imshow("Equalized Image", equalized)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\04_equalized.jpg", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
