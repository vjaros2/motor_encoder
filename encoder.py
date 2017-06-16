
import RPi.GPIO as GPIO
from time import sleep

class encoder:

    CW = 0
    CCW = 1
    
    def __init__(self, clockPin, dataPin, switchPin, rotaryCallback, switchCallback):
        #setup pins
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback

        #setup pins
        GPIO.setup(clockPin, GPIO.IN)
        GPIO.setup(dataPin, GPIO.IN)
        GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
		#start listening
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING, 
		callback=self._clockCallback, bouncetime=40)
        GPIO.add_event_detect(self.switchPin, GPIO.FALLING, 
		callback=self._switchCallback, bouncetime=40)

    def stop(self):
		#stop listening
		#this is superfluous, when gpio pins are shut down they stop listening 
		#on there own. Still nive to have even though it is never really used.
        GPIO.remove_event_detect(self.clockPin)
        GPIO.remove_event_detect(self.switchPin)
    
    def _clockCallback(self, pin):
		#decode the signal and notify
        if GPIO.input(self.clockPin) == 0:
            data = GPIO.input(self.dataPin)
            if data == 0:
                self.rotaryCallback(self.CCW)
            else:
                self.rotaryCallback(self.CW)

    def _switchCallback(self, pin):
		#decode the signal and notify
        if GPIO.input(self.switchPin) == 0:
            self.switchCallback()

