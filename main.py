from typing import Tuple
import cv2
from .detectors.face import detect_face
from .detectors.eyes import detect_eye
from .detectors.left_eye import detect_left_eye
from .detectors.right_eye import detect_right_eye
from .detectors.full_body import detect_full_body
from .detectors.upper_body import detect_upper_body
from .detectors.smile import detect_smile
from .detectors.plate import detect_plate

def main() -> None:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read the frame.")
            break

        # Apply each detection function
        frame, _ = detect_face(frame)
        frame, _ = detect_eye(frame)
        frame, _ = detect_left_eye(frame)
        frame, _ = detect_right_eye(frame)
        frame, _ = detect_full_body(frame)
        frame, _ = detect_upper_body(frame)
        frame, _ = detect_smile(frame)
        frame, _ = detect_plate(frame)

        cv2.imshow('Combined Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
