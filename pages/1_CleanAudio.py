import streamlit as st
from pydub import AudioSegment
from io import BytesIO
import tempfile
import os

st.title("Audio Converter")
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3"])
audio=st.audio(uploaded_file, format='audio/mp3')

if uploaded_file is not None:
    st.write("File uploaded successfully!")

    # Save uploaded file to a temporary location
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    temp_file.write(uploaded_file.read())

    # Close the file to release the resources
    temp_file.close()

    # Convert the temporary file to AudioSegment
    sound = AudioSegment.from_mp3(temp_file.name)