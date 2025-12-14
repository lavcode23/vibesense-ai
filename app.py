import streamlit as st
import cv2
from utils.face_utils import extract_face_features
from utils.vibe_logic import infer_vibe

st.set_page_config(
    page_title="VibeSense AI",
    layout="centered"
)

st.title("🧠 VibeSense AI")
st.caption("Real-time Human State Detection")

run = st.checkbox("▶ Start Camera")

FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.warning("Camera not accessible")
            break

        features = extract_face_features(frame)

        if features:
            vibe, confidence = infer_vibe(features)
            st.markdown(f"### {vibe}")
            st.progress(confidence)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

    cap.release()
import streamlit as st
import cv2
from utils.face_utils import extract_face_features
from utils.vibe_logic import infer_vibe

st.set_page_config(
    page_title="VibeSense AI",
    layout="centered"
)

st.title("🧠 VibeSense AI")
st.caption("Real-time Human State Detection")

run = st.checkbox("▶ Start Camera")

FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.warning("Camera not accessible")
            break

        features = extract_face_features(frame)

        if features:
            vibe, confidence = infer_vibe(features)
            st.markdown(f"### {vibe}")
            st.progress(confidence)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

    cap.release()
