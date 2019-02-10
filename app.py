from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from db import *

app = Flask(__name__)
api = Api(app)

'''{
    'device1': {'status': 'off'},
    'device2': {'status': 'off'},
    'device3': {'status': 'on'},
}'''

def abort_if_doestn_exist(argumento):
    if argumento not in dbsq.getAllDevices():
        abort(404, message="Device {} doesn't exist".format(argumento))

parser = reqparse.RequestParser()
parser.add_argument('argumento')

class returnDevices(Resource):
    def get(self, device_name):
        abort_if_doestn_exist(device_name)
        return dbsq.getDevice(device_name)

    def delete(self, device_name):
        abort_if_doestn_exist(device_name)
        dbsq.removeDevice(device_name)
        return '', 204

    def put(self, device_name): 
        args = parser.parse_args()
        dbsq.updateDevice(device_name, args['argumento'])
        return "", 201

class all_Devices(Resource):
    def get(self):
        return dbsq.getAllDevices()

    def post(self):
        args = parser.parse_args()

        dbsq.addDevice(args['argumento'])
        return dbsq.getDevice(args['argumento']), 201

api.add_resource(returnDevices, '/<string:device_name>')
api.add_resource(all_Devices, '/')