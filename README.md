# Ballston Metro Board ("Raspberry PID")

This script is meant to be run on a Raspberry Pi. It will hit the API of WMATA (Washington, DC's Metro) to access real-time train arrival data for Ballston station. Trains will be sorted into two groups: those going toward my office (Westbound Orange) and those going downtown (Eastbound Orange or Silver). The train times will be displayed on 7-segment LEDs connected to the Pi.

## Autostart

Add this to the end of `/etc/rc.local` (but before the `exit 0` command) to have the Raspberry Pi automatically run the script when it boots up.

```
python /home/pi/ballston-metro-board/ballston.py &
```

## Resources

[Blog Post](http://johnbhall.com/raspberry-pid/) and [presentation slides](https://speakerdeck.com/johnbhall/raspberry-pid) from June 2015.
