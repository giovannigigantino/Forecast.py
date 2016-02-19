#!/usr/bin/env python

# -*- coding: utf-8 -*-
#-- DOCS
'''
Giovanni Gigantino  2016-02-18  [Python 2.7]

Script to get weather forecast inside terminal.
'''

#-- LIB
import pyowm
from sys import argv

#-- CLASS
class WeatherForecast(object):
	''' Class that gets the weather from 'openweathermap.org'.
	'''

	owm = pyowm.OWM('1d1b2b66fee964ebb35ccd19e4fb3ed9')  # API key
	
	def __init__(self, city, state):
		''' Class constructor. '''

		self._city = city
		self._state = state
		location = "%s, %s" % (self._city, self._state)
		forecast = WeatherForecast.owm.daily_forecast(location)
		forecast = forecast.get_forecast()
		self._weather = forecast.get_weathers()

	def city(self):
		''' City get method. '''

		return self._city

	def setCity(self, city):
		''' City set method. '''

		self._city = city

	city = property(fget=city, fset=setCity)

	def state(self):
		''' State get method. '''
		return self._state

	def setState(self, state):
		''' Stete set method. '''
		self._state = state

	state = property(fget=state, fset=setState)

	def weatherToday(self):
		''' Returns a dict with today's weather. '''
		ref = self._weather[0]
		out = {
			"status": ref.get_detailed_status().capitalize(),
			"temperature": (str(ref.get_temperature(unit='celsius')['day']) + "C"),
			"reference": ref.get_reference_time(timeformat='iso')[:-6]
		}

		return out

	def weatherTomorrow(self):
		''' Returns a dict with tomorrow's forecast. '''
		ref = self._weather[1]
		out = {
			"status": ref.get_detailed_status().capitalize(),
			"temperature": (str(ref.get_temperature(unit='celsius')['day']) + "C"),
			"reference": ref.get_reference_time(timeformat='iso')[:-6]
		}

		return out

#-- MAIN
if __name__ == '__main__':
		
	if len(argv) == 3:	
	
		wf = WeatherForecast("Verona", "it")

		today = wf.weatherToday()
		tomorrow = wf.weatherTomorrow()

		for key, value in today.iteritems():
			print(key.capitalize() + ": " + value)

		print("\n")

		for key, value in tomorrow.iteritems():
			print(key.capitalize() + ": " + value)
	else:
		print("Usage: Forecast.py <City> <state>")
