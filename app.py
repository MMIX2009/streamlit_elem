import streamlit as st
col1, col2, col3 = st.columns([1,2,1])

col1.markdown("## Welcome to my app!")
col1.markdown(" Here is some info about the app")

uploaded_photo = col2.file_uploader("Upload an image")
camera_photo = col2.camera_input("Take a picture")
