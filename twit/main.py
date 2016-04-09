import tweepy
import dbconnect
import time

consumer_key = "uEiVjyO98GwtHeV84vnxFb8YI"
consumer_secret = "2HUukAwVgr3X4nworgMnvNDQT2vy4QNObmztx9Q3thvHPn2hJI"
access_token = "378220962-KJNvdtMLLKz4gEDEc9eAS7KdJUPFWsRQDDVYJH98"
access_token_secret = "a78VF2709JZghNQWd11rskIfuTshKVanDbGz9W8f6egyI"

# using OAuth to validate connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def find_order(status):
    for alias in dbconnect.get_items():
            for word in status:
                w = word.lower()
                if w == alias[1].lower():
                    print('FOUND ORDER')
                    return str(int(alias[0]))

    print('FOUND NO ORDER')
    return ''


def find_quantity(status):
    for quantity in dbconnect.get_quantities():
            q = quantity[1].lower()
            for word in status:
                w = word.lower()
                if w == q:
                    print('FOUND QUANTITY')
                    return w

    print('FOUND NO QUANTITY')
    return ''


def find_room(status):
    for room in dbconnect.get_rooms():
            r = room[0].lower()
            for word in status:
                w = word.lower()
                if w == r:
                    print('FOUND ROOM')
                    return w

    print('FOUND NO ROOM')
    return ''


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        order = {'id': '', 'quantity': '', 'handle': '', 'room': ''}

        split_status = str(status.text).split()

        order['handle'] = str(status.author.screen_name)

        order['id'] = find_order(split_status)

        order['quantity'] = find_quantity(split_status)

        order['room'] = find_room(split_status)

        print(str(order) + " :: FINAL")

        dbconnect.insert_order(order)

        api.status_update('@'+ order['handle'] + ' Thank you for your order!')


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
myStream.filter(track=['@senorsurvivor'])
