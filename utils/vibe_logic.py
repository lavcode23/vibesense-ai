def infer_vibe(features):
    eye = features["eye_open"]
    head = features["head_y"]

    focus = "Focused" if eye > 0.015 else "Tired"
    calm = "Calm" if head < 0.55 else "Restless"

    if focus == "Focused" and calm == "Calm":
        vibe = "🎯 Deep Flow"
    elif focus == "Tired":
        vibe = "😴 Low Energy"
    else:
        vibe = "🌊 Mildly Distracted"

    confidence = round(min(max(eye * 50, 0), 1), 2)

    return vibe, confidence
