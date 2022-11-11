import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

PWM = 13

GPIO.setup(PWM, GPIO.OUT)

p = GPIO.PWM(PWM, 100)
p.start(0)


for i in range(10, 101, 10):
	p.ChangeDutyCycle(i)
	print(i)
	time.sleep(2)

p.ChangeDutyCycle(0)
print('done')

GPIO.cleanup(PWM)
