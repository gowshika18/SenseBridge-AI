import cv2
import easyocr
import requests

# Initialize OCR reader (only once)
reader = easyocr.Reader(['en'])


def detect_number_plate():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return "Camera not working"

    results = reader.readtext(frame)

    detected_plates = []

    for (bbox, text, prob) in results:

        # Filter valid plate-like text
        if len(text) >= 6 and prob > 0.4:
            detected_plates.append(text)

            # Draw bounding box
            (top_left, top_right, bottom_right, bottom_left) = bbox

            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))

            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(frame, text, top_left,
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 255, 0), 2)

            # Optional API call (can remove if not needed)
            try:
                requests.post(
                    "http://localhost:3000/busEntry",
                    json={"bus": text, "status": "ENTRY"}
                )
            except:
                pass

    # Save image to show in frontend
    cv2.imwrite("static/plate.jpg", frame)

    if not detected_plates:
        return "No number plate detected"

    return ", ".join(detected_plates)