#!/usr/bin/python
# -*- coding: utf-8

# Jose H
# got help from, http://lpaste.net/107926
# Program is used like an alarm clock. User sets the Hour(Military time) and minutes. Program reads out your name,
#       what day it is, weather conditions, and temperature in degrees Fahreinheit. Using Raspberry pi 2 model B.
#       Program also check to see if the Pi is getting too hot, if it is, a relay switch that controls a fan turns
#       on to cool the pi.
import subprocess
import time
import textwrap
import RPi.GPIO as GPIO
from Better_Speak import now
from Better_Speak import period
#from get_url_btc2 import response_dictionary
from Get_Weather_url import current
#from get_url_weather5 import todays_low
#from get_url_weather5 import todays_high
from Get_Weather_url import conditions

# using try: as a safety precaution
try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False) # set warning to false
        GPIO.setup(23, GPIO.OUT)# set GPIO 23 on raspberry pi to output
        GPIO.output(23, GPIO.HIGH) # GPIO 23 is off at the moment



        # your name goes here:
        name = 'Jose'


        # reads out time of day + my name
        gmt = 'Good'+ period+ name+ ','

        # reads date and time
        day = ' its '+ now

		 # reads current weather
        wtr = ' .. Weather conditions for today are ' + str(conditions) + ' with a current temperature of ' + str(current) + ' Degrees ' + 'Fahrenheit '

        # reads today’s forecast weather
        #frc = ' with a low of ' + str(todays_low) + ' and a high of ' + str(todays_high)
        while 1:
                hour =int( time.strftime("%H")) # gets current time(Hour)
                minutes = int(time.strftime("%M")) #gets current time(minutes)


                hour2 = 17 #hour 8 == 8am, hour 13 == 1pm, hour 21 == 9pm, 12am = 00
                minutes2 = 17  # set hour and minutes here for when you want the alarm to be

                timing = hour2 - hour
                timing = abs(timing) # get absolute value
                timing2 = minutes - minutes2
                timing2 = abs(timing2) # get absolute value

                temp = int(open('/sys/class/thermal/thermal_zone0/temp').read())/1000 # get Raspberry pi 2 core temperature
                temp2 = (temp * (9/5)) + 32 # converted to degree Fahreinheit

				if(timing != timing2):
                        timing = hour2 - hour
                        timing = abs(timing)-1

                if(temp2 >=79): # if pi core temperature is >= 79  degrees Fahreinheit, turns on the fan to cool the pi
                        GPIO.output(23, GPIO.LOW)
                if(temp2 < 79): # if pi's core temperature is less than 79 keep fan off.
                        GPIO.output(23, GPIO.HIGH)


                if(timing == 0 and timing2 < 8): # if less than 1 hour and less than 8 minutes for alarm clock execute if statement
                        while 1:
                                GPIO.output(23, GPIO.HIGH) # turn off fan
                                hour =int( time.strftime("%H")) # get current time(Hour)
                                minutes = int(time.strftime("%M")) #get currrent time(Minutes)
								
								if(hour == hour2 and minutes == minutes2): # if its time for alarm, execute.
                                        wad = (gmt + day + wtr) # wad all the data of the string to be read
                                        print wad
                                        print subprocess.check_output("echo " + wad + " | festival --tts ", shell=True) # run Festival(text to speech). Install before
                                        time.sleep(3) # sleep for 3 seconds
                                        GPIO.cleanup() #clean up GPIO
                                        break # exit out of this while loop
                                time.sleep(3) # sleep for 3 seconds to give a little time to execute while loop again
                        break #exit ouf of first while loop. ends the program


                elif(timing >= 1): # if more than one hour is left for alarm clock, sleep for about 58 minutes
                        time.sleep(3537)

                time.sleep(3) # sleeps for 3 seconds from the first while loop to give time to execute again

# if a keyboard button is presses this exception is executed
except KeyboardInterrupt:
        print 'Quitting'
        GPIO.output(23, GPIO.HIGH) # turns off fan
        GPIO.cleanup()

# if unknown error is cause. this exception is executed
except:
        print 'Quitting of unknown cause'
        GPIO.output(23, GPIO.HIGH)
        GPIO.cleanup()
