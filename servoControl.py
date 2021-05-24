import RPi.GPIO as GPIO
import time
import threading

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


	def start_new_thread():
		pass


	def calibrate(self):
		self.servo.ChangeDutyCycle(7.5)
		print('calibrated' + self.desc )
		time.sleep(1)



	def get_pwm(self, angle):
		return (angle/18.0) + 2.5


	def move(self, degrees):
		self.servo.ChangeDutyCycle(self.get_pwm(degrees))
		print('moved ' + self.desc + ' '  + str(degrees) + ' degrees')
		time.sleep(1)


runner = servoController(17, 'xAxisServo ' )
runner2 = servoController(23, 'yAxisServo ')
runner.calibrate()
runner2.calibrate()
while True:
	runner.move(0)
	runner2.move(0)
	runner.move(180)
	runner2.move(180)
