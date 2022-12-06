import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

PWM = 13

GPIO.setup(PWM, GPIO.OUT)

p = GPIO.PWM(PWM, 100)
p.start(0)

status = 0
while status < 100:
	p.ChangeDutyCycle(status)
	time.sleep(1)
	status += 10
	print(status)


p.ChangeDutyCycle(status)
time.sleep(3)
print(status)

while status > 0:
	p.ChangeDutyCycle(status)
	time.sleep(1)
	status -= 10
	print(status)

p.ChangeDutyCycle(0)
print('done')

GPIO.cleanup(PWM)
