#!/usr/bin/env bash

# set here the path to the directory containing your videos
LOCATION="/home/pi/ftp/videos/"
# you can probably leave this alone
PROCESS="omxplayer"
# our loop
while true; do
    if ps ax | grep -v grep | grep ${PROCESS} > /dev/null
    then
    sleep 1;
else
    for entry in ${LOCATION}/*
    do
        clear
        # -r for stretched over the entire location
         omxplayer -r ${entry} > /dev/null
    done
fi
done