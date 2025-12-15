import streamlit as st
import numpy as np
import cv2
from fer import FER
from PIL import Image

# -----------------------
# App Config
# -----------------------
st.set_page_config(
    page_title="VibeSense AI",
    page_icon="😎",
    layout="centered"
)

st.title("😎 VibeSense AI")
st.subheader("Emotion • Aura • Vibe Detector")

st.markdown("Upload a face image and let AI read your **vibes** ✨")

# -----------------------
# Load Emotion Detector
# -----------------------
@st.cache_resource
def load_detector():
    return FER(mtcnn=False)

detector = load_detector()

# -----------------------
# Image Upload
# -----------------------
uploaded_file = st.file_uploader(
    "📷 Upload a face image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("🔍 Reading your vibes..."):
        emotions = detector.detect_emotions(img_array)

    if not emotions:
        st.error("😕 No face detected. Try another image.")
    else:
        emotion_scores = emotions[0]["emotions"]
        top_emotion = max(emotion_scores, key=emotion_scores.get)
        confidence = emotion_scores[top_emotion]

        vibe_map = {
            "happy": "✨ Positive Aura",
            "sad": "🌧 Soft & Emotional",
            "angry": "🔥 Intense Energy",
            "fear": "⚡ Alert & Aware",
            "surprise": "🎉 Curious Vibes",
            "neutral": "🧘 Calm Presence",
            "disgust": "😬 Reserved Mood"
        }

        st.success(f"### Dominant Emotion: **{top_emotion.upper()}**")
        st.progress(min(confidence, 1.0))

        st.markdown(f"## 🔮 Vibe Reading: {vibe_map.get(top_emotion, 'Unknown')}")

        st.markdown("---")
        st.markdown("### 📊 Emotion Breakdown")
        st.bar_chart(emotion_scores)

        st.markdown("---")
        st.markdown("### 👍 Did this feel accurate?")
        col1, col2 = st.columns(2)
        with col1:
            st.button("👍 Yes!")
        with col2:
            st.button("👎 Nope")

st.markdown("---")
st.caption("Built with ❤️ by Lavisha | Streamlit + FER")
