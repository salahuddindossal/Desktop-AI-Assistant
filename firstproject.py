import speech_recognition as sr
import win32com.client
import webbrowser
import os 
import datetime
import tkinter as tk
from tkinter import scrolledtextAnna Claire Clouds
import threading





speaker = win32com.client.Dispatch("SAPI.SpVoice")







def say(text):
   s=(f" {text}")
   speaker.Speak(s)

def play_song(song_name):
    search_query = f"youtube.com/results?search_query={song_name.replace(' ', '+')}"
    webbrowser.open(search_query)
def searches(search):
    search_query = f"youtube.com/results?search_query={search.replace(' ', '+')}"
    webbrowser.open(search_query)
def Gsearches(gsearch):
    search_query = f"google.com/results?search_query={gsearch.replace(' ', '+')}"
    webbrowser.open(search_query)
def takecommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      r.pause_threshold =  1
      audio = r.listen(source)
      try:
         print("Recognizing...")
         query = r.recognize_google(audio, language="en-in")
         print(f"User said: {query}")

         return query

      except Exception as e:
         return "Some Error Occurred. Sorry from Jarvis"



while 1:
   print("Pycharm")
   say("hello i am jarvis AI. How can i help you.")
   while True:
     print("Listning...")
     query = takecommand()

     sites=[["youtube", "https://youtube.com"],["google", "https://google.com"], ["instagram", "https://instagram.com"], ["whatsapp web", "https://web.whatsapp.com"]]

     for site in sites:
       if f"open {site[0]}".lower() in query.lower():

         say(f"opening {site[0]} sir...")
         webbrowser.open(site[1])

     #say(query)
       elif "the time" in query:
           hour = datetime.datetime.now().strftime("%H")
           min = datetime.datetime.now().strftime("%M")
           say(f"Sir time is {hour} bajke {min} minutes")

       if f"activate search engine".lower() in query.lower():
           say("what should i search sir?")
           print("Listning...")
           query = takecommand()
           for url in search(query, tld="co.in", num=10, stop=10, pause=2):
               print(query)
               webbrowser.open(query)
     if f"speak to me".lower() in query.lower():
         say("what should i say sir")
         print("Listning...")
         query = takecommand()

     if f"how are you".lower() in query.lower():
             say("I am fine sir, how are you")
     if f"i am also fine".lower() in query.lower():
         say("thats nice")
     if f"my name".lower() in query.lower():
         say("okay what is your name")
     if f"my name is".lower() in query.lower():
         say("okay")
     if f"what is your name".lower() in query.lower():
         say("My name is Jarvis AI")

     if f"exit".lower() in query.lower():
         say("Thank you sir")

     if f"song".lower() in query.lower():
         say("What song would you like to listen to?")
         say("app kia suna chate hai")
         print("Listning...")
         song_name = takecommand()
         say(f"playing {takecommand()}")
         play_song(song_name)
     elif f"exit".lower() in query.lower():
         say("Goodbye!")
         break



     if f"on youtube".lower() in query.lower():
         say("What would you like to search to?")
         say("app kia dekhna chate ho")
         print("Listning...")
         search = takecommand()
         say(f"searching {takecommand()}")
         searches(search)
     elif f"exit".lower() in query.lower():
         say("Goodbye!")
         break




