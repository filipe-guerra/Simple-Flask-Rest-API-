from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

devices = {
    'device1': {'status': 'off'},
    'device2': {'status': 'off'},
    'device3': {'status': 'on'},
}

def abort_if_doestn_exist(device_id):
    if device_id not in devices:
        abort(404, message="Device {} doesn't exist".format(device_id))

parser = reqparse.RequestParser()
parser.add_argument('status')

class returnDevices(Resource):
    def get(self, device_id):
        abort_if_doestn_exist(device_id)
        return {device_id: devices[device_id]}

    def delete(self, device_id):
        abort_if_doestn_exist(device_id)
        del devices[device_id]
        return '', 204

    def put(self, device_id):
        args = parser.parse_args()
        status = {'status': args['status']}
        devices[device_id] = status
        return status, 201

class all_Devices(Resource):
    def get(self):
        return devices

    def post(self):
        args = parser.parse_args()
        device_id = int(max(devices.keys()).lstrip('devices')) + 1
        device_id = 'device%i' % device_id
        devices[device_id] = {'status' : args['status']}
        return devices[device_id], 201

api.add_resource(returnDevices, '/<string:device_id>')
api.add_resource(all_Devices, '/')


#   todos os devices
#   curl http://localhost:5000/

#   primeiro device
#   curl http://localhost:5000/device1

#   delete device
#   curl http://localhost:5000/device3 -X DELETE -v

#   add device
#   curl http://localhost:5000/ -d "status=somethig new" -X POST -v

#   update a task
#   curl http://localhost:5000/device3 -d "status=something different" -X PUT -v
