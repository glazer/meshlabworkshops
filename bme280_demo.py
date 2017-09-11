import sys,time,traceback
from os.path import expanduser
sys.path.append(expanduser('~'))
from datetime import datetime
from node.drivers.Adafruit_BME280 import BME280_sl,BME280_OSAMPLE_8
from node.drivers.lcd20x4 import *

bus = 1

bme = BME280_sl(bus=bus,mode=BME280_OSAMPLE_8,address=0x76)
lcd = LCD(bus=1,address=0x3f)
lcd.backlight(True)

while True:
    try:
        R = {}

        R['ts'] = datetime.utcnow()
        r = bme.read()
        R['kPa'] = r['p']
        R['Deg.C'] = r['t']
        R['%RH'] = r['rh']

        lcd.write_lines([str(R['ts'])[0:19],
                         '{:.1f} deg C'.format(r['t']),
                         '{:.1f} % RH'.format(r['rh']),
                         '{:.2f} kPa'.format(r['p'])])
        time.sleep(1)
    except KeyboardInterrupt:
        break
    except:
        traceback.print_exc()

