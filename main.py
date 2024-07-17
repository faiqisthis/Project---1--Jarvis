import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import sys
from youtubesearchpython import VideosSearch
# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Create a Recognizer instance
recognizer = sr.Recognizer()

def play_on_Youtube(text):
   filtered_text=text.replace("play ","")
   speak(f"Playing {filtered_text}")
   videos_search = VideosSearch(filtered_text, limit=1)
   video_result = videos_search.result()
   video_url = video_result['result'][0]['link']
   webbrowser.open(video_url)

def open_on_Browser(text):
 if (text == "open google" or text =="open facebook" or text =="open youtube" or text == "open linkedin" or text == "open instagram" or text=="open tiktok" or text=="open twitter"):
   text= text.replace("open ","")
   speak(f"Opening {text}")
   webbrowser.open(f"https://www.{text}.com")

 elif(text.endswith(".com") or text.endswith(".pk")):
   text= text.replace("open ","")
   speak(f"Opening {text}")
   webbrowser.open(f"https://{text}")
 
 
def understandCommand(text):
  print("You said:", text)
  text=text.lower()
  if(text=="jarvis"):
   speak("Yes")
  elif(text=="open my computer" or text=="open this pc"):
   filtered_text=text.replace("open","")
   speak(f"Opening {filtered_text}")
   os.system("explorer shell:MyComputerFolder") 
  elif(text=="open spotify"):
   filtered_text=text.replace("open","")
   speak(f"Opening {filtered_text}")
   os.system("spotify.exe") 
  elif("open" in text):
   open_on_Browser(text)
  elif("play" in text):
   play_on_Youtube(text)
  elif(text=="exit"):
   speak("Okay")
   sys.exit()

# Capture audio input from the microphone
# Perform speech recognition using Google Web Speech API
while True:
 try:
  with sr.Microphone() as source:
   print("Speak something...")
   command = recognizer.listen(source,timeout=1,phrase_time_limit=3)
   text = recognizer.recognize_google(command)
   understandCommand(text)
   
 except sr.UnknownValueError:
  print("Sorry, could not understand audio.")
 except sr.RequestError as e:
  print("Error: Could not request results from Google Speech Recognition service;")

