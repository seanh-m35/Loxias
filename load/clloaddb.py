import psycopg2
import psycopg2.extras
import sys
import pprint

import loxias.readfiles
#import cldbselect
#import cldbinsert
import loxias.database as db

class loaddb(object):
    def __init__(self):
        self.conn = None
        x = cldbconfig()
        self.conn_string.format(host = x.getdbhost(), dbname = x.getdbname(), user = x.getdbuser, password = x.getdbpassword())
        self.pathdata = Path(x.getpathdata())
        self.setteams = set([])
    def connect(self):
        self.conn = psycopg2.connect(self.conn_string)

    def getrecords(self, lst):
        r = clprocessfiles.processfiles(self.path)
        for i, rec in enumerate(r.readfiles()):
 #           if i < 10:
 #
#               print(rec)
            dct = {}
            for a in lst:
                dct[a] = rec[a]
            yield dct

    def getmapteams(self):
        x = db.dbselect()
        r = x.selectmapteams()
        print(r)
        self.dctteams = {}
        for a in r:
            self.setteams.add(a[0])
            self.dctteams[a[0]] = (a[1], a[2])
        print(len(self.dctteams))
        print(self.dctteams)
    def mapteams(self):
        st = set([])
        sea = set([])
        for i, r in enumerate(self.getrecords(['HomeTeam', 'AwayTeam'])):
            if i < 10:
                print(r)
            if r['HomeTeam'] in self.setteams:
                if r['AwayTeam'] in self.setteams:
                    continue
            if r['HomeTeam'] not in self.setteams:
                st.add(r['HomeTeam'])
            if r['AwayTeam'] not in self.setteams:
                st.add(r['AwayTeam'])
        cnt = len(self.setteams) + 1
        x = cldbinsert.dbinsert()
        for j in st:
            x.insertmapteams(j)
    def teams(self):
        x = cldbselect.dbselect()
        r = x.selectmapteamsfalse()
        y = cldbinsert.dbinsert()
        for t in r:
            y.insertteams(t)
    def getcompetition(self):
        x = cldbselect.dbselect()
        r = x.selectmapcompetition()
        print(r)

    def seasonteam(self):
       self.getcompetition()
       for i, r in enumerate(self.getrecords(['HomeTeam', 'AwayTeam', 'Date', 'season', 'Div', 'FTHG', 'FTAG'])):
            if i < 10:
                print(r)

    def deletetablemapteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("delete from fbmapteams;")
    def updatemapteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute("update fbmapteams set mapped = 't';")


if __name__ == '__main__':
    x = loaddb()
    x.getmapteams()
#    x.createtableevent()
#    x.insertseasonteam()
#    x.seasonteam()
#    x.teams()
 #   x.updatemapteams()
#    x.cancel()
#    x.droptablemapteams()
#    x.droptables()
#    x.createtables()
#    x.createtableseason()
#    x.insertseason()
