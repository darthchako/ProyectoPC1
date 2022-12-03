import os, whisper, string, re
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
        cleanfilename2 = cleanfilename.translate(str.maketrans("","",string.punctuation))
        cleanfilename = re.sub(r'[\W_]', '', cleanfilename)
        print(string.punctuation)
        print(cleanfilename)
        print(cleanfilename2)



