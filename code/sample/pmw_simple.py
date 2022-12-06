import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

PWM = 13

GPIO.setup(PWM, GPIO.OUT)

p = GPIO.PWM(PWM, 500)
p.start(0)

l = []

for i in range(0, 1000, 1):
    l.append(i)

for i in range(1000, -1, -1):
    l.append(i)

for i in l:
	power = i / 10
	if i != 1000:
		p.ChangeDutyCycle(power)
		time.sleep(0.01)

	else:
		p.ChangeDutyCycle(power)
		time.sleep(10)


p.ChangeDutyCycle(0)
print('done')

GPIO.cleanup(PWM)
