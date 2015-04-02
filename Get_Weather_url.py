#!/usr/bin/python
# -*- coding: utf-8 -*-

# Jose H
# got help from this site, http://python-weather-api.googlecode.com/svn/trunk/pywapi.py
# This program gets the URL from where you want to get the weather data

import urllib2
import json

from urllib2 import urlopen
from urllib import quote
from urllib import urlencode
from urllib2 import URLError
import sys
import re
from math import pow
from xml.dom import minidom





"""Fetches weather report from NOAA: National Oceanic and Atmospheric
    Administration (United States)

    Parameter:
      station_id: the ID of the weather station near the desired location
      To find your station ID, perform the following steps:
      1. Open this URL: http://www.weather.gov/xml/current_obs/seek.php?state=az&Find=Find
      2. Select the necessary state state. Click 'Find'.
      3. Find the necessary station in the 'Observation Location' column.
      4. The station ID is in the URL for the weather page for that station.
      For example if the weather page is http://weather.noaa.gov/weather/current/KPEO.html -- the station ID is KPEO.

      Another way to get the station ID: use the 'Weather.location2station'
      function of this library: http://code.google.com/p/python-weather/

    Returns:
      weather_data: a dictionary of weather data that exists in XML feed.

      ( useful icons: http://www.weather.gov/xml/current_obs/weather.php )

"""

NOAA_WEATHER_URL     = 'http://www.weather.gov/xml/current_obs/%s.xml'

station_id = 'KDFW'
station_id = quote(station_id)
url = NOAA_WEATHER_URL % (station_id)
#check to see if the webpage can open
try:
        handler =  urllib2.urlopen(url)
#if webpage can't open execute this
except URLError:
        print{'error': 'Could not connect to NOAA'}
		
content_type = handler.info().dict['content-type']

#check to see if we are using the correct character set
try:
        charset = re.search('charset\=(.*)', content_type).group(1)
except AttributeError:
        charset = 'utf-8'
if charset.lower() != 'utf-8':
        xml_response = handler.read().decode(charset).encode('utf-8')
else:
        xml_response = handler.read()

dom = minidom.parseString(xml_response)
handler.close()

#tags for the API of the weather statiion to call from
data_structure = ('suggested_pickup',
                'suggested_pickup_period',
                'location',
                'station_id',
                'latitude',
				'longitude',
                'observation_time',
                'observation_time_rfc822',
                'weather',
                'temperature_string',
                'temp_f',
                'temp_c',
                'relative_humidity',
                'wind_string',
                'wind_dir',
                'wind_degrees',
                'wind_mph',
                'wind_gust_mph',
                'pressure_string',
                'pressure_mb',
                'pressure_in',
                'dewpoint_string',
                'dewpoint_f',
                'dewpoint_c',
                'heat_index_string',
				'heat_index_f',
                'heat_index_c',
                'windchill_string',
                'windchill_f',
                'windchill_c',
                'icon_url_base',
                'icon_url_name',
                'two_day_history_url',
                'ob_url'
                )
weather_data = {}
current_observation = dom.getElementsByTagName('current_observation')[0]

for i in data_structure:
        current = current_observation.getElementsByTagName('temp_f')[0].firstChild.data # gets temperature
        break

for i in data_structure:
        conditions = current_observation.getElementsByTagName('weather')[0].firstChild.data # gets weather conditions
        break
		
dom.unlink()
#main programs stops here----------


		
		