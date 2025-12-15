😎 VibeSense AI — Face-Based Mood & Vibe Intelligence System

VibeSense AI is an interactive computer vision–powered web application that analyzes facial cues from an image and intelligently infers a user's vibe / emotional state using lightweight, explainable AI logic.

This project focuses on real-world deployability, clean UI, and human-centric AI — avoiding heavy deep-learning dependencies while still delivering meaningful insights.

🚀 Live Demo

👉 Streamlit App:(https://vibesense-ai-xs9puslv2umwgxr4jx89dq.streamlit.app/)
👉 GitHub Repo: https://github.com/lavcode23/vibesense-ai

🧠 What This Project Does

Detects a human face from an uploaded image

Analyzes facial features such as:

Smiles

Eye openness

Face proportions

Infers the user's vibe using rule-based intelligence

Displays:

Emoji-based mood output 😄😴😎

Confidence score

Visual feedback loop (👍 / 👎)

✨ Why VibeSense Is Unique

✅ No heavy deep-learning libraries
✅ Fully deployable on Streamlit Cloud
✅ Explainable & transparent logic
✅ Fast and lightweight
✅ Human-centric design
✅ Resume-ready real-world project

Unlike typical emotion detection apps, VibeSense focuses on behavioral inference and user experience, not black-box predictions.

🛠️ Tech Stack

Python

Streamlit – Frontend & deployment

OpenCV – Face, smile & eye detection

NumPy – Numerical processing

Pillow – Image handling

📂 Project Structure
vibesense-ai/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── README.md             # Project documentation

⚙️ How It Works (Logic Overview)

User uploads an image

Image is converted to grayscale

OpenCV Haar Cascades detect:

Face

Smile

Eyes

Rule-based logic maps facial signals to a vibe

Confidence score is calculated

Results displayed with emojis and progress bar

🧪 Example Output
Facial Signals	Detected Vibe
Smile detected	✨ Happy & Positive
Eyes partially closed	😴 Low Energy
Wide face posture	😎 Confident Presence
Neutral features	🧘 Calm Neutral
▶️ Run Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the App
streamlit run app.py

📦 requirements.txt
streamlit
numpy
opencv-python-headless
pillow

🎯 Use Cases

Human-centric AI experiments

Computer Vision learning projects

UI-focused ML demos

Resume & portfolio projects

Rapid AI prototyping

🔮 Future Improvements

Real-time webcam input

User history & personalization

Emotion timeline visualization

Multi-face detection

ML-based scoring refinement

👩‍💻 Author

Lavisha Yadav
AI / ML | Data Science
GitHub: https://github.com/lavcode23

LinkedIn: https://www.linkedin.com/in/lavishayadav-ai/

⭐ Final Note

VibeSense AI proves that great AI projects are not about heavy models — they are about clarity, usability, and deployment.

If you like this project, don’t forget to ⭐ the repository!
