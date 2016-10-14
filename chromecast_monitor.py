#!/usr/bin/env python

import time
import pychromecast
import RPi.GPIO as GPIO

#GPIO setup

gpio_channels = [23, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_channels, GPIO.OUT)

#Connect to chromecast to its monitor state

kitchen_cast = pychromecast.get_chromecast(friendly_name="Kitchen")

#print kitchen_cast.status


def time_delay(timeout):

    """
    Creates a time delay.
    Used for switching the amp off after a period of time if the chromecast is
    not playing anything.

    If chromecast playback is started during this time the script goes back to
    the amp_on state.

    """

    for n in range(timeout):

        time.sleep(1)
        #print "Turning amp off in {} seconds".format(timeout - n)

        if kitchen_cast.app_display_name is not None:

            amp_on()


def amp_off():

    """
    Switch amp off.

    Also checks if chromecast is playing and turns back on if it is.

    """

    time.sleep(0.8)
    #print "func.Switch amp off"
    GPIO.output(gpio_channels, 1)
    if kitchen_cast.app_display_name is not None:

        amp_on()


def amp_on():

    """
    Switch amp on.

    IF chromecast is not playing, run time delay and ultimately turn off amp.

    """

    time.sleep(0.8)
    #print "func.Switch amp on"
    GPIO.output(gpio_channels, 0)
    if kitchen_cast.app_display_name is None:
        time_delay(1200)

#Main Script#

while True:

    if kitchen_cast.app_display_name is not None:
        amp_on()
    elif kitchen_cast.app_display_name is None:
        amp_off()

