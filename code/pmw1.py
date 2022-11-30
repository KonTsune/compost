import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

PWM = 13

GPIO.setup(PWM, GPIO.OUT)

p = GPIO.PWM(PWM, 100)
p.start(0)


for i in range(20, 101, 20):
	p.ChangeDutyCycle(i)
	print(i)
	time.sleep(5)

p.ChangeDutyCycle(0)
print('done')

GPIO.cleanup(PWM)
