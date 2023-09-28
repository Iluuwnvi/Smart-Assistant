import customtkinter
from customtkinter import CTkImage
from PIL import Image
import keyboard
import speech_recognition as sr
from AppOpener import open 
import pyttsx3
import pywhatkit as kt
import win32com.client
import ctypes

global ol
global olmailitem
global window
global mystring
global compare
global num1
global num2 

engine = pyttsx3.init() # creates a new instance 
engine.setProperty('rate', 150) # sets the speaking rate for the engine
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x200")



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=5, padx=10, fill="both", expand=True)
# setting tkinter window size
## set the attributes and dimensions of the screen and where it is placed

root.attributes('-topmost', 1) # sets the window to always be on top


#root.withdraw()
root.title("Smart Assistant") # names the window
label = customtkinter.CTkLabel(master=frame, text="Hello, I am your digital smart assistant, how may I help?") # adds text to the window
label.pack(pady=12, padx=10)

##################do more on the gui

engine = pyttsx3.init()  # creates a new instance
def listen():
    global compare
    r = sw.Recognizer()
    with sw.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5)  # records a phrase and stores it in the variable audio
            compare = r.recognize_google(audio)
        except UnknownValueError:
            engine.say("I'm sorry I didn't hear you pleaes speak louder")
            engine.runAndWait()
            listen()

#stores a numpy array in a json database
def store():
    global compare
    engine.say("please say your first name")  # says the words in quotation marks
    engine.runAndWait()  # initilises the text to speech and makes it run
    listen() # runs the function listen
    name = compare#stores compare in name

    firstname = name#########needs to be a varaible of the name
    engine.say("please say the pass phrase that you want to use")  # says the words in quotation marks
    engine.runAndWait()  # initilises the text to speech and makes it run
    listen()
    passphrase = compare
    with open("C:/worksop collage/computing/python/a level/Smart Assistant/passphrase.txt") as file:
        database = json.load(file)#loads the file
    database[name] = passphrase  # sets key called name to value
    print(name)
    print(passphrase)
    with open("C:/worksop collage/computing/python/a level/Smart Assistant/passphrase.txt", "w") as file:
        string = json.dumps(database)  # dumps the value of database into string
        file.write(string)  # writes the value of string into the database, if try to write to already writen id field overwrites it
    file.close()
    engine.say("thank you, please wait while your voice is analysed and your data stored")  # says the words in quotation marks
    engine.runAndWait()  # initilises the text to speech and makes it run
    with open("recording0.wav", mode='wb') as file:
        file.write(audio.get_wav_data())
        file.close()
    data, sr = librosa.load('recording0.wav', sr=16000, mono=True)
    data = svt.rms_silence_filter(data)
    data = svt.extract_mfcc(data)
    serialisable_data = data.tolist()
    ##storing the data in a json database
    with open("C:/worksop collage/computing/python/a level/Smart Assistant/database.txt") as file:
        database = json.load(file)
    personEntry = {}
    datadict={}
    for i in range(len(serialisable_data)):#itterates through all the values in the data and stores it in a dictionary
        datadict[i]=serialisable_data[i]
    database[firstname] = datadict  # sets key 0 to value but can be a dictionary or variable
    with open("C:/worksop collage/computing/python/a level/Smart Assistant/database.txt",
              "w") as file:  # opens the file again
       string = json.dumps(database)  # dumps the value of database into string
       file.write(string)  # writes the value of string into the database, if try to write to already writen id field overwrites it
    file.close()
    with open("C:/worksop collage/computing/python/a level/Smart Assistant/check.txt" ,"w") as file:
        file.write("1")



