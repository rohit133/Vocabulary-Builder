import time 
import requests 
import vocabulary as vol
from win10toast import ToastNotifier

# initilizing the Words 
toaster = ToastNotifier()
word = vol.get_word()
meaning = None

# calling Function
try:
    meaning = vol.get_meaning()
except:
    print("Please! Check your internet connection")

results = "Word :"+word.upper() +"\n" +"Meaning: "+str(meaning)

# Creating Notification
toaster.show_toast("\n",
results,
icon_path="bell-Icon.ico",
duration=30)


