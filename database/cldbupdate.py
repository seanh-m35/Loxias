import psycopg2
import psycopg2.extras
import sys
import pprint
import clprocessfiles

class dbupdate(object):
    def __init__(self):
        self.conn = None
        self.path = '/home/sean/football/data/England/'
        self.conn_string = "host='localhost' dbname='footballdb' user='postgres' password='tqbfjot1d'"

    def connect(self):
        conn_string = "host='localhost' dbname='footballdb' user='postgres' password='tqbfjot1d'"
        print "Connecting to database\n  -->%s" % (conn_string)
        self.conn = psycopg2.connect(conn_string)
    def updatemapteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("update fbmapteams set mapped = 't';")



if __name__ == '__main__':
    x = loaddb()
#    x.createtableevent()
#    x.insertseasonteam()
    x.insertmapteams()
 #   x.updatemapteams()
#    x.cancel()
#    x.droptablemapteams()
#    x.droptables()
#    x.createtables()
#    x.createtableseason()
#    x.insertseason()
