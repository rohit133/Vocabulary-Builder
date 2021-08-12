import time 
import requests 
import vocabulary as vol
from win10toast import ToastNotifier
import schedule 


def notify():
    # initilizing the Words 
    toaster = ToastNotifier()
    word = vol.get_word()
    meaning = None

    # calling Function
    try:
        meaning = vol.get_meaning()
    except:
        print("Please! Check your internet connection")

    results = "Word :"+word.capitalize() +"\n" +"Meaning: "+str(meaning)

    # Creating Notification

    toaster.show_toast("Vocabulary Builder\n",results,icon_path ="E:\github\Vocabulary-Builder\icon\icon.ico",duration=30)


schedule.every(2).hours.do(notify)
while 1:
    schedule.run_pending()
    time.sleep(1)

