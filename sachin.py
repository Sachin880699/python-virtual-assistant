import speech_recognition as sr  
from time import sleep
# get audio from the microphone                                                                       
r = sr.Recognizer()

def main():
    with sr.Microphone() as source:
        sleep(1)
        print("Say something and wait wait.")
        audio = r.listen(source)
        sleep(1)

    try:
        data = r.recognize_google(audio)
        print(data)
        print('I add this line ')
        
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
        
        
        
main()
