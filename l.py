import speech_recognition as sr
import pyttsx3
from openai_request import send_request

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Voice output function
def speak(text):
    print("JARVIS:", text)
    tts_engine.say(text)
    tts_engine.runAndWait()

# Voice input function
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Could not request results from Google Speech Recognition.")
            return None

# Main loop
def main_process():
    while True:
        query = listen()
        if query:
            if "exit" in query.lower() or "quit" in query.lower():
                speak("Goodbye!")
                break
            response = send_request(query)
            speak(response)

if __name__ == "__main__":
    main_process()
