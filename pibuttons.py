#!/usr/bin/python
# -*- coding: utf-8 -*-

#Cole Deaton

#Playing with the pi buttons

#the base code was written by Alex Eames and i found it at http://RasPi.tv  

#I edited the code as needed

import RPi.GPIO as GPIO

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

import time

GPIO.setmode(GPIO.BCM)



# GPIO pins 23 & 24 are set up as the inputs. One as a pulled up, the other as a pull  down.  

# GPIO pin 23 will go to GND when button pressed 
# GPIO pin 24 will go to 3V3 (3.3V) when button is ppressed 

# this enables us to show both the rising and the falling edge detection  

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)



# we'll now define and set up the threaded callback function  

# when the event is detected this will run in a seperate thread.   

def my_callback(channel):

    lcd.clear()

    lcd.message("Falling edge \on port 24")

    print ("Rising edge detected on port 24")

    print ("we are still waiting for a falling edge")

    print ("Make sure you have a button connected so that when pressed")

    print ("it will connect GPIO port 23 to GND")

    print ("You will also need a second button connected so that when pressed")

    print ("It will connect GPIO port 24 to 3V3")

raw_input(lcd.message("Press Enter"))



# The GPIO.add_event_detect() the following will set things up so that when
# port 24 has falling edge my_callback takes place.



GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback, bouncetime = 200)

          

try:

    lcd.clear()

    lcd.message("Waiting...")

    print "Waiting for falling edge on port 23"

    GPIO.wait_for_edge(23, GPIO.FALLING)

    lcd.clear()

    lcd.message("falling edge detected")

    print "Falling edge detected."

    

except KeyboardInterrupt:

    GPIO.cleanup() # clean up GPIO on forced exit

GPIO.cleanup() # clean up GPIO on normal exit
