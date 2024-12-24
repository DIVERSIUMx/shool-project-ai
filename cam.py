import cv2

cap = cv2.VideoCapture(2)

for i in range(30):
    cap.read()

ret, frame = cap.read()

cv2.imwrite("cam.png", frame)

cap.release()
