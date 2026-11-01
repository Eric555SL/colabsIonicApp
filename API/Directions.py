# Importacion de librerias
from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
import BackEnd.Functions as Callmethod
import BackEnd.GlobalInfo.ResponseMessages as mensajitos

# Instancia
app=Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin(allow_headers=['Content-Type'])
def Getmessage():
    try:
        objResult=Callmethod.fnMensajeGet()
        return objResult
    except Exception as e:
        print("Error en Getmessage",e)
        return jsonify(mensajitos.err500)

@app.route('/getUsers')
@cross_origin(allow_headers=['Content-Type'])
def fnGetUsers():
    try:
        objResult=Callmethod.fnGetUsers()
        return objResult
    except Exception as e:
        print("Error en Getmessage",e)
        return jsonify(mensajitos.err500)

@app.route('/getColabs')
@cross_origin(allow_headers=['Content-Type'])
def fnGetColabs():
    try:
        objResult=Callmethod.fnGetColabs()
        return objResult
    except Exception as e:
        print("Error en Getmessage",e)
        return jsonify(mensajitos.err500)

@app.route('/deleteUser/<id>', methods=['DELETE'])
@cross_origin(allow_headers=['Content-Type'])
def fnDeleteUser(id):
    try:
        objResult = Callmethod.fnDeleteUsers(id)
        return objResult
    except Exception as e:
        print("Error en ruta deleteUser", e)
        return jsonify(mensajitos.err500)

@app.route('/postUser', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def fnPostUser():
    try:
        objUsers = request.get_json()
        objResult = Callmethod.fnPostUsers(objUsers)
        return objResult
    except Exception as e:
        print("Error en ruta postUser", e)
        return jsonify(mensajitos.err500)

@app.route('/putUser/<id>', methods=['PUT'])
@cross_origin(allow_headers=['Content-Type'])
def fnPutUser(id):
    try:
        objData = request.get_json()
        objResult = Callmethod.fnPutUsers(id, objData)
        return objResult
    except Exception as e:
        print("Error en ruta updateUser:", e)
        return jsonify(mensajitos.err500)
    
@app.route('/buscarUser/<id>', methods=['GET'])
@cross_origin(allow_headers=['Content-Type'])
def fnBuscarUser(id):
    try:
        # Pasa el ID recibido en la URL a la función de búsqueda
        objResult = Callmethod.fnBuscarUser(id)
        return objResult
    except Exception as e:
        print("Error en ruta buscarUser:", e)
        return jsonify(mensajitos.err500)

    
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)