import tweepy
import intent
import pprint

consumer_key = "uEiVjyO98GwtHeV84vnxFb8YI"
consumer_secret = "2HUukAwVgr3X4nworgMnvNDQT2vy4QNObmztx9Q3thvHPn2hJI"
access_token = "378220962-KJNvdtMLLKz4gEDEc9eAS7KdJUPFWsRQDDVYJH98"
access_token_secret = "a78VF2709JZghNQWd11rskIfuTshKVanDbGz9W8f6egyI"

# using OAuth to validate connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
def update(response):
	api.update_status(status=response)
