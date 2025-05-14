import pyttsx3
import speech_recognition as sr
import random 
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit
import user_config
import smtplib,ssl
import openai_request as ai


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    print("Bot:", audio)
    engine.say(audio)
    engine.runAndWait()

def commond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        content = r.recognize_google(audio, language='en-in')
        print("You said:", content)
        return content
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return ""
    except sr.RequestError:
        speak("Sorry, the speech service is down.")
        return ""

def main_process():
    jarvis_chat=[]
    speak("Hello! I'm your assistant. How can I help you?")
    while True:    
        request = commond().lower()

        if request == "":
            continue

        elif "hello" in request:
            speak("Hi, how are you?")
        
        elif "play music" in request:
            speak("Playing Music")
            song = random.randint(1,5)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=PMzTLWTWLZU")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=TMY1g8pAktk") 
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=fclPhO1FsOY") 
            elif song == 4:
                webbrowser.open("https://www.youtube.com/watch?v=EcdswCLAIKU") 
            else:
                webbrowser.open("https://www.youtube.com/watch?v=mTuPDGFboNU&list=PLjity7Lwv-zo0QYOdDVzVKTMTdpIVh6Xw")  

        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + now_time)

        elif "say date" in request:
            now_date = datetime.datetime.now().strftime("%d-%m-%Y")
            speak("Today's date is " + now_date)  

        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task != "":
                speak("Adding task: " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")

        elif "speak task" in request:
            with open("todo.txt","r") as file:
                speak("work we have to do today is: "+file.read())   

        elif "show work" in request:
            with open("todo.txt","r") as file:
                tasks=file.read()  
            notification.notify(
                title="today's work",
                message =tasks
            )  
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")         
        elif "open" in request:
            query = request.replace("open", "").strip()
            if query:
                speak(f"Opening {query}")
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter")
            else:
                speak("Please specify the app to open.")
        
        elif "wikipedia" in request:
            try:
                request = request.replace("jarvis", "").replace("search wikipedia", "").strip()
                result = wikipedia.summary(request, sentences=1)
                print(result)
                speak(result)
            except Exception as e:
                speak("Sorry, I couldn't find anything on Wikipedia.")

           
        elif " search google" in request:
            request = request.replace("jarvis", "")
            request =request.replace("search google"," ").strip()
            webbrowser.open("https://www.google.com/search?q="+request)

        elif "send message" in request:
            pywhatkit.sendwhatmsg("+918951124048", "Hi",20,25,30)
        # elif "send email" in request:
        #     pywhatkit.send_hmail(email_sender: str, password: str, subject: str, html_code: str, email_receiver: str) -> None    
        elif "send email" in request:
            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("lokeshsnatikar@gmail.com", user_config.gmail_password)
                message = "This is a message"
                s.sendmail("lokeshsnatikar@gmail.com", "mailu143natikar@gmail.com", message)
                s.quit()
                speak("Email sent")
            except Exception as e:
                print(e)
                speak("Failed to send email.")


        elif "ask chatgpt" in request:
            jarvis_chat=[]
            request = request.replace("jarvis", "")
            request =request.replace("ask chatgpt"," ").strip()
            jarvis_chat.append({"role":"user","content":request})
            response=ai.send_request(jarvis_chat)
            speak(response)
        # elif "clear chat" in request:
        #     jarvis_chat =[]
        #     speak("chat cleared")
        # else:
        #     request=request.replace("jarvis"," ")  
        #     jarvis_chat.append({"role":"user","content":request})
        #     print(jarvis_chat)
        #     response=ai.send_request(jarvis_chat)
            
        #     jarvis_chat.append({"role":"assistant","content":response})
        #     print(jarvis_chat)
        #     speak(response) 



            

        elif "exit" in request or "quit" in request:
            speak("Goodbye! Have a great day!")
            break

# Start the assistant
main_process()
