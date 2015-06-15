import time
from Adafruit_7Segment import SevenSegment
import urllib2
import json

REFRESH_INTERVAL = 20

segment0 = SevenSegment(address=0x70)
segment1 = SevenSegment(address=0x71)
segment2 = SevenSegment(address=0x72)
segment3 = SevenSegment(address=0x73)

# K04 is Ballston station
STATION_ID = "K04"
API_KEY = "< YOUR API KEY HERE >"
prediction_url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction"

print "Press CTRL+Z to exit"

# fetch train predictions from WMATA API
def train_predictions():
    response  = urllib2.urlopen(prediction_url + "/" + STATION_ID + "?api_key=" + API_KEY)
    data = json.load(response)
    trains = data["Trains"]
    train_predictions = {
        "customink": [],
        "downtown": []
    }
    for t in trains:
        if t["Group"] == "2" and t["Line"] == "OR":
            train_predictions["customink"].append( minutes_for_train(t["Min"]) )
        elif t["Group"] == "1":
            train_predictions["downtown"].append( minutes_for_train(t["Min"]) )
    return train_predictions

# convert a string to integer. Return 0 for "ARR" and "BRD" and "---"
def minutes_for_train(str):
    try:
        mins = int(str)
    except:
        mins = 0
    return mins

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
    predictions = train_predictions()
    
    customink_str = output_string(predictions["customink"])
    downtown_str = output_string(predictions["downtown"])
    
    print "customink: " + customink_str.replace(" ", "_")
    print "downtown:  " + downtown_str.replace(" ", "_")
    
    update_segment(segment0, customink_str[0:4])
    update_segment(segment1, customink_str[4:8])
    update_segment(segment2, downtown_str[0:4])
    update_segment(segment3, downtown_str[4:8])
    
    time.sleep(REFRESH_INTERVAL)
