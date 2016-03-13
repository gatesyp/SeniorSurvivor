import MySQLdb
db = None
def connect():    
	global db
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
		    user="root",         # your username
		    passwd="admin",  # your password
		    db="seniorsurvivor")
	cur = db.cursor()
	return cur;

def commit_db():
	global db
	db.commit()

