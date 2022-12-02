# 土壌水分をセンシングし表示する

from gpiozero import MCP3002

Vref = 3.3

# 土壌水分(hum)を返す
def read_hum():
    sen0193 =sen0193 = MCP3002(channel=0)
    hum = float(round(sen0193.value * Vref * 100,2))
    return hum

print(read_hum())
