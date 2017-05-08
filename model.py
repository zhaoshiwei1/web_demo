import os
import sqlite3

class sqldb:
    def __init__(self):
           if os.path.exists("web_test.db3"):
               self.conn = sqlite3.connect("web_test.db3")
               self.cu = self.conn.cursor()
           else:
               # self.conn = sqlite3.connect("msg.db")
               # self.cu = self.conn.cursor()
               # self.cu.execute("""create table msgs(
               #          id integer primary key,
               #          name text,
               #          date text,
               #          content text) """)
               # self.cu.execute("""insert into msgs values(1,'Ahai','2010-05-19 15:11:20','Ahi alaws be ok!')""")
               # self.conn.commit()
                print "FILE NOT FOUND, PLEASE CHECK THE PATH!"