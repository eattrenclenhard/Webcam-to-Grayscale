import streamlit as st
from PIL import Image

with st.expander("Launch Webcam"):
    # launch webcam
    camera_img = st.camera_input("Camera")

if camera_img:
    # create a pillow image instance
    img = Image.open(camera_img)

    # convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)

