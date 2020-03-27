import speech_recognition as sr  
from time import sleep
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import pandas as pd
import random



#---------------------text to speech site is open---------
driver = webdriver.Chrome('/home/sachin/Desktop/chromedriver')
driver.get('https://texttospeech.io/')
print("Site is open")
sleep(5)
'''audio_text_file = "नमस्ते इस virtual communication technology मे आपका  स्वागत हें. मे अपने सारे system protocol  को activate कर रही हू.इस में थोडा वक्त लग sakta हें. . . . . .  . . .  . system is ready  to use "
username_box = driver.find_element_by_id('speech-msg')
username_box.send_keys(audio_text_file)
print("Message is type")
select_fr = Select(driver.find_element_by_id("voice"))
select_fr.select_by_index(39)
data = driver.find_element_by_id('btnSpeak').click()
username_box = driver.find_element_by_id('speech-msg').clear()'''


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
                    audio_text_file = lines[command]

                    username_box = driver.find_element_by_id('speech-msg')
                    username_box.send_keys(audio_text_file)
                    print("Message is type")
                    select_fr = Select(driver.find_element_by_id("voice"))
                    select_fr.select_by_index(39)
                    data = driver.find_element_by_id('btnSpeak').click()
                    username_box = driver.find_element_by_id('speech-msg').clear()

                    main()







            else:
                with open('temp_command.txt')as f:
                    data = f.read()

                    if data=='किती वाजलेत':
                        hour = pd.datetime.now().hour
                        minute = pd.datetime.now().minute

                        username_box = driver.find_element_by_id('speech-msg')
                        username_box.send_keys(hour,'वाजून',minute,'मिनिटे')
                        print("Message is type")
                        select_fr = Select(driver.find_element_by_id("voice"))
                        select_fr.select_by_index(39)
                        data = driver.find_element_by_id('btnSpeak').click()
                        username_box = driver.find_element_by_id('speech-msg').clear()
                        main()
                    if data=='मराठी विनोद' or data=='मराठी जोके' or data=='जोके' or data=='विनोद':
                        with open('joke.txt') as f:
                            command = [line.rstrip() for line in f]
                            joke = random.choice(command)


                        username_box = driver.find_element_by_id('speech-msg')
                        username_box.send_keys(joke)
                        print("Message is type")
                        select_fr = Select(driver.find_element_by_id("voice"))
                        select_fr.select_by_index(39)
                        data = driver.find_element_by_id('btnSpeak').click()
                        username_box = driver.find_element_by_id('speech-msg').clear()
                        sleep(5)
                        main()






        
    except sr.UnknownValueError:
        print("Could not understand audio")
        main()
    except sr.RequestError as e:
        main()
        print("Could not request results; {0}".format(e))
        
        
        
        
main()
