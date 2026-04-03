import cv2

def detect_objects():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return "Camera Error"

    cv2.imwrite("static/capture.jpg", frame)
    return "Image Captured"
