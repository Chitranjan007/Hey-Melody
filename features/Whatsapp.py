import pywhatkit
import pyttsx3
import speech_recognition as sr
from datetime import datetime

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use index 1 for female voice
rate = engine.setProperty("rate", 200)  # Adjust the rate as needed

# Define a function to speak out the given text
def speak(audio):
    try:
        engine.say(audio)
        print(audio)
        engine.runAndWait()
    except RuntimeError:
        pass  # Do nothing if the pyttsx3 engine's run loop is already started

# Define a function to take a command
def takeCommand():
    r = sr.Recognizer()

    # Adjust recognizer settings
    r.energy_threshold = 2000  # Adjust energy threshold as needed (lower values make it more sensitive)
    r.pause_threshold = 0.5  # Adjust pause threshold as needed (lower values detect shorter pauses)
    r.non_speaking_duration = 0.2  # Adjust non-speaking duration as needed
    r.dynamic_energy_threshold = True  # Enable dynamic energy threshold

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.3
        audio = r.listen(source, timeout=10, phrase_time_limit=10)  # Adjust timeout and phrase time limit
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-IN')
            print(f"User said: {query}\n")
            query = query.lower()
            return query
        except sr.UnknownValueError:
            print("Unable to recognize your voice...")
            return ""
        except sr.RequestError:
            print("I'm sorry, I'm having trouble accessing the Google API.")
            return ""


def sendMessage():
    speak("Who do you want to message")
    # recipient = input("Enter the recipient's phone number (without country code): ")
    # recipient_with_country_code = "+91" + recipient

    recipient_with_country_code = "+919835386353"

    speak("What is the message?")
    message = takeCommand()

    pywhatkit.sendwhatmsg(recipient_with_country_code, message, datetime.now().hour, datetime.now().minute + 1)
    print("Message sent successfully!")


# def TaskExecution():
#     while True:
#         order = takeCommand()
#         if "whatsapp" in order:
#             sendMessage()
#
# if __name__ == "__main__":
#     TaskExecution()
