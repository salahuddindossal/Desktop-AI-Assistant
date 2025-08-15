# Desktop-AI-Assistant

I’ve developed an AI model and integrated it into a desktop assistant capable of performing multiple tasks such as opening YouTube, Google, WhatsApp, searching for songs, and more.
It uses a predefined script structure, allowing users to interact with it naturally and easily.

In the future, I plan to enhance it further to function more like ChatGPT—possibly by integrating APIs—but I intend to build most of it on my own.
I also aim to expand its capabilities to include features like setting alarms, creating to-do lists and reminders, sending messages, and handling other personalized tasks.

Eventually, I want to bring this assistant to mobile devices as a fully functional phone app. 

# How It Works
This is a pre-scripted, voice-controlled desktop assistant that executes specific commands based on user input.
For example, if you say "open YouTube", the program will automatically launch YouTube. Similarly, it can open other platforms such as Google or search for songs — this is achieved using Python’s webbrowser module.

In addition to performing tasks, the assistant can also engage in basic conversation. I’ve integrated predefined question–answer pairs, so if the user asks something like:

User: What is your name?
Assistant: My name is Jarvis.

This makes the assistant interactive and capable of handling both functional and conversational tasks.

# Modules I used
import speech_recognition as sr      # For converting speech to text (speech recognition)
import win32com.client               # For text-to-speech functionality on Windows
import webbrowser                    # For handling tasks like opening YouTube, Google, etc. in the browser
import os                            # For interacting with the operating system (automating tasks, file operations)
import datetime                      # For working with and displaying the current date & time



