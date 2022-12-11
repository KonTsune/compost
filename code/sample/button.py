# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys, os
from pmw_simple import pmw

# ボタンを押したらプログラムを呼び出す
if __name__ == "__main__":
	# GPIOピン番号設定
	pin1 = 22

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)

	while True:
		button1 = GPIO.input(pin1)

		cmd = ""
		if button1 == False:
			# ボタン1の処理
			pmw()

		time.sleep(0.1)

	GPIO.cleanup()
