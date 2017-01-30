#import the yelp api and the client authentication 
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from os import environ

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
	#define authentication based on the 4 API Keys given
	auth = Oauth1Authenticator(
    	consumer_key= environ['CONSUMER_KEY'],
    	consumer_secret= environ['CONSUMER_SECRET'],
    	token= environ['TOKEN'],
    	token_secret= environ['TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
    	'term': term,
    	'lang': 'en',
    	'limit': 3
	}
	
	response = client.search(location, **params)

	# creating a lost of businesses
	businesses = []

	#going through list of businesses # 'for' loops work differently than functions in that you can access inside of them variables that you've created outside of them 
	for business in response.businesses:
		# print(business.name, business.rating, business.phone)
		# appending the name of each business to this list
		# in 'Returning a Dictionary of Businesses' video, to store a few different things for each business, instead of appending the business name, which is a string, you'd append a dictionary
		businesses.append(business.name)
			#"rating": business.rating,
			#"phone": business.phone
		#)
	
	#return the list at the end and it should be full that at point
	return businesses

#businesses = get_businesses(address, term)

#print(businesses)