def compare(): # gets the voice data that needs to be comapared against the database
    global names
    global index
    global comparedata
    global posmfcc
    global compare
    global passphrase
    engine.say("please say your pass phrase")  # says the words in quotation marks
    engine.runAndWait()  # initilises the text to speech and makes it run
    listen()
    inputtedpassphrase = compare
    engine.say("thank you, please wait while your voice is analysed")  # says the words in quotation marks
    engine.runAndWait()  # initilises the text to speech and makes it run
    with open("recording0.wav", mode='wb') as file:
        file.write(audio.get_wav_data())
        file.close()
    data, sr = librosa.load('recording0.wav', sr=16000, mono=True)
    data = svt.rms_silence_filter(data)
    data = svt.extract_mfcc(data)
    comparedata = data

    print (inputtedpassphrase)
    loadfrmdb()
    posname = (names[index])
    dist = int(svt.compute_distance(data, posmfcc))
    print(dist)
    if dist <= 27000 and passphrase == inputtedpassphrase:
        print(posname)
        engine.say("Welcome back " + posname)  # says the words in quotation marks
        engine.runAndWait()  # initilises the text to speech and makes it run

    else:
        engine.say("I'm sorry i could not recognise your voice, please either try again by saying again or register a new user by saying register")  # says the words im listening
        engine.runAndWait()
        listen()
        compare = r.recognize_google(audio)  # stores what the user says in a variable
        if "again" in compare:  # gets the index position of open
            compare()#runs the function compare to allow for another try at signing in
        elif "register" in compare:
            store()

        #input function that doese the desired outcomes stated above


### converting dictionary to numpy array
def loadfrmdb():
    global names
    global index
    global posmfcc
    global passphrase
    with open("C:/worksop collage/computing/python/a level/Smart Assistant/database.txt")as file:
        database = json.load(file)
    mfcc_list=[]
    names = []
    for i in database.keys():
        mfcc=[]
        for j in database[i].values():
            mfcc.append(j)
        mfcc_list.append(mfcc)
    index = svt.find_nearest_voice_data(mfcc_list, comparedata)
    for i in database.keys():
        names.append(i)

    posmfcc = (mfcc_list[index])
    name = names[index]
    print (name)

    with open("C:/worksop collage/computing/python/a level/Smart Assistant/passphrase.txt") as file:
        database = json.load(file)
    try:
        passphrase = database[name]  # returns the mfcc value
        print(passphrase)

    except KeyError:
        print("name not in list")

def diagnostics(): #should allow for an admin to access the database and change what values are entered in it. text instead of voice to allow for a more secure system
    with open("C:/worksop collage/computing/python/a level/Smart Assistant/database.txt")as file:
        database = json.load(file)
    names = []
    cpassword = "openup"
    password = str(input("enter password"))
    password = cpassword
    while password != cpassword:
        password = str(input("enter correct password"))
    for i in database.keys():
        names.append(i)
    print (names)



#########################################################################################################################################
def add(): #defines the fucntion add
    mystring = compare 
    index = (mystring.index("+"))
    num1="" # sets num1 as a variable 
    num2 = "" # sets num2 as a variable 
    backdone=False # sets backdone to false so the loop can repeat 
    frontdone = False # sets frontdone to false so the loop can repeat 
    index = index - 2 # takes 2 of the index posoiton 
    while (not backdone) and index >=0: # runs when backdone is false and index is greater than or equal to 0
        if mystring[index].isdigit(): # checks if the value at the index positon is a digit 
            num1=mystring[index]+num1 # adds teh digit to the variable num1
        else:
            backdone=True # sets backdone to true to stop the loop
        index-=1 # takes 1 off teh index posoition 
    index = (mystring.index("+")) # gets the index position of x again 
    index = index + 2 # adds 2 to the index position 
    while (not frontdone) and index<len(mystring): # runs when frontdone is false and index is less than the length of mystring
        if mystring[index].isdigit(): # checks if the index position is a digit 
            num2=num2 + mystring[index] # adds the digit at the index posotion ot the variable num2 
        else:
            frontdone=True # sets frontdone to true 
        index+=1 # adds 1 to the index posotion 
    answer = int(num1) + int(num2) # adds num1 and num2 
    engine.say ("the answer is " + (str(answer)))# says what the output to the calculation is 
    engine.runAndWait()# initilises the text to speech and makes it run 

