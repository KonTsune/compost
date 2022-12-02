import subprocess

temp = 2
hum = 2

# result = subprocess.run(['python3', '/home/compost/compost/code/hard-data-transmission/main.py', 'add', '-i', '{}'.format(temp), '{}'.format(hum)])
result = subprocess.run(['python3', '/home/compost/compost/code/hard-data-transmission/main.py', 'add', '-i', '2', '3'])

print(result)
