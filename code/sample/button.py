# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys, os

# ボタンを押したらプログラムを呼び出す
if __name__ == "__main__":
	# GPIOピン番号設定
	pin1 = 15
	pin2 = 21
	pin3 = 29
	pin4 = 35

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(pin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(pin3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(pin4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

	# ボタンクリック待機中
	print("ボタン待機中...")

	while True:
		button1 = GPIO.input(pin1)
		button2 = GPIO.input(pin2)
		button3 = GPIO.input(pin3)
		button4 = GPIO.input(pin4)

		cmd = ""
		if button1 == False:
			# ボタン1の処理
			cmd = "sudo python3 /home/pi/button1.py"	# 例です

		elif button2 == False:
			# ボタン2の処理
			cmd = "sudo python3 /home/pi/button2.py"	# 例です

		elif button3 == False:
			# ボタン3の処理
			cmd = "sudo python3 /home/pi/button3.py"	# 例です

		elif button4 == False:
			# ボタン4の処理
			cmd = "sudo python3 /home/pi/button4.py"	# 例です

		# 実行
		if cmd != "":
			ret = os.popen(cmd).readline().strip()
			print(ret)
			time.sleep(1)	# ボタンを押した後のチャタリング防止のため

		time.sleep(0.1)

	GPIO.cleanup()
