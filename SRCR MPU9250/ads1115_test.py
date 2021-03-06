# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:16:39 2020

@author: vital
"""

import time
import Adafruit_ADS1x15
#import numpy as np

#ADS1115 = 0x01              # Specify that the device being used is the ADS1115, for the ADS1015 used 0x00
adc = Adafruit_ADS1x15.ADS1115()   # Create instance of the class ADS1x15 called adc
GAIN = 2/3                  # Set full-scale range of programable gain amplifier (page 13 of data sheet), change depending on the input voltage range
#sps = 128           # how long it takes for the ADC to carry out a single conversion (1/sps)

frequency = 5 # how often the Pi reads the ADS1115, Hz
deltat = 1.0 / frequency        # Calculate sampling period

startTime=time.time()                   # Time of first sample
t1=startTime                            # T1 is last sample time
t2=t1                                   # T2 is current time

while True:                         # Loop in which data is sampled
    while (t2-t1 < deltat):         # Check if t2-t1 is less then sample period, if it is then update t2
        t2 = time.time()                # and check again       
    t1 += deltat                        # Update last sample time by the sampling period
    print adc.read_adc(0, gain=GAIN), " mV       ", ("%.2f" % (t2 - startTime) , " s")    # Print sampled value and time to the terminal
# /home/pi/.local/lib/python2.7/site-packages/Adafruit_PureIO/smbus.py REQUIRED FIXING
# AT LINE 216 - ADDED str()