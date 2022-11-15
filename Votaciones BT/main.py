from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

import pymongo
import certifi

app=Flask(__name__)
cors = CORS(app)
#importar controladores
#Candidato
from Controladores.ControladorCandidato import ControladorCandidato
controllerCandidato=ControladorCandidato()
#Mesa
from Controladores.ControladorMesa import ControladorMesa
controllerMesa=ControladorMesa()
#Partido
from Controladores.ControladorPartido import ControladorPartido
controllerPartido=ControladorPartido()
#Resultados
from Controladores.ControladorResultados import ControladorResultados
controllerResultado=ControladorResultados()

#Accesos
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Servidor en ejecución ..."
    return jsonify(json)

#Micro Servicio de Listado de Candidatos
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    print("Micro Servicio Listando los candidatos...")
    json=controllerCandidato.index()
    return jsonify(json)

#Micro Servicio de Creacion de Candidatos
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    print("Micro Servicio Creando candidato....")
    data = request.get_json()
    json=controllerCandidato.create(data)
    return jsonify(json)

#Consultar candidato
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    print("Micro Servicio de Consultar el candidato con id: " + id)
    json=controllerCandidato.show(id)
    return jsonify(json)

#Actualizar Candidato
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    print("Micro Servicio Actualizando candidato: " + id)
    data = request.get_json()
    json=controllerCandidato.update(id,data)
    return jsonify(json)

#Eliminar Candidato
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    print("Micro Servicio Se eliminara el candidato con id: " + id)
    json=controllerCandidato.delete(id)
    return jsonify(json)



#************************************************* MESA ****************************************************************
#Micro Servicio de Listado de Estudiantes
@app.route("/mesas",methods=['GET'])
def getmesas():
    print("Micro Servicio Listando las mesas de votación...")
    json=controllerMesa.index()
    return jsonify(json)

#Micro Servicio de Creacion de Candidatos
@app.route("/mesas",methods=['POST'])
def crearMesa():
    print("Micro Servicio Creando la mesa de votación....")
    data = request.get_json()
    json=controllerMesa.create(data)
    return jsonify(json)

#Consultar candidato
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    print("Micro Servicio de Consultar la mesa con id: " + id)
    json=controllerMesa.show(id)
    return jsonify(json)

#Actualizar Mesa
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    print("Micro Servicio Actualizando la mesa con: " + id)
    data = request.get_json()
    json=controllerMesa.update(id,data)
    return jsonify(json)

#Eliminar Mesa
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    print("Micro Servicio Se eliminara la mesa con id: " + id)
    json=controllerMesa.delete(id)
    return jsonify(json)

#*********************************************************************************************************************


#************************************************* PARTIDO ****************************************************************
#Micro Servicio de Listado de los partidos politicos
@app.route("/partidos",methods=['GET'])
def getpartidos():
    print("Micro Servicio Listando los partidos politicos...")
    json=controllerPartido.index()
    return jsonify(json)

#Micro Servicio de Creacion de partidos
@app.route("/partidos",methods=['POST'])
def crearPartido():
    print("Micro Servicio Creando los partidos politicos....")
    data = request.get_json()
    json=controllerPartido.create(data)
    return jsonify(json)

#Consultar partido
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    print("Micro Servicio de Consultar el partido politico con id: " + id)
    json=controllerPartido.show(id)
    return jsonify(json)

#Actualizar partido
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartidos(id):
    print("Micro Servicio Actualizando los partidos politicos: " + id)
    data = request.get_json()
    json=controllerPartido.update(id,data)
    return jsonify(json)

#Eliminar Partido
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    print("Micro Servicio Se eliminara el partido politico con id: " + id)
    json=controllerPartido.delete(id)
    return jsonify(json)

#*********************************************************************************************************************

#************************************************* RESULTADOS ****************************************************************
#Micro Servicio de Listado de los Resultados de las votaciones
@app.route("/resultados",methods=['GET'])
def getResultados():
    print("Micro Servicio Listando los resultados de las votaciones...")
    json=controllerResultado.index()
    return jsonify(json)

#Micro Servicio de los resultados
@app.route("/resultados",methods=['POST'])
def crearResultado():
    print("Micro Servicio Creando los resultados de las votaciones....")
    data = request.get_json()
    json=controllerResultado.create(data)
    return jsonify(json)

#Consultar resultados
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    print("Micro Servicio de Consultar los resultados de las votaciones con id: " + id)
    json=controllerResultado.show(id)
    return jsonify(json)

#Actualizar resultados
@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultado(id):
    print("Micro Servicio Actualizando los resultados de las votaciones: " + id)
    data = request.get_json()
    json=controllerResultado.update(id,data)
    return jsonify(json)

#Eliminar Resultados
@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    print("Micro Servicio Se eliminaran los resultados de las votaciones con id: " + id)
    json=controllerResultado.delete(id)
    return jsonify(json)

#*********************************************************************************************************************


def loadFileConfig():
    with open('config.json') as file:
        data = json.load(file)
    return data

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__=='__main__':
    print_hi('Ciclo 4 Mision TIC 2022 TDVJ')
    dataConfig = loadFileConfig()
    print("Server ejecutandose : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])





""" 
ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://usuario-votaciones:Pruebas2022@cluster0.b1xs3bm.mongodb.net/bd-registro-votaciones?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

baseDatos = client["bd-registro-votaciones"]
print(baseDatos.list_collection_names())
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
