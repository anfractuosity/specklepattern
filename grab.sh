#!/bin/bash

BATCH="$(date +%s)"
mkdir -p "imgs/$BATCH"

while [[ 1 ]];
do
	gphoto2 --filename="imgs/$BATCH/$(date +%s).%C" --capture-image-and-download
	sleep 10
done

