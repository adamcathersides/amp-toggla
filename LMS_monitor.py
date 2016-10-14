#!/usr/bin/env python

from pylms.server import Server
from pylms.player import Player
import time
import RPi.GPIO as GPIO

#GPIO setup

gpio_channels = [23, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_channels, GPIO.OUT)

#Connect to chromecast to its monitor state

server = Server(hostname="LMS-server", port=9090)
server.connect()

print server.get_version()

player = server.get_player("kitchen-pi")
print player.get_ip_address()


print player.get_name()
print player.get_mode()

mode = player.get_mode


def time_delay(timeout):

    """
    Creates a time delay.
    Used for switching the amp off after a period of time if the LMS is
    not playing anything.

    If LMS playback is started during this time the amp is switched
    back on the amp_on state.

    """


    for n in range(timeout):

        time.sleep(1)
        #print "Turning amp off in {} seconds".format(timeout - n)

        if player.get_mode() == "play":

            amp_on()


def amp_off():

    """
    Switch amp off.

    Also checks if LMS is playing and turns back on if it is.

    """

    time.sleep(0.8)
    #print "func.Switch amp off"
    GPIO.output(gpio_channels, 1)
    if player.get_mode() == "play":
        amp_on()


def amp_on():

    """
    Switch amp on.

    IF LMS is not playing, run time delay and ultimately turn off amp.

    """

    time.sleep(0.8)
    #print "func.Switch amp on"
    GPIO.output(gpio_channels, 0)
    if player.get_mode() == "pause":
        time_delay(1200)
    elif player.get_mode() == "stop":
        time_delay(1200)

#Main Script

while True:

    if player.get_mode() == "play":
        amp_on()
    elif player.get_mode() == "pause":
        amp_off()
    elif player.get_mode() == "stop":
        amp_off()
