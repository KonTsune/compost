import RPi.GPIO as GPIO
import sys

duty = 80

#GPIO初期設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

p1 = GPIO.PWM(27, 500) #50Hz

p1.start(0)

try:
    while True:
        #「e」キーが押されたら前進
        c = sys.stdin.read(1)
        if c == 'e':
            p1.ChangeDutyCycle(duty)

        #「q」キーが押されたら止まる
        if c == 'q':
            p1.ChangeDutyCycle(0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
