
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.convertScaleAbs(gray)

corners = cv2.cornerHarris(gray.astype("float32"), 2, 3, 0.04)
result = img.copy()
result[corners > 0.01 * corners.max()] = [0, 0, 255]

cv2.imshow("Harris Corners", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\15_corners.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
