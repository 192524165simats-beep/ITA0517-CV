
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
h, w = img.shape[:2]
result = img[h//4:3*h//4, w//4:3*w//4]

cv2.imshow("Cropped Image", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\18_cropped.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
