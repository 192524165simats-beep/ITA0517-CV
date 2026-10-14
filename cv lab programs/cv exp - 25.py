
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
h, w = img.shape[:2]

template = img[0:h//4, 0:w//4]
result = img.copy()

match = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
_, _, _, location = cv2.minMaxLoc(match)

th, tw = template.shape[:2]
cv2.rectangle(result, location,
              (location[0] + tw, location[1] + th), (0, 255, 0), 2)

cv2.imshow("Template Matching", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\25_template.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
