import streamlit as st
import numpy as np
import librosa
import moviepy.editor as mp
import soundfile as sf
from pydub import AudioSegment

def getAudioFromVideo(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    return True

def addAudioToVideo(src, dest, audio):
    video = mp.VideoFileClip(src)
    video.write_videofile(dest, audio=audio)
    return True

def readAudio(audio_path, sr=None, chunk_size=None):
    raw_audio, samplerate = librosa.core.load(audio_path, sr=sr)
    chunk = chunk_size * samplerate
    audio = np.array([raw_audio[i:i+chunk] for i in range(0, len(raw_audio), chunk)])
    return raw_audio, audio, chunk

def computeEnergy(audio):
    audio_amp = np.abs(audio) ** 2
    return [np.sum(x) for x in audio_amp]

def createSilence(secs):
    duration = secs * 1000
    silence = AudioSegment.silent(duration=duration)
    silence = silence.get_array_of_samples()
    return np.array(silence)

def clearAudio(audio_file, threshold=1600, chunk_size=4):
    raw_audio, audio, chunk = readAudio(audio_file, chunk_size=chunk_size, sr=None)
    energy = computeEnergy(audio)

    chunk = chunk_size * 44100
    silence = createSilence(secs=chunk_size)

    for i in range(len(energy)):
        if energy[i] > threshold:
            start = i * chunk
            end = start + chunk
            raw_audio[start:end] = silence

    return raw_audio

def processFile(file, file_type, threshold=1600, chunk_size=4):
    if file_type == "audio":
        cleared_audio = clearAudio(file, threshold, chunk_size)
        return cleared_audio
    elif file_type == "video":
        temp_audio_path = "temp_audio.mp3"
        getAudioFromVideo(file, temp_audio_path)
        cleared_audio = clearAudio(temp_audio_path, threshold, chunk_size)

        temp_video_path = "temp_video.mp4"
        addAudioToVideo(src=file, dest=temp_video_path, audio=cleared_audio)
        return open(temp_video_path, "rb").read()

def main():

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
    st.title("AudioCleaner")

    st.write("## Drop down the file whose noisy audio you need to get cleaned.")

    file_type = st.radio("Select file type", ["audio", "video"])
    file = st.file_uploader(f"Upload a {file_type} file", type=[file_type])

    if file is not None:
        processed_data = processFile(file, file_type)

        if file_type == "audio":
            st.audio(processed_data, format='audio/wav', start_time=0)
            st.download_button(
                label="Download Cleared Audio",
                data=processed_data,
                file_name="cleared_audio.wav",
                mime="audio/wav"
            )
        elif file_type == "video":
            st.video(processed_data)
            st.download_button(
                label="Download Cleared Video",
                data=processed_data,
                file_name="cleared_video.mp4",
                mime="video/mp4"
            )

if __name__ == "__main__":
    main()