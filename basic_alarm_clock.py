import datetime
import time
import os

Alarm_time = input("Enter alarm time(HH.MM) : ")
print(f"Alarm set for {Alarm_time} . Waiting😊...")

if os.name == 'nt':
 import winsound
 
now = datetime.datetime.now().strftime("%H.%M")
if Alarm_time < now:
        print("That time has already passed. Please try again😔...")
else:
 while True:
    now = datetime.datetime.now().strftime("%H.%M")
    if now == Alarm_time :
        print("Wake up... Wake up... Time Is Ok⏰___")
       
        
        for _ in range (5):
            if os.name == 'nt':
             winsound.Beep(1000,500)
            else:
                print('/a')
            time.sleep(1)
        break
    time.sleep(10)             
