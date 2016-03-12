import json
import sys

from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine
def testing():
	return "hellooooooooo"
engine = IntentDeterminationEngine()



menu_items = [
        "coke",
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
        "201",
        "100"
        ]

for loc in locations:
    engine.register_entity(loc, "location")

teachers = [
        "Stratton",
        "Baydar",
        "Monroe"
        ]

for ppl in teachers:
    engine.register_entity(ppl, "teachers")

order_intent = IntentBuilder("OrderIntent").require("menu_items").optionally("locations").optionally("teachers").build()


engine.register_intent_parser(order_intent)

if __name__ == "__main__":
    for intent in engine.determine_intent(' '.join(sys.argv[1:])):
        if intent.get('confidence') > 0:
            print(json.dumps(intent, indent=4))



