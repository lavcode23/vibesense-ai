import streamlit as st
import cv2
import numpy as np
from PIL import Image

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="VibeSense AI 😎",
    page_icon="😎",
    layout="centered"
)

st.title("😎 VibeSense AI")
st.subheader("Face-Based Mood & Vibe Intelligence")
st.markdown("Upload a photo and let AI read your **vibe** ✨")

# ---------------- LOAD MODELS ----------------
@st.cache_resource
def load_models():
    face = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    smile = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_smile.xml"
    )
    eye = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye.xml"
    )
    return face, smile, eye

face_cascade, smile_cascade, eye_cascade = load_models()

# ---------------- UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📷 Upload a face image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        st.error("😕 No face detected. Try another image.")
    else:
        (x, y, w, h) = faces[0]
        roi_gray = gray[y:y+h, x:x+w]

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)

        # ---------------- VIBE LOGIC ----------------
        vibe = "🧘 Calm Neutral"
        confidence = 0.5

        if len(smiles) > 0:
            vibe = "✨ Happy & Positive"
            confidence = 0.85
        elif len(eyes) < 2:
            vibe = "😴 Low Energy / Tired"
            confidence = 0.7
        elif w > h:
            vibe = "😎 Confident Presence"
            confidence = 0.75

        # ---------------- OUTPUT ----------------
        st.success(f"### 🔮 Vibe Detected: **{vibe}**")
        st.progress(confidence)

        st.markdown("### 🧠 Analysis Summary")
        st.write(f"• Face detected ✅")
        st.write(f"• Smiles detected: {len(smiles)}")
        st.write(f"• Eyes detected: {len(eyes)}")

        st.markdown("---")
        st.markdown("### 👍 Was this accurate?")
        col1, col2 = st.columns(2)
        with col1:
            st.button("👍 Yes")
        with col2:
            st.button("👎 Needs improvement")

st.markdown("---")
st.caption("Built by Lavisha | Computer Vision + Streamlit")
