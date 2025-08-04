import cv2
import pytesseract
import re
import time
from speech_local import speak_mac
from main import main  # 👈 import the assistant interaction
import os

# Staff database
staff_db = {
    "NU1919": "Mr. Izrul",
}

# Face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
greeted_ids = set()
face_prompted = False

print("AI Assistant Scanner is running...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 1. If face detected, prompt for ID
    if len(faces) > 0 and not face_prompted:
        speak_mac("Please show your staff ID card.")
        face_prompted = True
        time.sleep(2)

    # 2. OCR for ID
    if face_prompted:
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        _, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
        text = pytesseract.image_to_string(thresh)

        match = re.search(r'NU\d{4}', text)
        if match:
            staff_id = match.group(0)
            if staff_id in staff_db and staff_id not in greeted_ids:
                name = staff_db[staff_id]
                speak_mac(f"Hello, {name}!")
                time.sleep(1)
                greeted_ids.add(staff_id)
                face_prompted = False  # Reset for next user
                # cap.release()
                # cv2.destroyAllWindows()
                main()  # 👈 Start assistant chat
                break

    # Show webcam
    cv2.imshow("Staff ID Scanner", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
