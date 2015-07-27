from configparser import ConfigParser

class cldbconfig(object):
    def __init__(self):
        print('CONSTRUCTOR: cldbconfig')
        self.cfg = ConfigParser()
        self.cfg.read('/Users/seanheffernan/Development/python/lib/Loxias/database/config.ini')
        print(self.cfg.sections())

    def getdbhost(self):
        return self.cfg.get('database', 'host')
    def getdbname(self):
        return self.cfg.get('database', 'dbname')
    def getdbuser(self):
        return self.cfg.get('database', 'user')
    def getdbpassword(self):
        return self.cfg.get('database', 'password')
    def getpathdata(self):
        return self.cfg.get('path', 'pathdata')

if __name__ == '__main__':
    x = cldbconfig()
    print('DBHOST: ', x.getdbhost())
    print('DBNAME: ', x.getdbname())
    print('DBUSER: ', x.getdbuser())
    print('DBPASSWORD: ', x.getdbpassword())
