
import cv2

img = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\CV\cv image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = cascade.detectMultiScale(gray, 1.1, 5)
result = img.copy()

for (x, y, w, h) in faces:
    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 255, 0), 2)

count = len(faces)
cv2.putText(result, "Faces: " + str(count), (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

print("Number of faces:", count)

cv2.imshow("Face Count", result)
cv2.imwrite(r"C:\Users\harsh\OneDrive\Desktop\CV\38_face_count.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
