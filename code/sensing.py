import glob
import os
import subprocess
from time import sleep
from gpiozero import MCP3002

# 以下温度センシング
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

# 温度(temp)を返す
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp = float(temp_string) / 1000.0
        return temp


# 以下土壌水分センシング
Vref = 3.3

# 土壌水分(hum)を返す
def read_hum():
    sen0193 =sen0193 = MCP3002(channel=0)
    hum = float(round(sen0193.value * Vref * 100,2))
    return hum

# データ送信と情報表示
result = subprocess.run(['python3', '/home/compost/compost/code/hard-data-transmission/main.py', 'add', '-i', '{}'.format(read_temp()), '{}'.format(read_hum())])
print(result)
print("温度:", read_temp(), "土壌水分:", read_hum())
