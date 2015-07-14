import psycopg2
import psycopg2.extras
import sys
import pprint
import clprocessfiles
import cldbselect
import cldbinsert

class dbdrop(object):
    def __init__(self):
        self.conn = None
        self.path = '/home/sean/football/data/England/'
        self.conn_string = "host='localhost' dbname='footballdb' user='postgres' password='password'"

    def connect(self):
        conn_string = "host='localhost' dbname='footballdb' user='postgres' password='password'"
        print "Connecting to database\n  -->%s" % (conn_string)
        self.conn = psycopg2.connect(conn_string)

    def droptablemapteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
               cursor.execute("drop table if exists fbmapteams;")
    def droptableteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("drop table if exists fbteams;")
    def droptablemapcompetition(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("drop table if exists fbmapcompetition;")
    def droptablecompetition(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("drop table if exists fbcompetition;")
    def droptableseason(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("drop table if exists fbseason;")
    def droptableseasonteam(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("drop table if exists fbseasonteam;")
    def droptableevent(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("drop table if exists fbevent;")
    def droptableeventteam(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("drop table if exists fbeventteam;")



    def droptables(self):
#        self.droptableeventteam()
#        self.droptableevent()
        self.droptableseasonteam()
#        self.droptableseason()
#        self.droptablecompetition()
#        self.droptablemapcompetition()



if __name__ == '__main__':
    x = dbdrop()
    x.droptables()
