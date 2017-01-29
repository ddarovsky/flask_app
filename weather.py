# -*- coding: utf-8 -*-

#import forecastio library
import forecastio
#import address to long/lat 'translater' to use in forecastio api so we can input the address not the lat/long
from geopy.geocoders import Nominatim

import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
	
#define a function to pull the weather based on the address inserted
def get_weather(address):
	api_key = os.environ['FORECASTIO_API_KEY']
	#set the part of the library from the geopy library we want, since we don't want the whole thing
	geolocator = Nominatim()
	#set location as the address inputted into the geopy library
	location = geolocator.geocode(address)
	#set latitude as 'location.latitude' which is how it's defined in the geopy library
	latitude = location.latitude
	#set longitude as 'location.longitude' which is how it's defined in the geopy library
	longitude = location.longitude
	#set the forecast as a function of the api key, lat/long, using current weather results
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	#set summary as 'forecast.summary' which is how it's defined as an attribute in the dark skies library
	summary = forecast.summary
	#set temperature as 'forecast.temperature' which is how it's defined as an attribute in the dark skies library
	temperature = forecast.temperature
	#rreturn the result for the forecast + temp + address
	return "{} and {}° at {}".format(summary, temperature, address)
