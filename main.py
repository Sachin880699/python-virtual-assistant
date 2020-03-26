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
        data = r.recognize_google(audio,language = 'mr-IN')
        with open('temp_command.txt','w') as file_save_data:
            file_save_data.write(data)

        with open('command.txt') as f:
            command = [line.rstrip() for line in f]
            print(command)
            if data in command:
                print('ok')

                command = command.index(data)
                with open('answer.txt') as f:
                    lines = [line.rstrip() for line in f]
                    print(command)
                    print(lines[command])
            else:
                data =data
                if data=="बारा आहे":
                    print('okkkkkkkkkkkkkkkkkkk')






        
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
        
        
        
main()
