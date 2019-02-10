#   todos os devices
#   curl http://localhost:5000/

#   primeiro device
#   curl http://localhost:5000/device1

#   delete device
#   curl http://localhost:5000/device3 -X DELETE -v

#   add device
#   curl http://localhost:5000/ -d "argumento=lamp44" -X POST -v

#   update a task
#   curl http://localhost:5000/device3 -d "argumento=on" -X PUT -v

#   Starting Flask Debug Mode
#   export FLASK_APP=app.py
#   export FLASK_ENV=development
#   flask run