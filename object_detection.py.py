import cv2

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        cv2.imwrite("static/capture.jpg", frame)
        return "Image Captured"
    return "Capture Failed"


def detect_objects():
    # Basic placeholder detection (can upgrade to YOLO)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return "Camera Error"

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Simple face detection (demo purpose)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    result = []

    for (x, y, w, h) in faces:
        result.append("Person detected")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imwrite("static/capture.jpg", frame)

    if len(result) == 0:
        return "No object detected"

    return ", ".join(result)