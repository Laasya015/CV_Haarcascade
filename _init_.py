from .detectors.face import detect_face
from .detectors.eyes import detect_eyes
from .detectors.left_eye import detect_left_eye
from .detectors.right_eye import detect_right_eye
from .detectors.smile import detect_smile
from .detectors.full_body import detect_full_body
from .detectors.upper_body import detect_upper_body
from .detectors.number_plate import detect_number_plate

__all__ = [
    "detect_face",
    "detect_eyes",
    "detect_left_eye",
    "detect_right_eye",
    "detect_smile",
    "detect_full_body",
    "detect_upper_body",
    "detect_number_plate"
]
