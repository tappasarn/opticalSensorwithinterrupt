import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# keep signal at 0 and wait for signal 1 to arrive
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
count = 0
while True:
    print "Waiting for high signal"
    try:
        GPIO.wait_for_edge(4, GPIO.RISING)
        count +=1
        print count 
    except KeyboardInterrupt:
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit
   # GPIO.cleanup()           # clean up GPIO on normal exit




 

