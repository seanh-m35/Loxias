import psycopg2
import psycopg2.extras
import sys
import pprint
import clprocessfiles
import cldbselect

class dbinsert(object):
    def __init__(self):
        self.conn = None
        self.path = '/home/sean/football/data/England/'
        self.conn_string = "host='localhost' dbname='footballdb' user='postgres' password='password'"

    def connect(self):
        conn_string = "host='localhost' dbname='footballdb' user='postgres' password='password'"
        print "Connecting to database\n  -->%s" % (conn_string)
        self.conn = psycopg2.connect(conn_string)


    def insertmapteams(self, team):
        x = cldbselect.dbselect()
        cnt = x.selectcountmapteams() + 1
        lstdct = []
        c = {'teamname':team, 'teamid':cnt, 'mapped':'F'}

        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                try:
                    cursor.execute('''insert into fbmapteams
                     (teamname, teamid, mapped)
                     values (%(teamname)s, %(teamid)s, %(mapped)s)''', c)
                    print('INSERTED: ', c)
                except:
                    print(sys.exc_info()[:2])

    def insertteams(self, team):
        dct = {}
        dct['teamid'] = team[1]
        dct['teamname'] = team[0]

        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute('''insert into fbteams
                         (teamid, teamname)
                         values (%(teamid)s, %(teamname)s)''', dct)
                print('INSERTED: ', dct)
    def insertcompetition(self):
        x = clprocessfiles.processfiles(self.path)
        lst = x.mapdivision()
        lstcompetition = []
        for r in lst:
            dct = {'competitionname':r, 'competitionid':'ENG000', 'mapped':'f'}
            lstcompetition.append(dct)

        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                for d in lstcompetition:
                    print d
                    cursor.execute('''insert into fbmapcompetition
                                  (competitionname, competitionid, mapped)
                         values (%(competitionname)s, %(competitionid)s, %(mapped)s)''', d)

    def insertseason(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                x = clprocessfiles.processfiles(self.path)
                dctcompetition = self.selectmapcompetition()
                dctseason = x.season()
                lst = dctseason.keys()
                lst.sort()
                lstall = []
                for k in lst:
                    print k, dctseason[k], dctcompetition
                    dct = {'seasonid':k[0], 'competitionid':dctcompetition[k[1]],
                            'seasonstart':dctseason[k][0], 'seasonend':dctseason[k][1]}
                    cursor.execute('''insert into fbseason (seasonid, competitionid, seasonstart,
                            seasonend) values (%(seasonid)s, %(competitionid)s,
                            %(seasonstart)s, %(seasonend)s);''', dct)

    def insertseasonteam(self):
        teams = self.selectmapteams()
        dctteams = {}
        for team in teams:
            dctteams[team[0]] = team[1]
#        print dctteams
        dctdivs = self.selectmapcompetition()
        print dctdivs
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                x = clprocessfiles.processfiles(self.path)
                dct = x.seasonteam()
                for k, v in dct.items():
                    lst = list(v)
                    lst.sort()
                    d = {}
                    print k
                    seasonid = k[0]
                    competitionid = dctdivs[k[1]]
                    homerating = 0
                    awayrating = 0
                    numberofgames = 0
                    teamid = ''
                    dctteam = {}
                    for r in lst:
                        teamid = dctteams[r]
                        dctteam = {'seasonid':seasonid, 'competitionid':competitionid,
                                   'teamid':teamid, 'currentrating':0, 'homerating':0,
                                   'awayrating':0, 'numberofgames':0}
                        cursor.execute('''insert into fbseasonteam
                                        (seasonid, competitionid, teamid, currentrating,
                                         homerating, awayrating, numberofgames)
                                        values (%(seasonid)s, %(competitionid)s, %(teamid)s,
                                                %(currentrating)s, %(homerating)s,
                                                %(awayrating)s, %(numberofgames)s)''', dctteam)

    def insertmapcompetition(self):
        lst = self.selectmapcompetition()
        lstcompetition = []
        for r in lst:
            dct = {}
            dct['competitionid'] = r[1]
            dct['competitionname'] = r[0]
            lstcompetition.append(dct)
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                for c in lstcompetition:
                    cursor.execute('''insert into fbcompetition
                         (competitionid, competitionname)
                         values (%(competitionid)s, %(competitionname)s)''', c)

if __name__ == '__main__':
    x = dbinsert()
