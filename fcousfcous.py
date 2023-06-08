import time
from playsound import playsound

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(minutes, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Focus complete!")
    playsound('alarm.mp3') # Replace 'alarm.mp3' with the path to your own alarm sound file

# Set your desired focus time in minutes
focus_timer(25) # 25 minutes of focus time
