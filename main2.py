#temp file
import tweepy
import json
import pprint
import time
from random import randint
from random import random


print ("Start")
consumer_key = "2E39YN2PgjgTscKjpU8JCPWkw"
consumer_secret = "aiIo63Bs8LsglpYWfOWKwDyh4UNWABNd6Cg7b0CeGs7ZkEHDcT"
access_token = "718226842579243012-y6TZ8wU5ZYgK3zfrXzvARKyPTaPWTaY"
access_token_secret = "a6OnUSfMDAAd2bEsIzxarJCh7rb7DsjZioxKcmsK9SPie"


# using OAuth to validate connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#for item in dbconnect.get_items():
#    print item[1]
#print ""



# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print("############################################################################")
		print ("new status!")
		order = {'id': '', 'quantity': '', 'handle': '', 'room': '', 'extras': '', 'lat': '' , 'long': ''}
		status_txt = (str(status.text))
		print (status_txt)
		pp = pprint.PrettyPrinter(indent = 4)
		pp.pprint(status)





myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
myStream.filter(track=['@SweetTweetsUA'])
