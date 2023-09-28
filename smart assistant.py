import speech_recognition as sw
import speaker_verification_toolkit.tools as svt
import librosa
import pyttsx3
import wavfile
import sqlite3
from scipy.io.wavfile import write
import json

conn = sqlite3.connect('MFCC.db')#establish connection to a db
c = conn.cursor()#create a cursor


freq = 44100

engine = pyttsx3.init()  # creates a new instance

engine.setProperty('rate', 150)  # sets the speaking rate for the engine
with open('check.txt', 'r') as f:
    check = f.read()


def newuser():
    r = sw.Recognizer()  # creates new instance which represents a collection of speech recognition
    with sw.Microphone() as source:  # sets the microphone on the computer as a source
        r.adjust_for_ambient_noise(source)  # adjusts the recording for aimbient noise from the surroundings
        engine.say("please say the pass phrase that you want to use")  # says the words im listening
        engine.runAndWait()  # initilises the text to speech and makes it run
        audio = r.listen(source, timeout=5)  # records a phrase and stores it in the variable audio
        compare = r.recognize_google(audio)
        passphrase = compare
        engine.say("thank you, please wait while your data is stored")  # says the words please state your first name
        engine.runAndWait()  # initilises the text to speech and makes it run
    with open("recording0.wav", mode='wb') as file:
        file.write(audio.get_wav_data())
        file.close()
    data, sr = librosa.load('recording0.wav', sr=16000, mono=True)
    data = svt.rms_silence_filter(data)
    data = svt.extract_mfcc(data)

    r = sw.Recognizer()  # creates new instance which represents a collection of speech recognition
    with sw.Microphone() as source:  # sets the microphone on the computer as a source
        r.adjust_for_ambient_noise(source)  # adjusts the recording for aimbient noise from the surroundings
        engine.say("please state your first name")  # says the words please state your first name
        engine.runAndWait()  # initilises the text to speech and makes it run
        audio = r.listen(source, timeout=5)  # records a phrase and stores it in the variable audio
        compare = r.recognize_google(audio)  # stores what the user says in a variable
    firstname = compare  # stores firstname in compare
    ##storing the data in a json database
    with open("C:/worksop collage/computing/python/a level/Smart Assistant/database.txt") as file:
        database = json.load(file)
    personEntry = {}
    datadict={}
    for i in range(len(data)):
        datadict[i]=data[i]
    database[firstname] = datadict  # sets key 0 to value but can be a dictionary or variable
    with open("C:/worksop collage/computing/python/a level/Smart Assistant/database.txt",
              "w") as file:  # opens the file again
        string = json.dumps(database)  # dumps the value of database into string
        file.write(
            string)  # writes the value of string into the database, if try to write to already writen id field overwrites it
    file.close()

    print(firstname)
    print("MFCC Values :\n", data)
    ##storing the check data
    with open('check.txt', 'a') as f:
        f.write('1')

def checkuser():
    r = sw.Recognizer()  # creates new instance which represents a collection of speech recognition
    with sw.Microphone() as source:  # sets the microphone on the computer as a source
        r.adjust_for_ambient_noise(source)  # adjusts the recording for aimbient noise from the surroundings
        engine.say("please say the pass phrase that you want to use")  # says the words im listening
        engine.runAndWait()  # initilises the text to speech and makes it run
        audio = r.listen(source, timeout=5)  # records a phrase and stores it in the variable audio
        compare = r.recognize_google(audio)
        passphrase = compare
        engine.say("thank you, please wait while your data is stored")  # says the words please state your first name
        engine.runAndWait()  # initilises the text to speech and makes it run
    with open("recording0.wav", mode='wb') as file:
        file.write(audio.get_wav_data())
        file.close()
    data, sr = librosa.load('recording0.wav', sr=16000, mono=True)
    data = svt.rms_silence_filter(data)
    data = svt.extract_mfcc(data)

    r = sw.Recognizer()  # creates new instance which represents a collection of speech recognition
    with sw.Microphone() as source:  # sets the microphone on the computer as a source
        r.adjust_for_ambient_noise(source)  # adjusts the recording for aimbient noise from the surroundings
        engine.say("please say the pass phrase that you want to use")  # says the words im listening
        engine.runAndWait()  # initilises the text to speech and makes it run
        audio = r.listen(source, timeout=5)  # records a phrase and stores it in the variable audio
        compare = r.recognize_google(audio)
        passphrase = compare
        engine.say("thank you, please wait while your data is stored")  # says the words please state your first name
        engine.runAndWait()  # initilises the text to speech and makes it run
    with open("recording0.wav", mode='wb') as file:
        file.write(audio.get_wav_data())
        file.close()
    newdata, sr = librosa.load('recording0.wav', sr=16000, mono=True)
    newdata = svt.rms_silence_filter(newdata)
    newdata = svt.extract_mfcc(newdata)


if check==1:
    checkuser()
else:
    newuser()


'''
#svt.find_nearest_voice_data(data,newdata)
dist=svt.compute_distance(data, newdata)
print(dist)






print ("command done")



conn = sqlite3.connect('MFCC.db')#establish connection to a db
c = conn.cursor()#create a cursor
c.execute('SELECT mfcc FROM people')
tbldata = c.fetchall()
print(tbldata)
for row in tbldata:
    print(row)

#svt.find_nearest_voice_data('MFCC.db', newdata)

####### what to do next, make it so that it doent keep storing within database that is compared against by looping correclty
####### put into function and work out how to find closest voice data then compare to see if its wthin certian boundry'''
#svt.find_nearest_voice_data('MFCC.db', newdata)



