import streamlit as st
from PIL import Image


def convert_img(img_param):
    """Gets a PIL image file and returns its grayscale version"""
    img_param = Image.open(img_param)
    return img_param.convert("L")


col1, col2, col3 = st.columns([.5, 2, .5])
with col2:
    st.title('Color to Grayscale Converter')
    user_upload = st.file_uploader(label='Upload Image', key='imgUpload')
    if user_upload:
        user_gray_img = convert_img(user_upload)
        st.image(user_gray_img)

    with st.expander("Launch Webcam"):
        # launch webcam
        camera_img = st.camera_input("Camera")

    if camera_img:
        cam_gray_img = convert_img(camera_img)
        st.image(cam_gray_img)

        # # create a pillow image instance
        # img = Image.open(camera_img)
        #
        # # convert the pillow image to grayscale
        # gray_img = img.convert("L")
        #
        # # Render the grayscale image on the webpage
        # st.image(gray_img)
