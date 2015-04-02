#!/usr/bin/python

# Jose H
#got help from, http://lpaste.net/107929
import time


#will the the current date(number). Then it will combine associate it with the word
if int(time.strftime("%d")) == 1:
  suffixed = 'first'
elif int(time.strftime("%d")) == 2:
  suffixed = 'second'
elif int(time.strftime("%d")) == 3:
  suffixed = 'third'
elif int(time.strftime("%d")) == 4:
  suffixed = 'fourth'
elif int(time.strftime("%d")) == 5:
  suffixed = 'fifth'
elif int(time.strftime("%d")) == 6:
  suffixed = 'sixth'
elif int(time.strftime("%d")) == 7:
  suffixed = 'seventh'
elif int(time.strftime("%d")) == 8:
  suffixed = 'eighth'
elif int(time.strftime("%d")) == 9:
  suffixed = 'ninth'
elif int(time.strftime("%d")) == 10:
  suffixed = 'tenth'
elif int(time.strftime("%d")) == 11:
  suffixed = 'eleventh'
elif int(time.strftime("%d")) == 12:
  suffixed = 'twelfth'
elif int(time.strftime("%d")) == 13:
  suffixed = 'thirteenth'
elif int(time.strftime("%d")) == 14:
  suffixed = 'fouteenth'
elif int(time.strftime("%d")) == 15:
  suffixed = 'fifteenth'
elif int(time.strftime("%d")) == 16:
  suffixed = 'sixteenth'
elif int(time.strftime("%d")) == 17:
  suffixed = 'seventeeth'
elif int(time.strftime("%d")) == 18:
  suffixed = 'eighteenth'
elif int(time.strftime("%d")) == 19:
  suffixed = 'nineteenth'
elif int(time.strftime("%d")) == 20:
  suffixed = 'twentieth'
elif int(time.strftime("%d")) == 21:
  suffixed = 'twentyfirst'
elif int(time.strftime("%d")) == 22:
  suffixed = 'twentysecond'
elif int(time.strftime("%d")) == 23:
  suffixed = 'twentythird'
elif int(time.strftime("%d")) == 24:
  suffixed = 'twentyfourth'
elif int(time.strftime("%d")) == 25:
  suffixed = 'twentyfifth'
elif int(time.strftime("%d")) == 26:
  suffixed = 'twentysixth'
elif int(time.strftime("%d")) == 27:
  suffixed = 'twentyseventh'
elif int(time.strftime("%d")) == 28:
  suffixed = 'twentyeigth'
elif int(time.strftime("%d")) == 29:
  suffixed = 'twentyninth'
elif int(time.strftime("%d")) == 30:
  suffixed = 'thirtieth'
elif int(time.strftime("%d")) == 31:
  suffixed = 'thirtyfirst'



now = time.strftime("%A %B ") + suffixed + time.strftime(" %I %M %p")


#check to see what time of the day it is
if int(time.strftime("%H")) < 12:
  period = ' morning '
elif int(time.strftime("%H")) >= 12:
  period = ' afternoon '
elif int(time.strftime("%H")) >= 17:
  period = ' evening '

