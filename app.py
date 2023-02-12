import streamlit as st
import time

col1, col2, col3 = st.columns([1,2,1])

col1.markdown("## Welcome to my app!")
col1.markdown(" Here is some info about the app")

uploaded_photo = col2.file_uploader("Upload an image")
camera_photo = col2.camera_input("Take a picture")

progress_bar = col2.progress(0);

for perc_completed in range(100):
  time.sleep(0.05)
  progress_bar.progress(perc_completed +1)
  
if uploaded_photo:
  col2.success("Photo uploaded sucessfully!")
  
col3.metric(label="Temperature", value="60 °C", delta="3 °C")


