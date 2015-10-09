import RPi.GPIO as GPIO
import time
import signal

# use BCM mode any problem look up BCM vs BOARD
GPIO.setmode(GPIO.BCM)
# keep signal at 0 and wait for signal 1 to arrive
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# init count as 0
count = 0


# the chatcher catch 2 sec
def catcher(signum, _):
    print "aHH 2 sec pass"
    signal.alarm(2)

# set up signal timmer
signal.signal(signal.SIGALRM, catcher)
signal.alarm(2)


while True:
    print "Waiting for high signal"
    try:
        GPIO.wait_for_edge(4, GPIO.RISING)
        count += 1
        print "\nRising edge detected. Now your program can continue with"
        print "this is ur current count: ", count
    except KeyboardInterrupt:
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit
    # GPIO.cleanup()           # clean up GPIO on normal exit

