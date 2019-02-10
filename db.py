# -*- coding: utf-8 -*-
import sqlite3


class database:
    def __init__(self):
        self.database = 'database.sqlite' 

        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()

# Remove the table 
#        self.cur.execute(
#        'DROP TABLE IF EXISTS devices;')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deviceName TEXT UNIQUE NOT NULL,
        deviceStatus BOOLEAN NOT NULL
        );''')

        self.close()

    def connect(self):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()

    def addDevice(self, name):
        self.connect()
        aux = self.cur.execute('''
        INSERT INTO devices VALUES(
            NULL,
            '{0}',
            0
        );'''.format(name))
        self.conn.commit()
        self.close()
        return aux

    def getAllDevices(self):
        self.connect()
        allitens = self.cur.execute(
        'SELECT * FROM devices;')

        devc = {}
        for item in allitens:
            func = lambda x : 'on' if (x) else 'off'
            devc[item[1]] = {'status': func(item[2])}
        
        self.close()
        return devc
        
    def getDevice(self, deviceNm):
        self.connect()
        busca = self.cur.execute(
        'SELECT * FROM devices WHERE deviceName=:name;',
        {"name": deviceNm})
        devc = {}
        for item in busca:
            func = lambda x : 'on' if (x) else 'off'
            devc[item[1]] = {'status': func(item[2])}
        
        self.close()
        return devc

    def updateDevice(self, deviceNm, status):
        self.connect()
        func = lambda x: 1 if (x=='on') else 0
        aux = self.cur.execute(
        'UPDATE devices SET deviceStatus=:stat WHERE deviceName=:name;',
        {"stat": func(status), "name": deviceNm})
        self.conn.commit()
        self.close()
        return aux

    def removeDevice(self, deviceNm):
        self.connect()
        aux = self.cur.execute(
        'DELETE FROM devices WHERE deviceName=:name;',
        {"name": deviceNm})
        self.conn.commit()
        self.close()
        return aux

dbsq = database()

'''dbsq.addDevice('lamp1')
print dbsq.getDevice('lamp1')
dbsq.addDevice('lamp2')
dbsq.addDevice('lamp3')

print dbsq.getAllDevices()
dbsq.removeDevice('lamp2')
dbsq.updateDevice('lamp1', 'on')
print dbsq.getAllDevices()
dbsq.close()'''