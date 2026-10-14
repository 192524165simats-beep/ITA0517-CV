
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
result = img.copy()

cv2.putText(result, "Computer Vision", (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Text Image", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\35_text.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
