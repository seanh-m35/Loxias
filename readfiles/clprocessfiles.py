import os
import csv
import datetime
from pathlib import Path
from ..database import cldbconfig as cfg

class processfiles(object):
    def __init__(self):
        print("PROCESSFILES: CONSTRUCTOR")
        x = cfg.cldbconfig()
        self.path = Path(x.getpathdata())
        print("PATH: ", self.path)

    def readfiles(self):
        print("PROCESSFILES =====> readfiles ")
        print("PROCESSFILES: ", self.path)
        lst = self.listdir()
        lstall = self.listfiles(lst)
        for child in lstall:
            with child.open() as f:
                reader = csv.DictReader(f)
                for i, r in enumerate(reader):
                    yield r

#            q = Path(child)
#            print("CHILD: ", child)
#            print("Q: ", q)
#            if q.is_dir():
#                for subchild in q.iterdir():
#                    nn = subchild.name
#                    if nn[0] == ".":
#                        continue

        # lst = [os.path.join(self.path, x) for x in lst]
        # lst = [x for x in lst if os.path.isdir(x)]
        # for d in lst:
        #     #            print 'RF02'
        #     lst1 = os.listdir(d)
        #     lst1 = [os.path.join(d, x) for x in lst1]
        #     lst1 = [x for x in lst1 if os.path.isfile(x)]
        #     for f in lst1:
        #         #   print 'RF03'
        #         with open(f, 'r') as f1:
        #             f1_csv = csv.DictReader(f1)
        #             p1 = os.path.split(f)
        #           #  print 'P1: ', p1[0]
        #             p2 = os.path.split(p1[0])
        #             season = p2[1]
        #          #   print 'RF04'
        #             for i, r in enumerate(f1_csv):
        #                 r['season'] = season
        #                 #      print 'RF05'
        #                 yield r

    def listdir(self):
        lst = [x for x in self.path.iterdir() if x.is_dir()]
        return lst
    def listfiles(self, lst):
        lstall = []
        for x in lst:
            lstf = [y for y in x.iterdir() if y.suffix == ".csv"]
            lstall.extend(lstf)
        return lstall

    def mapteams(self):
        '''Returns a list of teams '''
        setteams = set([])
        for i, t in enumerate(self.readfiles()):
            setteams.add(t['AwayTeam'])
            setteams.add(t['HomeTeam'])
        lst = list(setteams)
        lst.sort()
#        print lst
        return lst

    def mapdivision(self):
        '''Returns a list of divisions '''
        setdiv = set([])
        for d in self.readfiles():
            setdiv.add(d['Div'])
        lst = list(setdiv)
        lst.sort()
        return lst
    def season(self):
        ''' Return dict holding start and end date for each season  key for dict
              is tuple t = (season, division)'''
        setseason = set([])
        dctseason = {}
        for s in self.readfiles():
            sea = s['season']
            dt = self.getdate(s['Date'])
            setseason.add(sea)
            division = s['Div']
            t = (sea, division)
            try:
                d = dctseason[t]
#                print 'D: ', d, sea
                d.add(dt)
                dctseason[t] = d
            except:
                ss = set([dt])
#                print 'DT: ', dt, ss, sea
                dctseason[t] = ss
        lstkeys = dctseason.keys()
        lstkeys.sort()
        dctstartend = {}
        for k in lstkeys:
            dd = dctseason[k]
            lstdates = list(dd)
            lstdates.sort()
            dctstartend[k] = (lstdates[0], lstdates[-1])
        return dctstartend
    def seasonteam(self):
        dct = {}
        for i, s in enumerate(self.readfiles()):
            dt = self.getdate(s['Date'])
            if i < 10:
                print(s)
            sea = s['season']
            div = s['Div']
            t = (sea, div)
            try:
                st = dct[t]
                st.add(s['HomeTeam'])
                st.add(s['AwayTeam'])
                dct[t] = st
            except:
                st = set([])
                st.add(s['HomeTeam'])
                st.add(s['AwayTeam'])
                dct[t] = st
        return dct

    def getdate(self, ds):
        '''  Converts  a dd/mm/yy string into a date object '''
        lst = ds.split('/')
        dd = int(lst[0])
        mm = int(lst[1])
        yy = int(lst[2])
        yyyy = 2000 + yy
        dt = datetime.date(yyyy, mm, dd)
        return dt

if __name__ == '__main__':
    path = '/Users/seanheffernan/Documents/football/results/english/'
    x = processfiles(path)
    dct = x.seasonteam()
#    lst = x.mapteams()
#    lst = x.mapdivision()
#    dct = x.season()
#    print dct
