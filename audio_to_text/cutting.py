from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Replace the filename below.
required_video_file = "speech_old.mp4"

with open("times.txt") as f:
  times = f.readlines()

times = [x.strip() for x in times] 

for time in times:
  starttime = int(time.split("-")[0])
  endtime = int(time.split("-")[1])
  ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(times.index(time)+1)+".mp4")

#h#https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
  #https://stackoverflow.com/questions/67334379/cut-mp4-in-pieces-python
  #https://realpython.com/python-speech-recognition/
  #https://stackoverflow.com/questions/62719408/speech-recognition-python-having-strange-request-error
  #https://stackoverflow.com/questions/75566209/python-speech-recognition-error-400-bad-request
