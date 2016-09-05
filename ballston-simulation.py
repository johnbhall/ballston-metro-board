import time
import datetime
from random import randint
from Adafruit_7Segment import SevenSegment

REFRESH_INTERVAL = 20

segment0 = SevenSegment(address=0x70)
segment1 = SevenSegment(address=0x71)
segment2 = SevenSegment(address=0x72)
segment3 = SevenSegment(address=0x73)

segment0.disp.setBrightness(1)
segment1.disp.setBrightness(1)
segment2.disp.setBrightness(1)
segment3.disp.setBrightness(1)

now = datetime.datetime.now()
customink = []
downtown = []

customink.append(now + datetime.timedelta(0, randint(0,250)))
downtown.append(now + datetime.timedelta(0, randint(0,450)))

customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))
customink.append(customink[-1] + datetime.timedelta(0, randint(200,500)))

downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))
downtown.append(downtown[-1] + datetime.timedelta(0, randint(200,500)))

print "Press CTRL+Z to exit"


# 8-character string that will be used to update a row of LEDs
def output_string(arr):
    str_predictions = []
    for p in arr:
        str_predictions.append( str(p).rjust(2) )
    return " ".join(str_predictions).ljust(8)

# ignore the colon (third character of the segment)
def update_segment(segment, str):
    for index, char in enumerate(str):
        i = index
        if index > 1:
            i = index + 1
        if char == " ":
            segment.writeDigitRaw(i, 0)
        else:
            segment.writeDigit(i, int(char))

while(True):
    now = datetime.datetime.now()

    customink_predictions = []
    downtown_predictions = []

    j = 0
    for index,dt in enumerate(customink):
        mins_away = int(round((dt-now).total_seconds()/60))
	if (dt > now):
	    j = j+1
            if (index % 2 == 0) and (j <= 3):
                customink_predictions.append(mins_away)

    for dt in downtown:
        mins_away = int(round((dt-now).total_seconds()/60))
        if (dt > now) and (len(downtown_predictions) < 3):
            downtown_predictions.append(mins_away)
    
    predictions = {
        "customink": customink_predictions,
        "downtown": downtown_predictions
    }
    
    customink_str = output_string(predictions["customink"])
    downtown_str = output_string(predictions["downtown"])
    
    print "customink: " + customink_str.replace(" ", "_")
    print "downtown:  " + downtown_str.replace(" ", "_")
    
    update_segment(segment0, customink_str[0:4])
    update_segment(segment1, customink_str[4:8])
    update_segment(segment2, downtown_str[0:4])
    update_segment(segment3, downtown_str[4:8])
    
    time.sleep(REFRESH_INTERVAL)

