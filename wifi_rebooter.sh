#!/bin/bash

# The IP for the server you wish to ping (8.8.8.8 is a public Google DNS server)
SERVER=8.8.8.8

# Only send two pings, sending output to /dev/null
ping -c2 ${SERVER} > /dev/null

# If the return code from ping ($?) is not 0 (meaning there was an error)
if [ $? != 0 ]
then
    echo "WiFi is not connected. Restarting the wireless interface."
    # Restart the wireless interface
    sudo ifdown --force wlan0
    sudo ifup wlan0
else
    echo "WiFi is connected."
fi

