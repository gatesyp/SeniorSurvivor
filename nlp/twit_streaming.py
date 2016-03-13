import tweepy
import random
import intent
from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine
import  pprint
import update_status

engine = IntentDeterminationEngine()

engine = intent.build_engine(engine)


consumer_key = "uEiVjyO98GwtHeV84vnxFb8YI"
consumer_secret = "2HUukAwVgr3X4nworgMnvNDQT2vy4QNObmztx9Q3thvHPn2hJI"
access_token = "378220962-KJNvdtMLLKz4gEDEc9eAS7KdJUPFWsRQDDVYJH98"
access_token_secret = "a78VF2709JZghNQWd11rskIfuTshKVanDbGz9W8f6egyI"

# using OAuth to validate connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# override tweepy.StreamListener to add logic to on_status
class StreamListener(tweepy.StreamListener):
    global engine
    global api

    def on_status(self, status):
        global api
        global engine
        vars(self)
        order = intent.get_intent(engine, status.text)
        processed_order = intent.normalize_order(order)
        
        if status.user.screen_name:
            processed_order['name'] = status.user.screen_name.encode('ascii')
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(order)
	print("AND NOW THE NORMALIZED ORDER")
	pp.pprint(processed_order)
        intent.insert_order(processed_order)

        price = intent.get_price(processed_order['menu_item'], processed_order['quantity']) 
        print(status.text)
        randomness = random.choice('qwertyuiopasdflkjhgm,nbzxcv,./;][p1230987365!$%^&*>ZX<MNCBVLKASJDHFGPOQIWEURYT')
        response = "@" + processed_order['name'] + " price is $" + str(price) + "! Thanks for supporting us! " + randomness
        print(response)
        try:
            update_status.update(response)
        except:
            print("no response")

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
myStreamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
i = 5
while i:
    try:
        myStream.userstream(encoding='utf8')
    except:
        print("no response")
        continue
