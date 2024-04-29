import speech_recognition as sr
import requests

def recognize_speech(recognizer, microphone):
    print("Listening...")
    with microphone as source:
        audio_data = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def startup():
    print("Say 'Gaurdian' to activate the bot.")
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    while True:
        text = recognize_speech(recognizer, microphone)
        if text == "Gaurdian":
            print("Activated!")
            recognize_speech_loop(recognizer, microphone)
        elif text == "stop":
            print("Stopping...")
            break

def recognize_speech_loop(recognizer, microphone):
    while True:
        text = recognize_speech(recognizer, microphone)
        if text == "stop":
            print("Stopping...")
            break
        elif text == "what is your name":
            print("My name is Gaudian and I am a speech recognition bot. I am here to help you with your tasks.")
        elif text == "what is the time":
            print("Sorry, I am not connected to the internet. I cannot provide the current time.")
        elif text == "what is the date":
            print("Sorry, I am not connected to the internet. I cannot provide the current date.")

        elif text == "How many servers does Arcane Magica Have":
            ## make a  request to https://arcane-magica.com/api/get/online
            ## get the response and print it
            reponse = requests.get("https://arcane-magica.com/api/get/online")
            print(f"Arcane Magica has {reponse.length} servers online.")

        elif text == "what is your purpose":
            print("I am a speech recognition bot created by TheRavenSeb. I am here to help you with your tasks and for you to upgrade as you learn my langagues.")
            

        elif text is not None:
            print("You said: " + text)

            
# Call the function to start speech recognition
startup()
