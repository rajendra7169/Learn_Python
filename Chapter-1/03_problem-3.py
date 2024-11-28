# Q-3 install any extermal module and use it
import pyttsx3  # pyttsx3 is an external library so we need to install pyttsx3 first by running "pip install pyttsx3"

engine = pyttsx3.init()
print("Enter the text you want to listen")
text = input()
engine.say(text)
engine.runAndWait()
