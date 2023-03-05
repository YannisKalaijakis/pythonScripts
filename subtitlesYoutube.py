from youtube_transcript_api import YouTubeTranscriptApi
import nltk
nltk.download('punkt')

srt = YouTubeTranscriptApi.get_transcript('jQVCSKpQmCo', languages=['en'])

with open("subtitles.txt", "w") as f:
   

    for i in srt:

        f.write("{}\n".format(i['text']))
