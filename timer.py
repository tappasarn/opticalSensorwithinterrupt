import time
import signal
import RPi.GPIO as GPIO

#set GIOP mode and pin here
GPIO.setmode(GPIO.BCM)
#by some reason, we need to pull up the signal or else result will not be correct
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#init count as 0
count = 0


#this method will be call if there is an even interrupt on the optical senson 
def my_callback():  
    global count
    #this line just simply increase number of count each time the interrupt happen
    count = count + 1 
    

#this method will be called by timmer (or signal) after a period of time
def catcher(signum, _):
    global count
    print "count per 2 sec= ",count
    count = 0


#set signal timmer
signal.signal(signal.SIGALRM, catcher)

#set timmer or x sec however the first number is for second and second number is for interval
#I dont know how they are different but keeping them the same allow the code to work fine
signal.setitimer(signal.ITIMER_REAL, 4, 4)

#add interrupt detector here
GPIO.add_event_detect(4, GPIO.RISING, callback=my_callback)  


while True:
    pass


