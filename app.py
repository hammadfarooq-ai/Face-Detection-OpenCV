import cv2
import numpy as np
from PIL import Image
import streamlit as st
import io

st.title("Face Detection App with Save Option")

# Input method: Upload or Webcam
option = st.radio("Select Input Method:", ("Upload Image", "Use Webcam"))

img = None

if option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

elif option == "Use Webcam":
    st.write("Capture photo from your webcam")
    if st.button("Capture"):
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        cap.release()
        if not ret:
            st.error("Failed to capture image.")
        else:
            st.success("Photo captured!")

# Face detection
if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img_rgb, caption=f"Detected {len(faces)} face(s)", use_column_width=True)

    # Save image option
    buf = cv2.imencode(".jpg", img)[1].tobytes()
    st.download_button(
        label="Save Image",
        data=buf,
        file_name="face_detected.jpg",
        mime="image/jpeg"
    )
