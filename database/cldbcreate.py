import psycopg2
import psycopg2.extras
import sys
import pprint
import clprocessfiles
import cldbselect
import cldbinsert

class dbcreate(object):
    def __init__(self):
        self.conn = None
        self.path = '/home/sean/football/data/England/'
        self.conn_string = "host='localhost' dbname='footballdb' user='postgres' password='password'"

    def connect(self):
        conn_string = "host='localhost' dbname='footballdb' user='postgres' password='password'"
        print "Connecting to database\n  -->%s" % (conn_string)
        self.conn = psycopg2.connect(conn_string)

    def createtablemapteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute('''create table if not exists fbmapteams
                         (teamname varchar(50) primary key, teamid integer, mapped boolean);''')
    def createtableteams(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute('''create table if not exists fbteams
                        (teamid integer primary key, teamname varchar(50));''')
    def createtablemapcompetition(self):
         with psycopg2.connect(self.conn_string) as conn:
             with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                  cursor.execute('''create table if not exists fbmapcompetition
                         (competitionname varchar(50) primary key, competitionid char(6),
                          mapped boolean);''')
    def createtablecompetition(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                 cursor.execute('''create table if not exists fbcompetition
                        (competitionid char(6) primary key, competitionname varchar(50));''')


    def createtableseason(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
               cursor.execute('''create table if not exists fbseason
                       (seasonid char(9), competitionid char(6), seasonstart date,
                       seasonend date, primary key(seasonid, competitionid));''')
    def createtableseasonteam(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute('''create table if not exists fbseasonteam
                        (seasonid char(9), competitionid char(6),
                        teamid integer references fbteams, updown char(1), currentrating integer,
                        homerating integer, awayrating integer, numberofgames integer,
                        primary key (seasonid, competitionid, teamid),
                        foreign key (seasonid, competitionid)
                        references fbseason (seasonid, competitionid));''')
    def createtableevent(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                #               cursor.execute('''create type e_eventtype as enum('F', 'R');''')
               cursor.execute('''create table if not exists fbevent
                       (eventid serial primary key, seasonid char(9), competitionid char(6),
                       eventdate date, eventtype e_eventtype);''')
    def createtableeventteam(self):
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
               cursor.execute('''create type e_homeaway as enum('H', 'A');''')
               cursor.execute('''create type e_result as enum('W', 'D', 'L');''')
               cursor.execute('''create table if not exists fbeventteam
                       (eventid integer references fbevent, teamid integer references fbteams,
                       result e_result,
                       homeaway e_homeaway, rating integer, homerating integer,
                       awayrating integer, percentrating integer);''')
    def createtables(self):
 #       self.createtableseason()
        self.createtableseasonteam()
 #       self.createtableevent()
 #       self.createtableeventteam()

if __name__ == '__main__':
    x = dbcreate()
    x.createtables()
