import sys,time,traceback
from os.path import expanduser
sys.path.append(expanduser('~'))
from datetime import datetime
from node.drivers.bmp280 import BMP280
from node.drivers.lcd20x4 import *

bus = 1

bmp = BMP280(bus=bus)
bmp.set_osr_p(2)
bmp.set_osr_t(2)
bmp.set_filter(2)

lcd = LCD(bus=1,address=0x3f)
lcd.backlight(True)

while True:
    try:
        R = {}

        R['ts'] = datetime.utcnow()
        r = bmp.read()
        R['kPa'] = r['p']
        R['Deg.C'] = r['t']
   
        lcd.write_lines([str(R['ts'])[0:19],
                         '{:.1f} deg C'.format(r['t']),
                         '{:.2f} kPa'.format(r['p']),
                         '            @meshlab'])
        time.sleep(1)
        
    except KeyboardInterrupt:
        break
    except:
        traceback.print_exc()

