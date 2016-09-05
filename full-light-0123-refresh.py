import time
from Adafruit_7Segment import SevenSegment

REFRESH_INTERVAL = 1

print "Press CTRL+Z to exit"

while(True):

    segment0 = SevenSegment(address=0x70)
    segment1 = SevenSegment(address=0x71)
    segment2 = SevenSegment(address=0x72)
    segment3 = SevenSegment(address=0x73)

    for i in [0,1,3,4]:
        segment0.writeDigit(i, 0)

    for i in [0,1,3,4]:
        segment1.writeDigit(i, 1)

    for i in [0,1,3,4]:
        segment2.writeDigit(i, 2)

    for i in [0,1,3,4]:
        segment3.writeDigit(i, 3)
    
    time.sleep(REFRESH_INTERVAL)

