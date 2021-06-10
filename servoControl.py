import RPi.GPIO as GPIO
from _thread import *
import time
 

GPIO.setwarnings(False)

class servoController():

	def __init__(self, servoPIN, content):
		self.servoPIN = servoPIN
		self.desc = content
		print(self.desc +  ' has been set to ' + str(self.servoPIN))

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.servoPIN, GPIO.OUT)

		self.servo = GPIO.PWM(self.servoPIN, 50)
		self.servo.start(0)


	def calibrate(self):
		self.servo.ChangeDutyCycle(7.5)
		print('calibrated' + self.desc)
		time.sleep(1)


	def get_pwm(self, angle):
		return (angle/18.0) + 2.5


	def move(self, degrees):
		self.servo.ChangeDutyCycle(self.get_pwm(degrees))
		print('moved ' + self.desc + ' ' + str(degrees) + ' degrees')
		time.sleep(1)
		
		

