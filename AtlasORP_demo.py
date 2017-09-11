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
from node.drivers.ezo_orp import EZO_ORP
from node.drivers.lcd20x4 import *

bus = 1

lcd = LCD(bus=1,address=0x3f)
lcd.backlight(True)
orp = EZO_ORP(bus=bus,lowpower=False)

while True:
    try:
        R = {}

        R['ts'] = datetime.utcnow()
        R['ORP'] = orp.read()
 
        lcd.write_lines([str(R['ts'])[0:19],
                         '{:.2f}'.format(R['ORP']),
                         '',
                         '            @meshlab'])

        time.sleep(1)
    except KeyboardInterrupt:
        break
    except:
        traceback.print_exc()

