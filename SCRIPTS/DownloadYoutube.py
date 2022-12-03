from pytube import YouTube
import os
import speech_recognition as sr
import whisper
import pandas as pd
from pathlib import Path 

df = pd.DataFrame(columns=["ID","URL","OriginalFilename","CleanFilename","Transcription"])

i = 0

with open('/url_list.txt') as urllist_file:
    for line in urllist_file:
        #print(line) # The comma to suppress the extra new line char
        nsert = []
        i +=1

        yt = YouTube(line)
        yt.streams.first().default_filename
        origfilename = yt.streams.first().default_filename
        cleanfilename = origfilename.replace('.3gpp','')
        cleanfilename = cleanfilename.replace(' ','')
        #print(cleanfilename)

        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(filename = cleanfilename+".mp4")

        command2mp3 = "ffmpeg -i "+cleanfilename+".mp4 "+cleanfilename+".mp3"
        #print(command2mp3)

        os.system(command2mp3)


        model = whisper.load_model("tiny")
        text = model.transcribe(cleanfilename+".mp3")
        #printing the transcribe

        insert = [i, line, origfilename, cleanfilename, 'text']
        df.loc[i] = insert
        #print(text['text'])

filepath = Path('D:/UNI/CURRENT/PROYECTO COMPUTACION 1/PROYECTO_GIT/CSV/URlTranscripts.csv') 
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)  

