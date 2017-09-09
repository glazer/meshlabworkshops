import sys,time,traceback
from os.path import expanduser
sys.path.append(expanduser('~'))
from datetime import datetime
from node.drivers.bmp280 import BMP280
#from node.drivers.tcs34725 import TCS34725
#from node.drivers.ezo_ec import EZO_EC
#from node.drivers.ezo_do import EZO_DO
#from node.drivers.ezo_ph import EZO_pH
#from node.drivers.ezo_orp import EZO_ORP
#from node.parse_support import pretty_print
from node.drivers.lcd20x4 import *


bus = 1


bme = BME280_sl(bus=bus,mode=BME280_OSAMPLE_8,address=0x76)
lcd = LCD(bus=1,address=0x3f)
lcd.backlight(True)
#rgb = TCS34725(bus=bus)
#rgb.gain(1)                   # {1x,4x,16x,60x}
#rgb.integration_time(2.4)     # {2.4ms,24ms,101ms,154ms,700ms}
#ec = EZO_EC(bus=bus,lowpower=False)
#do = EZO_DO(bus=bus,lowpower=False)
#ph = EZO_pH(bus=bus,lowpower=False)
#orp = EZO_ORP(bus=bus,lowpower=False)

while True:
    try:
        R = {}

        R['ts'] = datetime.utcnow()
       # R['Conductivity'] = ec.read()['ec']
       # R['pH'] = ph.read()
       # R['O2 mg/L'] = do.read()
       # R['ORP'] = orp.read()
        r = bme.read()
        R['kPa'] = r['p']
        R['Deg.C'] = r['t']
        R['%RH'] = r['rh']

        lcd.write_lines([str(R['ts'])[0:19],
                         '{:.1f} deg C'.format(r['t']),
                         '{:.1f} % RH'.format(r['rh']),
                         '{:.2f} kPa'.format(r['p'])])
       # r = rgb.read()
       # R['Red'] = r['r']
       # R['Green'] = r['g']
       # R['Blue'] = r['b']

        #print('\x1b[2J\x1b[;H')
        #pretty_print(R)

        #lcd.write_lines([str(R['ts'])[0:19], str(R['kPa']), str(R['Deg.C']), str(R['%RH'])])

        time.sleep(1)
    except KeyboardInterrupt:
        break
    except:
        traceback.print_exc()

