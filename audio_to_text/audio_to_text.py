import speech_recognition as sr
from pydub import AudioSegment
import os

# Load the video file
video = AudioSegment.from_file("2.mp4", format="mp4")
audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
audio.export("audio.wav", format="wav")


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Open the audio file
with sr.AudioFile("audio.wav") as source:
    audio_text = r.record(source)
# Recognize the speech in the audio
text = r.recognize_google(audio_text, language='el-GR')


# Print the transcript
file_name = "transcription.txt"

with open(file_name, "w") as file:
    # Write to the file
    file.write(text+ '\n')
# Open the file for editing by the user
os.system(f"start {file_name}")


#https://towardsdatascience.com/transcribing-interview-data-from-video-to-text-with-python-5cdb6689eea1
#https://blog.devgenius.io/how-to-transcribe-a-video-with-97-accuracy-using-python-f59bbf71d640

#https://unix.stackexchange.com/questions/1670/how-can-i-use-ffmpeg-to-split-mpeg-video-into-10-minute-chunks

#https://stackoverflow.com/questions/67334379/cut-mp4-in-pieces-python
