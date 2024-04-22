import streamlit as st
import speech_recognition as sr

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://raw.githubusercontent.com/Shi6aSK/SignalSolve/main/pages/Try%20Online.png");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

# Initialize the recognizer
r = sr.Recognizer()

# Function to transcribe audio from the microphone
def transcribe_audio():
    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            st.success(f"Transcription: {text}")
        except sr.UnknownValueError:
            st.error("Could not understand audio. Please try again.")
        except sr.RequestError as e:
            st.error(f"Error: {e}")

# Streamlit app
def main():
    st.title("Live Microphone to Text Transcription")

    # Create a button to start transcription
    if st.button("Start Transcription"):
        transcribe_audio()

if __name__ == "__main__":
    main()