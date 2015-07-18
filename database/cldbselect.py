import psycopg2
import psycopg2.extras
import sys
import pprint
import clprocessfiles
import cldbconfig
from pathlib import Path

class dbselect(object):
    def __init__(self):
        self.conn = None
        x = cldbconfig()
        self.conn_string.format(host = x.getdbhost(), dbname = x.getdbname(), user = x.getdbuser, password = x.getdbpassword())
        self.pathdata = Path(x.getpathdata())

    def connect(self):
        self.conn = psycopg2.connect(self.conn_string)
    def selectmapcompetition(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("select * from fbmapcompetition where mapped = 't'")
                records1 = cursor.fetchall()
                return records1
    def selectteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("select * from fbteams")
                records = cursor.fetchall()
                pprint.pprint(records)
                return records
    def selectmapteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("select * from fbmapteams")
                records = cursor.fetchall()
                return records
    def selectmapteamsfalse(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("select * from fbmapteams where mapped = 'F'")
                records = cursor.fetchall()
                return records
    def selectcountmapteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("select count(*) from fbmapteams")
                records = cursor.fetchone()
                cnt = records['count']
                return cnt


    def selectmapcompetition(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("select * from fbmapcompetition")
                records = cursor.fetchall()
                dct = {}
                for r in records:
                    k = r[0].strip()
                    v = r[1].strip()
                    dct[k] = v
                return dct


if __name__ == '__main__':
    x = dbselect()
    lst = x.selectmapteams()