def subtract():
    mystring = compare 
    index = (mystring.index("-"))
    num1="" # sets num1 as a variable 
    num2 = "" # sets num2 as a variable 
    backdone=False # sets backdone to false so the loop can repeat 
    frontdone = False # sets frontdone to false so the loop can repeat vc
    index = index - 2 # takes 2 of the index posoiton 
    while (not backdone) and index >=0: # runs when backdone is false and index is greater than or equal to 0
        if mystring[index].isdigit(): # checks if the value at the index positon is a digit 
            num1=mystring[index]+num1 # adds teh digit to the variable num1
        else:
            backdone=True # sets backdone to true to stop the loop   
        index-=1 # takes 1 off teh index posoition 
    index = (mystring.index("-")) # gets the index position of x again 
    index = index + 2 # adds 2 to the index position 
    while (not frontdone) and index<len(mystring): # runs when frontdone is false and index is less than the length of mystring
        if mystring[index].isdigit(): # checks if the index position is a digit 
            num2=num2 + mystring[index] # adds the digit at the index posotion ot the variable num2 
        else:
            frontdone=True # sets frontdone to true 
        index+=1 # adds 1 to the index posotion 
    answer = int(num1) - int(num2) 
    engine.say ("the answer is " + (str(answer)))# says what the output to the calculation is 
    engine.runAndWait()# initilises the text to speech and makes it run 


def multiply():
    global compare
    mystring = compare  # assinges the string in compare to mystring 
    index = (mystring.index("x"))# gets the index position of x 
    num1="" # sets num1 as a variable 
    num2 = "" # sets num2 as a variable 
    backdone=False # sets backdone to false so the loop can repeat 
    frontdone = False # sets frontdone to false so the loop can repeat
    index = index - 2 # takes 2 of the index posoiton 
    while (not backdone) and index >=0: # runs when backdone is false and index is greater than or equal to 0
        if mystring[index].isdigit(): # checks if the value at the index positon is a digit 
            num1=mystring[index]+num1 # adds teh digit to the variable num1
        else:
            backdone=True # sets backdone to true to stop the loop
        index-=1 # takes 1 off teh index posoition 
    index = (mystring.index("x")) # gets the index position of x again 
    index = index + 2 # adds 2 to the index position 
    while (not frontdone) and index<len(mystring): # runs when frontdone is false and index is less than the length of mystring
        if mystring[index].isdigit(): # checks if the index position is a digit 
            num2=num2 + mystring[index] # adds the digit at the index posotion ot the variable num2 
        else:
            frontdone=True # sets frontdone to true 
        index+=1 # adds 1 to the index posotion 
    answer = int(num1) * int(num2)
    engine.say ("the answer is " + (str(answer)))# says what the output to the calculation is 
    engine.runAndWait()# initilises the text to speech and makes it run 


def divide():
    mystring = compare   
    index = (mystring.index("/"))
    num1="" # sets num1 as a variable 
    num2 = "" # sets num2 as a variable 
    backdone=False # sets backdone to false so the loop can repeat 
    frontdone = False # sets frontdone to false so the loop can repeat 
    index = index - 2 # takes 2 of the index posoiton 
    while (not backdone) and index >=0: # runs when backdone is false and index is greater than or equal to 0
        if mystring[index].isdigit(): # checks if the value at the index positon is a digit 
            num1=mystring[index]+num1 # adds teh digit to the variable num1
        else:
            backdone=True # sets backdone to true to stop the loop
        index-=1 # takes 1 off teh index posoition 
    index = (mystring.index("/")) # gets the index position of / again 
    index = index + 2 # adds 2 to the index position 
    while (not frontdone) and index<len(mystring): # runs when frontdone is false and index is less than the length of mystring
        if mystring[index].isdigit(): # checks if the index position is a digit 
            num2=num2 + mystring[index] # adds the digit at the index posotion ot the variable num2 
        else:
            frontdone=True # sets frontdone to true 
        index+=1 # adds 1 to the index posotion 
    answer = int(num1) / int(num2)
    engine.say ("the answer is " + (str(answer)))# says what the output to the calculation is 
    engine.runAndWait()# initilises the text to speech and makes it run 


