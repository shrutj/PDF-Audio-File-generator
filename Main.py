import PyPDF2 # for pdf operations -pdfreader -extract_text -pages
#import pyttsx3
from gtts import gTTS # text to speech -gTTS -save
import os
from tkinter.filedialog import *  # - askopenfilename
from googletrans import Translator #

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)
num_of_chap= int(input("Enter the number of chapters: "))

for i in range(0, num_of_chap): # dividing chapters
    j=str(i+1)
    sp=int(input("Enter the starting page of chapter "+ j+": "))
    ep=int(input("Enter the ending page of chapter "+ j+": "))
    text=""
    for num in range(sp-1, ep): # extracting text and creating audio file
        page = pdfreader.pages[num]
        aptext=page.extract_text()
        text=text+aptext
        """player = pyttsx3.init()
        player.say(text)
        player.runAndWait()"""
    obj = gTTS(text=text, lang="en", slow=False)
    obj.save(j+"sample.mp3")
    os.system(j+"sample.mp3")

