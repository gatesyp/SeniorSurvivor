import json
import sys


from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

engine = IntentDeterminationEngine()

def build_engine(engine):
	menu_items = [
	        "coke12",
	        "pepsi",
	        "coke zero",
	        "candy",
	        "resees", 
	        "cokes",
	        "pepsis",
	        "coke zeros",
	        "candies"
	        ]
	
	for mi in menu_items:
	    engine.register_entity(mi, "menu_items")
	
	locations = [
	        "room 201",
		"room 100",
	        "201",
	        "100"
	        ]
	
	for loc in locations:
	    engine.register_entity(loc, "locations")
	
	teachers = [
	        "Stratton",
	        "Baydar",
	        "Monroe"
	        ]
	
	for ppl in teachers:
	    engine.register_entity(ppl, "teachers")
	
	order_intent = IntentBuilder("OrderIntent").require("menu_items").optionally("locations").optionally("teachers").build()
	
	engine.register_intent_parser(order_intent)
	return engine


def get_intent(engine, tweet):
	for intent in engine.determine_intent(tweet):
		if intent.get('confidence') > 0:
			print(json.dumps(intent, indent=4))
# engine = build_engine(engine)
# tweet = "coke for,pepsi,  room 201, Baydar"
# get_intent(engine, tweet)
