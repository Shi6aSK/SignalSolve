from gtts import gTTS
import os
import streamlit as st

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
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to convert text to speech using Google Text-to-Speech API
def text_to_speech(text: str, lang='en', voice_name='default'):
    tts = gTTS(text=text, lang=lang, tld='com', slow=False, lang_check=False)
    audio_file_path = "output.mp3"
    tts.save(audio_file_path)
    return audio_file_path

# Streamlit UI setup
st.title("Give voice to your Scripts")
st.markdown("Write your text and convert it to speech!")



# Text input from user
user_input = st.text_area("Enter text to convert to speech", "This is a sample text. You can change it to anything you want.")

# Select box for language selection
language = st.selectbox("Select Language", ["en", "es", "fr", "de"])

# Select box for voice selection
voices = {
    "Default": None,  # None will use the default voice
    "en-US-Wavenet-C": "Male",
    "en-US-Wavenet-D": "Female",
    "en-US-Wavenet-A": "WaveNet",
    "en-US-Wavenet-B": "WaveNet-compact",
    "en-US-Standard-C": "Standard",
    "en-US-Standard-B": "Standard-compact",
    "en-US-Standard-A": "Neutral",
}
selected_voice = st.selectbox("Select Voice", list(voices.keys()))

if st.button("Convert"):
    try:
        speech_path = text_to_speech(user_input, lang=language, voice_name=voices[selected_voice])
        st.audio(open(speech_path, 'rb'), format="audio/mp3")
        os.remove(speech_path)
    except Exception as e:
        st.error(f"An error occurred: {e}")