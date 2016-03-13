import json
import sys
import MySQLdb
import db_connect


from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

cur = db_connect.connect()
engine = IntentDeterminationEngine()

def get_aliases(category):
    sql = "SELECT * from aliases WHERE category = " + category
    cur.execute(sql)

    alias_list = list()

    for row in cur.fetchall():
        alias_list.append(row[2])
    return alias_list

def insert_order(item_id, quantity, name, location):
    global cur
    sql = "insert into orders(item_id, quantity, name, room, completed) VALUES (" + item_id + ", " + quantity + ", " + name + ", " + location + " 0)"
    cur.execute(sql)
    db_connect.commit_db()

# distill the order to DB core components
# -- change and teacher name to a room number
# -- keep room number if it is available
# -- change the current keyword to an alias
def normalize_order(order):
    global cur
    normalized = {}

    # change menu_item from alias to core name
    sql = "SELECT item_id FROM aliases WHERE alias = \"" + order["menu_items"] + "\""
    cur.execute(sql)

    for row in cur.fetchall():
        sql = "SELECT * FROM items where id = \"" + str(row[0]) + "\""
        cur.execute(sql)
        for rows in cur.fetchall():
            normalized['menu_item'] = rows[1]



    if 'locations' in order.keys():
        print(order['locations'])
        normalized['room'] = order['locations']
    else:
        sql = "SELECT room_number FROM location WHERE teacher_name = \"" + order['teachers'] + "\"" 
        cur.execute(sql)
        for row in cur.fetchall():
            normalized['room'] = row[0]



def build_engine(engine):
    global cur
    category = {"menu_items" : "1", "locations" : "2", "teachers" : "3", "quantity" : 4} 

    menu_items = get_aliases(category["menu_items"])
    for mi in menu_items:
        engine.register_entity(mi, "menu_items")

    locations = get_aliases(category["locations"])
    for loc in locations:
        engine.register_entity(loc, "locations")

    teachers = get_aliases(category["teachers"])
    for ppl in teachers:
        engine.register_entity(ppl, "teachers")

    quantities = ["1", "2", "3", "4", "5", "one", "two", "three", "four", "five", "some", "a few", "couple"]
    for num in quantities:
        engine.register_entity(num, "quantity")

    order_intent = IntentBuilder("OrderIntent").require("menu_items").optionally("locations").optionally("teachers").optionally("quantity").build()

    engine.register_intent_parser(order_intent)
    return engine


def get_intent(engine, tweet):
    for intent in engine.determine_intent(tweet):
        if intent.get('confidence') > 0:
            return intent
        # insert_order(intent["menu_items"], intent["locations"], intent["teachers"])

engine = build_engine(engine)

tweet = "for 1 chocolates, Stratton"
order = get_intent(engine, tweet)
normalize_order(order)
# insert_order("1", "2", "2")
