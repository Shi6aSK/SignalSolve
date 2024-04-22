import numpy as np
import librosa
import soundfile as sf
from sklearn.cluster import SpectralClustering
from pydub import AudioSegment
import os

# Function to load audio from file
def load_audio(file):
    try:
        samples, sampling_rate = librosa.load(file, sr=None, mono=True, offset=0.0, duration=None)
        return samples, sampling_rate
    except Exception as e:
        print(f"Error loading audio: {e}")
        return None, None

# Function to perform spectral clustering on spectrogram
def spectral_clustering(specgram_data, n_clusters=2):
    spectral = SpectralClustering(n_clusters=n_clusters, affinity="rbf", n_jobs=-1, assign_labels='discretize')
    all_labels = spectral.fit_predict(specgram_data.T)
    return all_labels

# Function to extract audio
def extract_audio(filename, audio, sampling_rate):
    try:
        sf.write(filename, audio, samplerate=sampling_rate)
        print("Extracted Successfully")
    except Exception as e:
        print(f"Error extracting audio: {e}")

# Function to clean audio
def clean_audio(input_file, output_file):
    # Load audio
    audio_samples, audio_sampling_rate = load_audio(input_file)

    if audio_samples is not None and audio_sampling_rate is not None:
        # Compute spectrogram
        specgram_data_final = librosa.stft(audio_samples, n_fft=4096, hop_length=128)

        # Perform spectral clustering
        all_labels = spectral_clustering(specgram_data_final)

        # Apply mask to spectrogram
        cleaned_specgram_data = specgram_data_final * all_labels[:, np.newaxis]

        # Extract cleaned audio
        output_audio = librosa.core.istft(cleaned_specgram_data, win_length=4096, hop_length=128)
        extract_audio(output_file, output_audio, audio_sampling_rate)

# Main function
def main():
    # Input and output file paths
    input_mp3_file = "E:\DTI\project\pages\\audio1.mp3"
    output_mp3_file = "cleaned_audio.mp3"
    input_mp4_file = "E:\DTI\project\pages\\video1.mp4"
    output_mp4_file = "cleaned_audio.mp4"

    # Clean MP3 audio
    print("Cleaning MP3 audio...")
    clean_audio(input_mp3_file, output_mp3_file)
    print("MP3 audio cleaned successfully!")

    # Clean MP4 audio
    print("Cleaning MP4 audio...")
    clean_audio(input_mp4_file, output_mp4_file)
    print("MP4 audio cleaned successfully!")

if __name__ == "__main__":
    main()
