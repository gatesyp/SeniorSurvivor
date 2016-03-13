import MySQLdb, json
import db_connect

cur = db_connect.connect()
        
def insert_order():
        sql = 'SELECT * FROM orders '
        # print(sql)
        cur.execute(sql)
        for row in cur.fetchall():
                print(row[3])
