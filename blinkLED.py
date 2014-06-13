GPIO.setmode(GPIO.BOARD)
from time import sleep
import RPi.GPIO as GPIO
GPIO.setup(11, GPIO.OUT)
while 1:
	GPIO.output(11, False)
	sleep(0.5)
	GPIO.output(11, True)
	sleep(0.5)