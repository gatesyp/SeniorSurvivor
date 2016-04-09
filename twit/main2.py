import tweepy
import dbconnect
import time
from random import randint
from random import random

consumer_key = "2E39YN2PgjgTscKjpU8JCPWkw"
consumer_secret = "aiIo63Bs8LsglpYWfOWKwDyh4UNWABNd6Cg7b0CeGs7ZkEHDcT"
access_token = "718226842579243012-y6TZ8wU5ZYgK3zfrXzvARKyPTaPWTaY"
access_token_secret = "a6OnUSfMDAAd2bEsIzxarJCh7rb7DsjZioxKcmsK9SPie"


# using OAuth to validate connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for item in dbconnect.get_items():
    print item[1]
print ""


def find_order(status):
    print ("finding order")
    for alias in dbconnect.get_items():
        if alias[1].lower() in status:
            print alias[1].lower()
            if int(alias[0]) == 23 or int(alias[0]) == 24:
                if "half" in status or "1/2" in status:
                    return "24", "none"
                else:
                    return "23", "none"
            elif int(alias[0]) == 25:
                extras = []
                split_status = status.split()
              	found = False
                for word in split_status:
                    if word == "doritos" or word == "dorito" or word == "dorito's":
                        extras.append("doritos")
			found = True
                i = 0
                length = len(split_status)
                while i + 1 < len(split_status):
                    print ("in this loop haha")
                    word = split_status[i]
                    if word == "no" or word == "without" or word == "but" or word == "with":
                        extras.extend(find_extras(status, word, i))
                    i = i + 1
                    if i > length: break
                print "extra string"
                extra_string = ""
                for extra in extras:
                    extra_string += extra + ", "
                return "25", extra_string

            else:
                return str(int(alias[0])), "none"

    print('FOUND NO ORDER')
    return '', ''


def find_extras(status, word, word_loc):
    split_status = status.split()
    length = len(split_status)
    extras = []
    i = word_loc
    if word == "no" or word == "without":
        while (i + 1) < len(split_status):
            keyword = split_status[i]
            keyword = keyword.replace(',', '')
            print("KEYWORD: " + keyword)
            if keyword == "or" or keyword == "any" or keyword == "and" or keyword == "cream":
                print "meme"
            # i = i+1
            #    if i > length: break

            elif keyword == "salsa":
                extras.append("no salsa")
            elif keyword == "sour" or keyword == "sourcream":
                extras.append("no sour cream")
            elif keyword == "lettuce":
                extras.append("no lettuce")
            elif keyword == "cheese":
                extras.append("no cheese")
            print "made it here"
            i = i + 1
            if i > length: break
            print i
        print "returning 1"
        return extras
    while (i + 1) < len(split_status):
        keyword = split_status[i]
        keyword = keyword.replace(',', '')
        print("Keyword: " + keyword)
        if keyword == "or" or keyword == "any" or keyword == "and" or keyword == "cream" or keyword == "with":
            print "memes"
        # i = i+1
        #    if i > length: break
        elif keyword == "salsa":
            extras.append("salsa")
        elif keyword == "sour" or keyword == "sourcream":
            extras.append("sour cream")
        elif keyword == "lettuce":
            extras.append("lettuce")
        elif keyword == "cheese":
            extras.append("cheese")
        i = i + 1
        if i > length: break
        print i
    print "returning 2"
    return extras


def find_quantity(status):
    for quantity in dbconnect.get_quantities():
        q = quantity[1].lower()
        for word in status:
            w = word.lower()
            if w == q:
                print('FOUND QUANTITY')
                return w

    print('FOUND NO QUANTITY')
    return '1'


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
        print("############################################################################")
        print ("new status!")

        order = {'id': '', 'quantity': '', 'handle': '', 'room': '', 'extras': ''}

        status_txt = (str(status.text))
        split_status = status_txt.split()
        print status_txt

        order['handle'] = str(status.author.screen_name)

        order['id'], order['extras'] = find_order(status_txt.lower())

        order['quantity'] = find_quantity(split_status)

        order['room'] = find_room(split_status)

        price = dbconnect.get_price(order['id'], order['quantity'])
        order_num = randint(0, 120)

        print "extras: " + order['extras']

        if order['handle'] == 'senorsurvivor':
            print("not going to reply to main account!")
            return

        if order['room'] == '':
            print('no room')
            error_id = random()*1000000000
            try:
                api.update_status('@' + order['handle'] + ' You did not specify a room number. Please try ordering again. Error: ' + str(order_num))
            except tweepy.error.TweepError:
                print("reply didnt work")
            print("############################################################################")
            return

        if order['id'] == '':
            print('no id')
            return

        if order['handle'] != '' and order['id'] != '' and order['quantity'] != '' and order['room'] != '':
            print(str(order) + " :: FINAL")
            dbconnect.insert_order(order)
            print('All Is Good! New Order Logged!!')
            print("############################################################################")

            try:
                api.update_status('@' + order['handle'] + ' Thank you for your order! Your order number is ' + str(order_num) + '. It will cost $' + price)
                return
            except tweepy.error.TweepError:
                try:
                    order_num = randint(0, 120)
                    api.update_status('@' + order['handle'] + ' Thank you for your order! Your order number is ' + str(order_num) + ' It will cost $' + price)
                    return
                except tweepy.error.TweepError:
                    try:
                        order_num = randint(0, 120)
                        api.update_status('@' + order['handle'] + ' Thank you for your order! Your order number is ' + str(order_num) + ' It will cost $' + price)
                        return
                    except tweepy.error.TweepError:
                        return


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
myStream.filter(track=['@senorsurvivor'])
