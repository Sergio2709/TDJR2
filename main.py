import datetime
import re

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from flask_jwt_extended import create_access_token
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app=Flask(__name__)
cors = CORS(app)

app.config["JWT_SECRET_KEY"] = "TDJR-API"

headers = {"Content-Type": "application/json; charset=utf-8"}

@app.route("/login", methods=['POST'])
def autenticacion():
    datos = request.get_json()
    urlBack = dataConfig["url-backend-seguridad"]+'/usuarios/validar'
    cabeceras = headers
    rta = request.post(urlBack, json=datos, headers=cabeceras)
    if rta.status_code == 200:
        usr = rta.jason()    #jason o json??
        vida_token = datetime.timedelta(seconds=60*60*24)
        token = create_access_token(identity=usr, expires_delta=vida_token)
        return jsonify({"token": token, "user_id":usr["id"]})
    else:
        return jsonify({"mensaje":"usuario o clave incorrectos"}), 401


@app.before_request
def before_request_callback():
    endPoint = limpiarPath(request.path)
    rutas_excluidas = ["/login"]
    if rutas_excluidas.__contains__(endPoint):
        pass
    elif verify_jwt_in_request():
        usr = get_jwt_identity()
        if usr["rol"] is not None:
            tieneAcceso = validarAcceso(usr["rol"]["id"], endPoint, request.method)
            if not tieneAcceso:
                return jsonify({"Mensaje":"Permiso denegado"}), 401
            else:
                return jsonify({"mensaje":"Permiso denegado"})


#Espacio para los microsevicios como estan en el transaccional
#1
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    print("Microservicio de listar candidatos")
    urlBack = dataConfig["url-backend-transaccional"] + '/candidatos'
    cabeceras = headers
    rta = request.get(urlBack, headers=cabeceras)
    json = rta.jason()
    return jsonify(json)

#2
@app.route("/candidatos", methods=['GET'])
def crearCandidato():
    print("Microservicio de crear candidato")
    urlBack = dataConfig["url-backend-transaccional"] + '/candidatos'
    cabeceras = headers
    rta = request.post(urlBack, headers=cabeceras)
    json = rta.jason()
    return jsonify(json)



#Fin del espacio


def validarAcceso(idRol, url, metodo):
    urlBack = dataConfig["url-backend-seguridad"]+'/permisoRol/valida-permiso/rol/ + str(idRol)'
    cabeceras = headers
    body = {
        "url"
        "metodo"
    }
    rta = request.get(urlBack, json=body, headers=cabeceras)
    acceso = False
    datos = rta.jason()  #jason o json??
    if ("id" in datos):
        acceso = True
    return acceso


def limpiarPath(url):
    secciones = url.split("/")
    for seccion in secciones:
        if re.search('\\d',seccion):
            url = url.replace(seccion, "?")
    return url

#Accesos
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Servidor del API en ejecucion"
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as file:
        data = json.load(file)
    return data

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__=='__main__':
    print_hi('API Gateway Ciclo 4 Mision TIC 2022 TDVJ')
    dataConfig = loadFileConfig()
    print("Server ejecutandose : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

