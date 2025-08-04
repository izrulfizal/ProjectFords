import cv2
import pytesseract
import re
import time
from speech_local import speak_mac


staff_db = {
    "NU1919": "Mr. Izrul",
}


cap = cv2.VideoCapture(0)

print("Show your NU staff card to the webcam. Press 'q' to quit.")

greeted_ids = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize if needed
    # frame = cv2.resize(frame, (640, 480))

 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)

   
    text = pytesseract.image_to_string(thresh)

    
    match = re.search(r'NU\d{4}', text)
    if match:
        staff_id = match.group(0)
        if staff_id in staff_db and staff_id not in greeted_ids:
            name = staff_db[staff_id]
            speak_mac(f"Hello, {name}!")
            greeted_ids.add(staff_id)
            time.sleep(2)


    cv2.imshow("Staff ID Scanner", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
