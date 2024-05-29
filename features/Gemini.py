import pyttsx3
import speech_recognition as sr
import google.generativeai as genai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use index 1 for female voice

# Define a function to speak out the given text
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()

    # Adjust recognizer settings
    r.energy_threshold = 4000  # Adjust energy threshold as needed
    r.dynamic_energy_threshold = True  # Enable dynamic energy threshold

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=10)  # Adjust timeout and phrase time limit
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-IN')
            print(f"User said: {query}\n")
        except Exception as e:
            speak("Unable to recognize your voice...")
            return "none"
        query = query.lower()
        return query

chatStr = ""

def chat(order):
    global chatStr
    # print(chatStr)
    chatStr += f"Boss: {order}\n Melody: "
    genai.configure(api_key="AIzaSyC0IIbk9HpSkHxerynC6F2bVtIEfsQjZKs")

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 512,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message(order)
    response = convo.last.text.replace('*', '')  # Remove asterisks from the response
    # print(response)
    speak(response)

    chatStr += f"{response}\n"
    return response

# while True:
#     user_input = takeCommand().strip()
#     if user_input.lower() == 'exit':
#         break
#     bot_response = chat(user_input)
#     chatStr += f"Melody: {bot_response}\n"

# After the conversation loop ends, you can print or speak the entire conversation log
# print(chatStr)
# speak(chatStr)  # If you want to speak out the conversation
