# 土壌水分をセンシングし連続で表示する

import time
import subprocess
from gpiozero import MCP3002

Vref = 3.3
try:
    while True:
        sen0193 = MCP3002(channel=0)
        hum = round(sen0193.value * Vref * 100,2)
        print(str(hum))
        time.sleep(5)
except: KeyboardInterrupt
subprocess.call('clear')
