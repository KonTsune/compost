import glob
import os
import subprocess
import pickle
import time
import RPi.GPIO as GPIO
from gpiozero import MCP3002

from sample import pmw_simple

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
        time.sleep(0.2)
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

#温度と土壌水分確定
temp = read_temp()
hum = read_hum()

# データ送信と情報表示
result = subprocess.run(['python3', '/home/compost/compost/code/hard-data-transmission/main.py', 'add', '-i', '{}'.format(temp), '{}'.format(hum)])
print(result)

print("温度:", temp, "土壌水分:", hum)

# 温度保存
btemp = [temp]
ave = 0
# temp = 10

def writep(filename, w, mes):
    with open('{}'.format(filename), 'wb') as p:
        pickle.dump(w, p)
        print("{}".format(mes))

def readp(filename, r, mes):
    with open('{}'.format(filename), 'rb') as p:
        a = pickle.load(p)
        print("{}".format(mes))
        return a

def temp_stack():
    if len(btemp) == 5:
        btemp.pop(0)
        btemp.append(temp)
        print("3-1ポップして追加",btemp)
        if temp <= ave-5:
            print("4-1撹拌")
            pmw_simple.pmw()
            mix_list = [1]
            with open('/home/compost/compost/code/mix.bin', 'wb') as p:
                pickle.dump(mix_list, p)
        else:
            print("4-2撹拌してない")
            mix_list = [0]
            with open('/home/compost/compost/code/mix.bin', 'wb') as p:
                pickle.dump(mix_list, p)
    else:
        btemp.append(temp)
        print("3-2追加",btemp)
        print("撹拌")
        pmw_simple.pmw()

filepath = "/home/compost/compost/code/pic.bin"
print(os.path.exists(filepath))
if os.path.exists(filepath) == True:
    with open('/home/compost/compost/code/pic.bin', 'rb') as p:
        btemp = pickle.load(p)
        print("1-1蓄積温度", btemp)
        ave = sum(btemp) / len(btemp)
        print("1-1平均", ave)
        with open('/home/compost/compost/code/mix.bin', 'rb') as p:
            mix = pickle.load(p)
            print("mix_list:", mix[0])
            if mix[0] == 1:
                print("2-1")
                temp_stack()
            else:
                print("2-2")
                temp_stack()
    with open('/home/compost/compost/code/pic.bin', 'wb') as p:
        pickle.dump(btemp, p)
        print("0書き込んだ")
else:
    with open('/home/compost/compost/code/pic.bin', 'wb') as p:
        pickle.dump(btemp, p)
        print("1-2ぴっく作った", btemp)
    mix_list = [1]
    with open('/home/compost/compost/code/mix.bin', 'wb') as p:
        pickle.dump(mix_list, p)
        print("1-2mix_list作った",mix_list)
    print("撹拌")
    pmw_simple.pmw()
