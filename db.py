# -*- coding: utf-8 -*-
import sqlite3

class database:
    def __init__(self):
        
        self.conn = sqlite3.connect('database.sqlite')
        self.cur = self.conn.cursor()

        self.cur.execute(
        'DROP TABLE IF EXISTS devices;')

        self.cur.execute('''
        CREATE TABLE devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deviceName TEXT UNIQUE NOT NULL,
        deviceStatus BOOLEAN NOT NULL
        );''')

    def dothis(self,cmd):
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
        
        self.conn.commit()
        # https://www.sqlite.org/lang_select.html
    #    sqlstr = 'SELECT org, count FROM Devices'


        '''print "Devices:"
        for row in cur.execute(sqlstr) :
            print str(row[0]), row[1]
        '''
        self.cur.close()

    def addDevice(self, name):
        return self.cur.execute('''
        INSERT INTO devices VALUES(
            NULL,
            '{0}',
            0
        )'''.format(name))
        self.commitAndClose()

    def allDevices(self):
        allitens = self.cur.execute(
        'SELECT * FROM devices')

        devc = {}
        for item in allitens:
            func = lambda x : 'on' if (x) else 'off'
            devc[item[1]] = {'status': func(item[2])}
        
        return devc
        
    def getDevice(self, deviceNm):
        return self.cur.execute(
        'SELECT * FROM devices WHERE deviceName=?',
        deviceNm)

    def updateDevice(self, deviceNm, status):
        func = lambda x: 1 if (x=='on') else 'off'
        return self.cur.execute(
        'UPDATE devices SET deviceStatus=:stat WHERE deviceName=:name',
        {"stat": func(status), "name": deviceNm})

    def removeDevice(self, deviceNm):
        return self.cur.execute(
        'DELETE FROM devices WHERE deviceName=:name',
        {"name": deviceNm})
        

    def commitAndClose(self):
        self.conn.commit()
        self.cur.close()

dbsq = database()

dbsq.addDevice('lamp1')
dbsq.addDevice('lamp2')
dbsq.addDevice('lamp3')
print dbsq.allDevices()
dbsq.removeDevice('lamp2')
dbsq.updateDevice('lamp1', 'on')
print dbsq.allDevices()