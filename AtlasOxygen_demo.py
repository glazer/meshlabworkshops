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
from node.drivers.ezo_do import EZO_DO
from node.drivers.lcd20x4 import *

bus = 1

do = EZO_DO(bus=bus,lowpower=False)
lcd = LCD(bus=1,address=0x3f)
lcd.backlight(True)

while True:
    try:
        R = {}

        R['ts'] = datetime.utcnow()
        R['O2 mg/L'] = do.read()
        R['O2 uM'] = do.read_uM()
 
        lcd.write_lines([str(R['ts'])[0:19],
                         '{:.1f} mg/L'.format(R['O2 mg/L']),
                         '{:.1f} uM'.format(R['O2 uM']),
                         '            @meshlab'])

        time.sleep(1)
    except KeyboardInterrupt:
        break
    except:
        traceback.print_exc()

