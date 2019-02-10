API Rest simples desenvolvida em Flask, salvando as informações num bando de dados SQLite3, com comandos para adicionar, remover e atualizar os dados.


#   all devices status
#   curl http://localhost:5000/

#   device1 status (device já adicionado anteriormente) 
#   curl http://localhost:5000/device1

#   delete device1
#   curl http://localhost:5000/device1 -X DELETE -v

#   add device5
#   curl http://localhost:5000/ -d "argumento=device5" -X POST -v

#   update a task
#   curl http://localhost:5000/device5 -d "argumento=on" -X PUT -v


Starting Flask

# Debug Mode activated
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

# Debug Mode not activated
export FLASK_APP=app.py
export FLASK_ENV
flask run
