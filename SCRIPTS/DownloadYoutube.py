import os, whisper, re
import speech_recognition as sr
import pandas as pd
from pathlib import Path 
from pytube import YouTube

df = pd.DataFrame(columns=["ID","URL","OriginalFilename","CleanFilename","Transcription"])

i = 0


filepathtxt = Path('D:/UNI/CURRENT/PROYECTO COMPUTACION 1/ProyectoPC1/TXT/url_list.txt') 


with open(filepathtxt) as urllist_file:
    for line in urllist_file:
        #print(line) # The comma to suppress the extra new line char
        nsert = []
        i +=1

        yt = YouTube(line)
        yt.streams.first().default_filename
        origfilename = yt.streams.first().default_filename
        cleanfilename = origfilename.replace('.3gpp','')
        cleanfilename = cleanfilename.replace(' ','')
        cleanfilename = re.sub(r'[\W_]', '', cleanfilename)

        pathmp3 = 'D:/UNI/CURRENT/PROYECTO COMPUTACION 1/ProyectoPC1/MP3/'+cleanfilename+'.mp3'
        pathmp4 = 'D:/UNI/CURRENT/PROYECTO COMPUTACION 1/ProyectoPC1/MP4/'+cleanfilename+'.mp4'
        pathtxt = 'D:/UNI/CURRENT/PROYECTO COMPUTACION 1/ProyectoPC1/TRANSCRIPT/RAW/'+cleanfilename+'.txt'
        filepathmp3 = Path(pathmp3) 
        filepathmp4 = Path(pathmp4) 

        #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(filename = cleanfilename+".mp4")
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(filename = filepathmp4)

        #command2mp3 = "ffmpeg -i "+cleanfilename+".mp4 "+cleanfilename+".mp3"
        command2mp3 = "ffmpeg -i \""+pathmp4+"\" \""+pathmp3+"\""
        print(command2mp3)

        os.system(command2mp3)


        model = whisper.load_model("tiny")
        #text = model.transcribe(cleanfilename+".mp3")
        text = model.transcribe(pathmp3)
        #printing the transcribe
        text_file = open(pathtxt, "w")
        n = text_file.write(str(text["text"]))
        text_file.close()


        #insert = [i, line, origfilename, cleanfilename, 'text']
        #df.loc[i] = insert
        #print(text['text'])

#filepathcsv = Path('D:/UNI/CURRENT/PROYECTO COMPUTACION 1/PROYECTO_GIT/CSV/URlTranscripts.csv') 
#filepathcsv.parent.mkdir(parents=True, exist_ok=True)  
#df.to_csv(filepathcsv)  

