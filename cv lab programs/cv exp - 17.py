
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
result = img.copy()

cv2.putText(result, "CV LAB", (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Watermark", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\17_watermark.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
