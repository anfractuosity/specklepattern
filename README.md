# specklepattern

See https://www.anfractuosity.com/projects/fun-with-speckle-patterns/ for the associated webpage, for detecting key presses 
and hand prints from the difference between speckle patterns.

* grab.sh - Takes photos every 10s using gphoto2 (I used this with a Canon camera attached via USB to my computer)
* diff.py - After using the previous command, this command generates differences between speckle patterns and creates a video using ffmpeg
