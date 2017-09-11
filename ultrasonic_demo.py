# Plot distance measurements in real-time
#
# sudo apt-get install python-gi-cairo
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# University of Hawaii
# 2017
import time,sys,traceback,logging,serial,io
from os.path import expanduser
sys.path.append(expanduser('~'))
import matplotlib.pyplot as plt
from matplotlib import animation
from datetime import datetime


logging.basicConfig(level=logging.DEBUG)

port = '/dev/ttyS0'
interval = 200     # ms
length = 60


'''ser = serial.Serial(port,9600,timeout=0.1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser),newline='\r')
while True:
    line = sio.readline()
    if len(line):
        print(line.strip())
ser.close()
exit()'''


fig,ax1 = plt.subplots()
line1, = ax1.plot([],[],'b.-',lw=4,markersize=10)
ax1.set_xlim(0,length)
ax1.set_ylim(0,5000)
#ax1.set_ylim(0,150)
ax1.grid()
xdata = []
d2wdata = []
plt.ylabel('Distance, millimeter',color='b',fontsize=16)
for t in ax1.get_yticklabels():
    t.set_color('b')
    
plt.xlabel('Index')
plt.title('Ultrasonic Sensor Demo')


def read_ultrasonic():
    try:
        with serial.Serial(port,9600,timeout=0.2) as s:
            for i in range(6):
                if 'R' == s.read():
                    break
            line = s.read(4)
            print(line)
            return float(line)
    except:
        traceback.print_exc()
        return float('nan')

def update_line(num,line1):
    d2w = read_ultrasonic()

    d2wdata.append(d2w)
    while len(d2wdata) > length:
        d2wdata.pop(0)

    xdata = range(0,len(d2wdata))

    #ax1.figure.canvas.draw()
    line1.set_xdata(xdata)
    line1.set_ydata(d2wdata)
    return line1,
    
line_ani = animation.FuncAnimation(fig,update_line,fargs=(line1,),
                                   interval=interval,blit=True)

plt.show()


