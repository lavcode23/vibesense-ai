import streamlit as st
import numpy as np
from PIL import Image
import cv2
from fer import FER

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(
    page_title="VibeSense AI",
    page_icon="🎭",
    layout="centered"
)

st.title("🎭 VibeSense AI")
st.subheader("Emotion-aware AI that reacts to your vibe")

# -----------------------------
# Load Emotion Detector
# -----------------------------
@st.cache_resource
def load_detector():
    return FER(mtcnn=False)

detector = load_detector()

# -----------------------------
# Image Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a face image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_np = np.array(image)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    with st.spinner("Analyzing vibes..."):
        result = detector.detect_emotions(img_cv)

    if not result:
        st.error("No face detected 😕")
    else:
        emotions = result[0]["emotions"]
        top_emotion = max(emotions, key=emotions.get)
        confidence = emotions[top_emotion]

        st.success(f"🎯 Detected Emotion: **{top_emotion.upper()}**")
        st.progress(confidence)

        # -----------------------------
        # Vibe Response
        # -----------------------------
        vibe_map = {
            "happy": "😄 Keep shining!",
            "sad": "💙 It's okay to feel this way.",
            "angry": "🔥 Take a deep breath.",
            "neutral": "😌 Calm and balanced.",
            "surprise": "😲 Something caught your attention!"
        }

        st.info(vibe_map.get(top_emotion, "✨ Unique vibe detected!"))

        # -----------------------------
        # Feedback Loop
        # -----------------------------
        st.markdown("### Was this accurate?")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("👍 Yes"):
                st.success("Thanks for the feedback!")

        with col2:
            if st.button("👎 No"):
                st.warning("We'll improve!")

else:
    st.info("👆 Upload an image to begin")
