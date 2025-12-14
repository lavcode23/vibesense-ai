import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

def extract_face_features(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return None

    landmarks = results.multi_face_landmarks[0].landmark

    # Eye openness (very simple but effective)
    left_eye = [landmarks[i] for i in [33, 159]]
    eye_open = abs(left_eye[0].y - left_eye[1].y)

    # Head movement proxy
    nose = landmarks[1]
    head_y = nose.y

    return {
        "eye_open": eye_open,
        "head_y": head_y
    }
