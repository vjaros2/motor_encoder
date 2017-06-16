from time import sleep
import RPi.GPIO as gpio

class stepper:
	#instantiate stepper 
	def __init__(self, stepPin, directionPin, enablePin):
		#setup pins
		self.stepPin = stepPin
		self.directionPin = directionPin
		self.enablePin = enablePin
		
		#set gpio pins
		gpio.setup(self.stepPin, gpio.OUT)
		gpio.setup(self.directionPin, gpio.OUT)
		gpio.setup(self.enablePin, gpio.OUT)
		
		#set motor to low power mode
		gpio.output(self.enablePin, True)
	


	# steps = number of steps
	# dir = direction
	# speed = defines waitTime equation: waitTime = 0.000001/speed. 
	# stayOn = defines whether the stepper should stay awake or not
	def step(self, steps, dir, speed=1, stayOn=False):
		#wake up motor
		gpio.output(self.enablePin, False)
		
		#set the output to true for cw and false for ccw
		#cw stands for clock-wise
		cw = True
		if (dir == 1):
			cw = False;
		elif (dir != 0):
			print("No Direction Supplied")
			return False
		gpio.output(self.directionPin, not cw)
		
		stepCounter = 0
	
		waitTime = 0.000001/speed #waitTime controls speed

		while stepCounter < steps:
			#turning the gpio on and off tells the easy driver to take one step
			gpio.output(self.stepPin, True)
			gpio.output(self.stepPin, False)
			stepCounter += 1
 
			#wait before taking the next step thus controlling rotation speed
			sleep(waitTime)
		
		if (stayOn == False):
			#motor reenters low power mode if necessary
			gpio.output(self.enablePin, True)

		#print("stepperDriver complete (turned " + str(dir) + " " + str(steps) + " steps)")
		
