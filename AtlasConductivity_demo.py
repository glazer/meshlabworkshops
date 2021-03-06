#dissolved oxygen measurements using Atlas Scientific chip
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# University of Hawaii
# 2017

import sys,time,traceback
from os.path import expanduser
sys.path.append(expanduser('~'))
from datetime import datetime
from node.drivers.ezo_ec import EZO_EC
from node.drivers.lcd20x4 import *

bus = 1

lcd = LCD(bus=1,address=0x3f)
lcd.backlight(True)
ec = EZO_EC(bus=bus,lowpower=False)

while True:
    try:
        R = {}

        R['ts'] = datetime.utcnow()
        R['Conductivity'] = ec.read()['ec']
        R['sal'] = ec.read()['sal']
 
        lcd.write_lines([str(R['ts'])[0:19],
                         '{:.1f} uS'.format(R['Conductivity']),
                         '{:.1f} ppt'.format(R['sal']),
                         '            @meshlab'])

        time.sleep(1)
    except KeyboardInterrupt:
        break
    except:
        traceback.print_exc()