def runopen():# works out what app needs opening 
    words = compare.split() # splitting the string
    #slicing the list (negative index means index from the end)
    #-1 means the last element of the list
    endword = (words [-1]) # stores the last word in a varaible 
    open (str(endword), match_closest= True, output = False) # trys to open a app with the name of the endoword
    engine.say ("opening" + str(endword))# says what the output to the calculation is 
    engine.runAndWait()# initilises the text to speech and makes it run 
    #tk.Label(window, text = "last request: ").grid(column=2, row=3)
    #tk.Label(window, text=compare).grid(column=1, row=3) # adds text to the window


def email():
    ol=win32com.client.Dispatch("outlook.application")
    olmailitem=0x0 #size of the new email
    newmail=ol.CreateItem(olmailitem)# creates a new email 
    # asking what the subject of the email should be 
    listen()

    engine.say ("what would you like the subject of the email to be")# says the text
    engine.runAndWait()# initilises the text to speech and makes it run

    subject = compare
    newmail.Subject= subject# asks what the subject of the email should be
    # asking who the emial should be sent to
    engine.say ("who would you like to send the email to")# says whatever is in the brackets
    engine.runAndWait()# initilises the text to speech and makes it run
    listen()
    send = compare
    newmail.To= send # asks who it would want to be sent to
    #asking what the main body of the email should say
    engine.say ("What would you like to say in the email")# says whatever is in the brackets
    engine.runAndWait()# initilises the text to speech and makes it run
    listen()
    body = compare
    newmail.Body= body #inputs whatever is in the variable body into the body of the email
    engine.say("email created, please check to make sure i understood everything correctly. Especially the email address of the reciever. ")
    engine.runAndWait()
    newmail.Display() # displayes the new email on screen

def lock():
    ctypes.windll.user32.LockWorkStation() # locks the computer

def search():
    kt.search(compare)  # perfomes a google search for whatever is in compare
    engine.say("here is what i found on the web")  # says heres what i found on the web
    engine.runAndWait()  # initilises the text to speech and makes it run


def recognition(): #defines a new funcion that will be used for speech recognition
    global root
    root.deiconify()
    #window.attributes('-topmost', 1) # sets the window to always be on top

    engine.say ("i'm listening")# says the word hello
    engine.runAndWait()# initilises the text to speech and makes it run
    listen()
       # exept UnknownValueError:
       #     pass 
    if "open" in compare: # gets the index position of open
            print (compare) # outputs what the user says
            runopen()
    elif "x" in compare: # looks for the value x
        multiply() # runs the function multiply

    elif "/" in compare: # looks for /
        divide() # runs the fuction divide

    elif "+" in compare: # looks for +
        add() # runs the fuction add

    elif "-" in compare: # looks for -
        subtract() # runs the fuction subtract

    elif "email" in compare: # looks for email in the word compare
        email() # runs the function email

    elif "lock" in compare and "computer" in compare: # looks for the word lock and computer in compare
        lock() # runs the function lock

    else: # provides a last path for the algorithm to run
        search()
    root.wm_state ('iconic') # sets the window back to minimised when it is no longer needed


    root.iconify() # sets the window back to minimised when it is no longer needed


with open("C:/worksop collage/computing/python/a level/Smart Assistant/check.txt")as file:
    check = file.read()
if check != "1":
    store()#running the store function
    compare()
elif check =="1":
    compare()

# Check if ctrl+1 was pressed
keyboard.add_hotkey('ctrl+1', recognition) # adds a hotkey and runs a function when it is pressed
image = customtkinter.CTkImage(light_image=Image.open("C:/worksop collage/computing/python/a level/Smart Assistant/microphoneImage.png"),
                                  dark_image=Image.open("C:/worksop collage/computing/python/a level/Smart Assistant/microphoneImage.png"),
                                  size=(30, 30))
button = customtkinter.CTkButton(frame, image=image, width= 30, height=50, text="",command =recognition)
button.pack(pady=15,padx=12, expand = True)
root.mainloop() # makes a root window appear when the program is run
a=input()
