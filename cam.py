import cv2

def shot():
    cap = cv2.VideoCapture(0)

    for i in range(30):
        cap.read()

    ret, frame = cap.read()

    cv2.imwrite("cam.png", frame)

    cap.release()

if __name__ == "__main__":
    shot()
