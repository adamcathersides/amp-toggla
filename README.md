# amp-toggla
A simple python script that controls a Rasberry Pi's GPIO in order to switch an amplifier on during media playback.

There are two versions of this script.  One for chromecast and one for Logitech Media Server (LMS).  Both versions are very similar in operation, however i have moved away from using LMS so this version may or may not work with later versions of LMS.

# Requirements

Both scripts are written in Python 2.7 use standard Raspberry Pi's GPIO python library, normally installed by default on Raspbian afaik.  

Chromecast:

pychromecast (https://github.com/balloob/pychromecast)

LMS:

pylms (https://github.com/jinglemansweep/PyLMS)

# Functionality

The script will constantly poll the media player to check if it is playing something.  In the Chromecast's case it will check to see if an app is connected.

Once playing the script should toggle the GPIO pin instantly, turning the amp on.  However if the script detects that the device has stopped playing it will enter a delay loop and will only switch to amp_off after the time has expired.  This delay is set to 1200 seconds (20 mins) and is to make sure that the amp does not toggle on and off during a quick pause or a change in media etc.

If the chromecast or LMS is set to play while in this time delay routine the script will detect this and return to the amp_on state.

# GPIO and Relays

The relay board that I use seems to break go open circuit when a 1 is set (the reverse of what i thought would happen).  Therefore it looks as though the logic is reversed in the script, but this is just the way it works in my case.



