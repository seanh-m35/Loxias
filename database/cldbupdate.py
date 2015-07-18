import psycopg2
import psycopg2.extras
import sys
import pprint
import clprocessfiles
import cldbconfig
from pathlib import Path

class dbupdate(object):
    def __init__(self):
        self.conn = None
        x = cldbconfig()
        self.conn_string.format(host = x.getdbhost(), dbname = x.getdbname(), user = x.getdbuser, password = x.getdbpassword())
        self.pathdata = Path(x.getpathdata())

    def connect(self):
        self.conn = psycopg2.connect(self.conn_string)
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
