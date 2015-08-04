import psycopg2
import psycopg2.extras
import sys
import pprint
#import clprocessfiles
from . import cldbselect
from . import cldbinsert
from . import cldbconfig as cfg
from pathlib import Path


class dbcreate(object):
    def __init__(self):
        self.conn = None
        x = cfg.cldbconfig()
        self.conn_string = "host = '{0}' dbname = '{1}' user = '{2}' password = '{3}'".format(str(x.getdbhost()), str(x.getdbname()), str(x.getdbuser()), str(x.getdbpassword()))
        self.pathdata = Path(x.getpathdata())

    def connect(self):
        self.conn = psycopg2.connect(self.conn_string)

    def createtablemapteams(self):
        """
        Holds teams names load from various sources. Maps these team names to the
        cannonical team names used in the database
              Man U, Man Utd, Manchester Utd -> Manchester United
        """
        print("MAPTEAMS: ", self.conn_string)
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute('''create table if not exists fbmapteams
                         (teamname varchar(50) primary key, teamid integer, mapped boolean);''')
                print("MAPTEAMS EXECUTE STATUS: ", cursor.statusmessage)
                conn.commit()
                print("MAPTEAMS COMMIT STATUS: ", cursor.statusmessage)

    def createtableteams(self):
        """
        Holds the cannonical team name for each team
        """
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute('''create table if not exists fbteams
                        (teamid integer primary key, teamname varchar(50));''')

    def createtablemapcompetition(self):
        """
        Holds competition ID from various sources and maps them to cannonical
        competition IDs used in the database
        """
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                cursor.execute('''create table if not exists fbmapcompetition
                         (competitionid serial primary key, tier integer, div varchar(5), country char(20),
                          mapped boolean);''')

    def createtablecompetition(self):
        """
        Holds cannonical competition IDs
        """
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
                 cursor.execute('''create table if not exists fbcompetition
                        (competitionid integer primary key, tier integer, competitionname varchar(50));''')


    def createtableseason(self):
        """
        For each competition holds information about each season played
        """
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
               cursor.execute('''create table if not exists fbseason
                       (seasonid char(9), competitionid char(6), seasonstart date,
                       seasonend date, primary key(seasonid, competitionid));''')

    def createtableseasonteam(self):
        """
        For competition/season holds the list of teams
        """
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
        """
        Holds information about each event/game
        """
        with psycopg2.connect(self.conn_string) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  as cursor:
#                try:
#                    cursor.execute('''create type e_eventtype as enum('F', 'R');''')
#                except Exception as e:
#                    print("ERROR createtableevent: " , e)
                try:
                    cursor.execute('''create table if not exists fbevent
                       (eventid serial primary key, seasonid char(9), competitionid char(6),
                       eventdate date, eventtype e_eventtype);''')
                except Exception as e:
                    print("ERROR createtableevent: " , e)

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
 #       self.createtableseasonteam()
        self.createtableevent()
 #       self.createtableeventteam()

if __name__ == '__main__':
    x = dbcreate()
    x.createtables()
