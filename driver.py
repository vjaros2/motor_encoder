import signal
import sys
import encoder
import stepper
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

CLOCKPIN = 5
DATAPIN = 6
SWITCHPIN = 13
STEP = 17
DIRECTION = 27
ENABLE = 22



def signal_handler(signal, frame):
	GPIO.cleanup()
	sys.exit(42)

def rotate(direction):
	print("turned - " + str(direction))
	motor.step(20, direction)
	
def press():
	print("button pressed")

ky040 = encoder.encoder(CLOCKPIN, DATAPIN, SWITCHPIN, rotate, press)
motor = stepper.stepper(STEP,DIRECTION,ENABLE)

#test
if __name__ == "__main__":
	
	signal.signal(signal.SIGINT, signal_handler)	

	

	

	

	

	ky040.start()

	while True:
		sleep(0.001)
	
		
		

