
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

smiles = cascade.detectMultiScale(gray, 1.7, 20)
result = img.copy()

for (x, y, w, h) in smiles:
    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Smile Detection", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\30_smiles.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
