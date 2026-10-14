
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
blur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow("Blur", blur)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\02_blur.jpg", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
