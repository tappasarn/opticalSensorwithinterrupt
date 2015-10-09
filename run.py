import RPi.GPIO as GPIO
import time

# be careful mode is BCM not board
GPIO.setmode(GPIO.BCM)
# set GPIO 4 (or pin 7) as input port
optical_sensors = 4
GPIO.setup(optical_sensors, GPIO.IN)


while True:
    if GPIO.input(optical_sensors) == GPIO.LOW:
        print(" ")
    else:
        print("SENSORS CATCH LIGHT!!!!!!!!!")
        time.sleep(0.75)

