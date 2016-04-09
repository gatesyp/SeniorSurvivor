import pprint
import sys
import MySQLdb

db = MySQLdb.connect(host="stoh.io",user="fashionksu", passwd="lollipop123", db="seniorsurvivor")
cur = db.cursor()


def get_price(item_id, quantity):
	global cur
	sql = "SELECT price FROM items WHERE id = \"" + str(item_id) + "\" AND available = 1"
	cur.execute(sql)
	price = None
	
	for row in cur.fetchall():
		price = float(row[0]) * float(quantity)
	return str(price)



def get_items():
        global cur
        sql = "SELECT * FROM aliases"
        cur.execute(sql)

        alias_list = list()

        for row in cur.fetchall():
                alias_list.append(row)

        sql = "SELECT id, name FROM items"
        cur.execute(sql)

        for row in cur.fetchall():
                alias_list.append(row)

            
        return alias_list

def get_rooms():
        global cur
        sql = "SELECT room FROM locations"
        cur.execute(sql)

        room_list = list()
        for row in cur.fetchall():
                room_list.append(row)
        return room_list

def get_quantities():
        global cur
        sql = "SELECT * FROM quantities"
        cur.execute(sql)

        quantity_list = list()
        for row in cur.fetchall():
                quantity_list.append(row)
        return quantity_list

def insert_order(order):
    print("insert_order")
    global cur
    global db
    print order['extras']
    sql = "insert into orders(item_id, quantity, name, room, completed, extras) VALUES (" + order['id']+ ", " + order['quantity'] + ", \"" + order['handle'] + "\", \"" + order['room'] + "\" , 0, \"" + order['extras'] + "\")"
    print(sql)
    cur.execute(sql)
    db.commit()
