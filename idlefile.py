import tkinter as tk
import keyboard
import speech_recognition as sr
from AppOpener import open 
import pyttsx3
import pywhatkit as kt
import win32com.client
import ctypes
global ol
global olmailitem


#from mttkinter import mtTkinter 
global window
global mystring
global compare
global num1
global num2 

engine = pyttsx3.init() # creates a new instance 
engine.setProperty('rate', 150) # sets the speaking rate for the engine
window = tk.Tk()
# setting tkinter window size
## set the attributes and dimensions of the screen and where it is placed
window.geometry=('10x20+0+0') #sets the popup window to be in the top left of the screen
window.attributes('-topmost', 1) # sets the window to always be on top
window.attributes('-alpha',0.8) # sets the transparency to slightly seethrough

window.wm_state ('iconic')
window.title("") # names the window
tk.Label(window, text="Hello, I am your digital smart assistant, how may I help?").grid(column=1, row=3) # adds text to the window

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
    frontdone = False # sets frontdone to false so the loop can repeat WWWW
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


def runopen():
    words = compare.split() # splitting the string
    #slicing the list (negative index means index from the end)
    #-1 means the last element of the list
    endwords = (words[-2]) # stores the second to last word 
    endwords = endwords + (words[-1]) # stores the endword in the variable endword 
    endword = (words [-1]) # stores the last word in a varaible 
    open (str(endwords), match_closest= True, output = False) # trys to open a app with the name of the endoword 
    engine.say ("opening" + str(endword))# says what the output to the calculation is 
    engine.runAndWait()# initilises the text to speech and makes it run 
    tk.Label(window, text = "you said: ")
    tk.Label(window, text=compare).grid(column=1, row=3) # adds text to the window



def email():
    ol=win32com.client.Dispatch("outlook.application")
    olmailitem=0x0 #size of the new email
    newmail=ol.CreateItem(olmailitem)# creates a new email 
    # asking what the subject of the email should be 
    r = sr.Recognizer() # creates new instance which represents a collection of speech recognition
    with sr.Microphone() as source: # sets the microphone on the computer as a source   
        global subject
        r.adjust_for_ambient_noise(source) # adjusts the recording for aimbient noise from the surroundings
        engine.say ("what would you like the subject of the email to be")# says the text 
        engine.runAndWait()# initilises the text to speech and makes it run 
        audio = r.listen(source) # records a phrase and stores it in the variable audio

        subject = r.recognize_google(audio) # stores what the user says in a variable
        newmail.Subject= subject# asks what the subject of the email should be
    # asking who the emial should be sent to 
    r = sr.Recognizer() # creates new instance which represents a collection of speech recognition
    with sr.Microphone() as source: # sets the microphone on the computer as a source   
        r.adjust_for_ambient_noise(source) # adjusts the recording for aimbient noise from the surroundings
        engine.say ("who would you like to send the email to")# says whatever is in the brackets
        engine.runAndWait()# initilises the text to speech and makes it run 
        audio = r.listen(source) # records a phrase and stores it in the variable audio
        send = r.recognize_google(audio) # stores what the user says in a variable
        newmail.To= send # asks who it would want to be sent to 
    #asking what the main body of the email should say
    r = sr.Recognizer() # creates new instance which represents a collection of speech recognition
    with sr.Microphone() as source: # sets the microphone on the computer as a source   
        r.adjust_for_ambient_noise(source) # adjusts the recording for aimbient noise from the surroundings
        engine.say ("What would you like to say in the email")# says whatever is in the brackets
        engine.runAndWait()# initilises the text to speech and makes it run 
        audio = r.listen(source,timeout=10) # records a phrase and stores it in the variable audio
        body = r.recognize_google(audio) # stores what the user says in a variable
        newmail.To= send # asks who it would want to be sent to 
    newmail.Body= body #inputs whatever is in the variable body into the body of the email
    engine.say("email created, please check to make sure i understood everything correctly. Especially the email address of the reciever. ")
    engine.runAndWait()
    newmail.Display() # displayes the new email on screen

def lock():
    ctypes.windll.user32.LockWorkStation() # locks the computer 

    
def recognition(): #defines a new funcion that will be used for speech recognition
    global window
    window.wm_state('normal')
    #window.attributes('-topmost', 1) # sets the window to always be on top
    #window.attributes('-alpha',0.5) # sets the transparency to half
    r = sr.Recognizer() # creates new instance which represents a collection of speech recognitio
    with sr.Microphone() as source: # sets the microphone on the computer as a source   
        global compare
        r.adjust_for_ambient_noise(source) # adjusts the recording for aimbient noise from the surroundings
        engine.say ("i'm listening")# says the word hello
        engine.runAndWait()# initilises the text to speech and makes it run 
        audio = r.listen(source, timeout=5) # records a phrase and stores it in the variable audio

        #try:
        compare = r.recognize_google(audio) # stores what the user says in a variable 
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
            kt.search(compare) # perfomes a google search for whatever is in compare
            engine.say ("here is what i found on the web")# says what the output to the calculation is 
            engine.runAndWait()# initilises the text to speech and makes it run 
        
        window.wm_state ('iconic') # sets the window back to minimised when it is no longer needed 


    window.wm_state ('iconic') # sets the window back to minimised when it is no longer needed 

# Check if ctrl+1 was pressed
keyboard.add_hotkey('ctrl+1', recognition) # adds a hotkey and runs a function when it is pressed 
window.mainloop() # makes a root window appear when the program is run 
a=input()
