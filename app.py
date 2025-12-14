import streamlit as st
from PIL import Image
import numpy as np
from deepface import DeepFace

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="VibeSense AI 🔮",
    page_icon="😎",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------
st.markdown(
    "<h1 style='text-align:center;'>VibeSense AI 🔮</h1>"
    "<h4 style='text-align:center;'>Emotion-Powered Face Intelligence</h4>",
    unsafe_allow_html=True
)

st.divider()

# -------------------------------
# Upload Image
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload a clear face image 👇",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing your vibe... ✨"):
        try:
            result = DeepFace.analyze(
                img_path=np.array(image),
                actions=["emotion"],
                enforce_detection=False
            )

            emotion = result[0]["dominant_emotion"]

            vibe_map = {
                "happy": ("😄 Positive & Energetic", "Yellow"),
                "sad": ("😢 Calm & Reflective", "Blue"),
                "angry": ("🔥 Intense & Powerful", "Red"),
                "surprise": ("🤯 Curious & Creative", "Purple"),
                "neutral": ("😐 Balanced & Focused", "Gray"),
                "fear": ("😨 Sensitive & Aware", "Teal"),
                "disgust": ("🤢 Honest & Selective", "Green")
            }

            vibe_text, color = vibe_map.get(
                emotion, ("✨ Unique Energy", "Black")
            )

            st.success(f"**Detected Emotion:** {emotion.upper()}")
            st.markdown(f"### {vibe_text}")
            st.markdown(f"🎨 **Your Vibe Color:** `{color}`")

            st.divider()

            # Feedback
            st.markdown("### Was this accurate?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("👍 Yes"):
                    st.success("Thanks for the feedback!")
            with col2:
                if st.button("👎 No"):
                    st.info("We’ll improve!")

        except Exception as e:
            st.error("Face could not be analyzed. Try a clearer image.")
