import psycopg2
import psycopg2.extras
import sys
import pprint
# relative import
from ..readfiles import *
#import cldbselect
#import cldbinsert
from ..database import *
import cldbconfig as cfg
from pathlib import Path


class loaddb(object):
    def __init__(self):
        self.conn = None
        x = cfg.cldbconfig()
        self.conn_string.format(host = x.getdbhost(), dbname = x.getdbname(), user = x.getdbuser, password = x.getdbpassword())
        self.pathdata = Path(x.getpathdata())
        self.setteams = set([])

    def connect(self):
        self.conn = psycopg2.connect(self.conn_string)

    def loadteams(self, rec):
        """
        Loads teams and IDs
        """
#   create table if not exists fbteams
#       (teamid integer primary key, teamname varchar(50));
        pass

    def loadmapteams(self, rec):
        """
        Loads a list of teams and IDs
        """
# create table if not exists fbmapteams
#        (teamname varchar(50) primary key, teamid integer, mapped boolean);
        pass

    def loadcompetitions(self, competitions):
        """
        Loads competitions
        Args
           competitions -> dct key (season, div) value set of teams
        """
#                cursor.execute('''create table if not exists fbcompetition
#                        (competitionid integer primary key, country varchar(20));''')
        pass

    def loadmapcompetittion(self, competitions):
#                cursor.execute('''create table if not exists fbmapcompetition
#                         (div varchar(5) primary key, competitionid integer,
#                          mapped boolean);''')
        pass

    def loadseasons(self, seasons):
#              cursor.execute('''create table if not exists fbseason
#                       (seasonid char(9), competitionid char(6),
#                        competitionname varchar(50),  seasonstart date,
#                        seasonend date, primary key(seasonid, competitionid));''')
        pass

    def loadseasonteam(self, seasonteams):
        """
               Args
           seasonteams -> dct key (season, div) value set of teams

        """
#  create table if not exists fbseasonteam
#   (seasonid char(9), competitionid char(6),
#    teamid integer references fbteams, updown char(1), currentrating integer,
#    homerating integer, awayrating integer, numberofgames integer,
#    primary key (seasonid, competitionid, teamid),
#    foreign key (seasonid, competitionid)
#    references fbseason (seasonid, competitionid));''')
       pass

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
