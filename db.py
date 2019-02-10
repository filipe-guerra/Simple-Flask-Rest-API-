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

    def addDevice(self, name):
        return self.cur.execute('''
        INSERT INTO devices VALUES(
            NULL,
            '{0}',
            0
        );'''.format(name))
        self.conn.commit()

    def getAllDevices(self):
        allitens = self.cur.execute(
        'SELECT * FROM devices;')

        devc = {}
        for item in allitens:
            func = lambda x : 'on' if (x) else 'off'
            devc[item[1]] = {'status': func(item[2])}
        return devc
        
    def getDevice(self, deviceNm):
        busca = self.cur.execute(
        'SELECT * FROM devices WHERE deviceName=:name;',
        {"name": deviceNm})

        devc = {}
        for item in busca:
            func = lambda x : 'on' if (x) else 'off'
            devc[item[1]] = {'status': func(item[2])}
        return devc

    def updateDevice(self, deviceNm, status):
        func = lambda x: 1 if (x=='on') else 0
        return self.cur.execute(
        'UPDATE devices SET deviceStatus=:stat WHERE deviceName=:name;',
        {"stat": func(status), "name": deviceNm})
        self.conn.commit()

    def removeDevice(self, deviceNm):
        return self.cur.execute(
        'DELETE FROM devices WHERE deviceName=:name;',
        {"name": deviceNm})
        self.conn.commit()

    def close(self):
        self.cur.close()

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