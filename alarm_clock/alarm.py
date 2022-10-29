import datetime
from playsound import playsound
alarmHour = int(input('enter hour:'))
alarmMin = int(input('enter minutes:'))
alarmAm = input('am / pm:')

if alarmAm =='pm':
    alarmHour+=12
while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print('playing..')
        playsound('Craig David - 7 Days.mp3')
        break    
