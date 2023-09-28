'''import sqlite3

import speaker_verification_toolkit.tools as svt
import librosa
import pyttsx3
import wavfile
import speech_recognition as sr
from scipy.io.wavfile import write

firstname = input ("please enter your first name ")
lastname = input ("please enter your last name ")
data,sr= librosa.load ('test.wav.wav', sr=16000,mono='true')
data = svt.rms_silence_filter(data)
data = svt.extract_mfcc(data)
print ("MFCC Values :\n", data)

newdata,sr= librosa.load ('BE2.wav', sr=16000,mono='true')
newdata = svt.rms_silence_filter(newdata)
newdata = svt.extract_mfcc(newdata)
print ("MFCC Values :\n", newdata)

#svt.find_nearest_voice_data(data,newdata)
dist=svt.compute_distance(data, newdata)
print(dist)



#establish connection to a db
conn = sqlite3.connect('MFCC.db')

#create a cursor
c = conn.cursor()

#create a table once it is created just hash it out

c.execute("CREATE TABLE IF NOT EXISTS customers (first_name text,last_name text,mfcc real)")

c.execute("INSERT INTO customers VALUES('?', '?',?)",(firstname, lastname, data,) )
#c.execute("INSERT INTO customers (mfcc) VALUES(?, ?)", (data))
#commit our command to the datatbase
conn.commit()



print ("command done")

freq = 44100
engine = pyttsx3.init() # creates a new instance 
engine.setProperty('rate', 150) # sets the speaking rate for the engine
r = sr.Recognizer() # creates new instance which represents a collection of speech recognitio
with sr.Microphone() as source: # sets the microphone on the computer as a source   
    r.adjust_for_ambient_noise(source) # adjusts the recording for aimbient noise from the surroundings
    engine.say ("i'm listening")# says the word hello
    engine.runAndWait()# initilises the text to speech and makes it run 
    audio = r.listen(source, timeout=5) # records a phrase and stores it in the variable audio
    wavfile.write("C:\worksop collage\computing\python\a level\Smart Assistant\test.wav.wav",
              audio,
              sample_rate=44100,
              bits_per_sample=16,
              fmt=wavfile.chunk.WavFormat.PCM,
              metadata=None)
#mfcc = svt.rms_silence_filter(audio)
#mfcc = svt.extract_mfcc(audio)

#svt.find_nearest_voice_data('MFCC.db', newdata)

#close the connection 
#conn.close()
'''
import pyttsx3

import speech_recognition as sr

from scipy.io.wavfile import write

freq = 44100

engine = pyttsx3.init()  # creates a new instance

engine.setProperty('rate', 150)  # sets the speaking rate for the engine

r = sr.Recognizer()  # creates new instance which represents a collection of speech recognitio

with sr.Microphone() as source:  # sets the microphone on the computer as a source

    global compare

    r.adjust_for_ambient_noise(source)  # adjusts the recording for aimbient noise from the surroundings

    engine.say("i'm listening")  # says the word hello

    engine.runAndWait()  # initilises the text to speech and makes it run

    audio = r.listen(source, timeout=5)  # records a phrase and stores it in the variable audio
with open("recording0.wav", mode='ba') as file:
    file.write(audio.get_wav_data())
    file.close()