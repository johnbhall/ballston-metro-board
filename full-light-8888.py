import time
from Adafruit_7Segment import SevenSegment

segment0 = SevenSegment(address=0x70)
segment1 = SevenSegment(address=0x71)
segment2 = SevenSegment(address=0x72)
segment3 = SevenSegment(address=0x73)

for i in [0,1,3,4]:
    segment0.writeDigit(i, 8)

for i in [0,1,3,4]:
    segment1.writeDigit(i, 8)

for i in [0,1,3,4]:
    segment2.writeDigit(i, 8)

for i in [0,1,3,4]:
    segment3.writeDigit(i, 8)

