import speech_recognition as sr

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
        elif text is not None:
            print("You said: " + text)

# Call the function to start speech recognition
startup()
