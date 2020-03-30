import network, machine, time, socket, sys, HTS221
from bh1750 import BH1750
import HTS221

print('RUN: Finished importing')

def connect():
    conn = network.WLAN(network.STA_IF)

    if not conn.isconnected():
        print('connecting to wifi...')
        conn.active(True)
        conn.connect('ssid', 'pass')
        while not conn.isconnected():
            pass
        print('network config:', conn.ifconfig())

def post(data, url):
    _, _, host, path = url.split('/', 3)
    address = socket.getaddrinfo(host, 8000)[0][-1]
    s = socket.socket()
    s.connect(address)
    
    header = 'POST /{} HTTP/1.0\r\nHost: {}'.format(path, host)
    payload = ''

    s.send(bytes('%s%s'%(header,payload), 'utf-8'))
    s.close()

scl = machine.Pin(5)
sda = machine.Pin(4)
i2c = machine.I2C(scl,sda)

lux_sensor = BH1750(i2c)
hts = HTS221.HTS221()

while True:
    lux_value = lux_sensor.luminance(BH1750.ONCE_HIRES_1)
    temp_value = hts.readTemp()
    print('lux:', lux_value,'\n')
    print('temp:', temp_value,'\n')
    time.sleep(2)