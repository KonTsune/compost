import subprocess

temp = float(2.3)
hum = float(2.2)

result = subprocess.run(['python3', '/home/compost/compost/code/hard-data-transmission/main.py', 'add', '-i', '{}'.format(temp), '{}'.format(hum)])
#result = subprocess.run(['python3', '/home/compost/compost/code/hard-data-transmission/main.py', 'add', '-i', '1', '2'])

print(result)
