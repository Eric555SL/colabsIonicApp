from flask import jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import BackEnd.GlobalInfo.ResponseMessages as mensajitos
import BackEnd.GlobalInfo.Keys as ColabsKeys

if ColabsKeys.dbconn==None:
    mongoConnect=MongoClient(ColabsKeys.strConnection)
    ColabsKeys.dbconn=mongoConnect[ColabsKeys.strDBConnection]
    dbUsers=ColabsKeys.dbconn["clUsuarios"]
    dbColabs=ColabsKeys.dbconn["clColabs"]

def fnGetUsers():
    try:
        arrFinalUser=[]
        objQuery=dbUsers.find({})
        listUsers=list(objQuery)
        if len(listUsers)!=0:
            for objUser in listUsers:
                print(objUser)
                objFormateado={
                    "_id":str(objUser['_id']),
                    "strCorreo":objUser["strCorreo"],
                    "strPassword":objUser['strPassword'],
                    "strRol":objUser['strRol'],
                }
                arrFinalUser.append(objFormateado)
        objResponse=mensajitos.succ200.copy()
        objResponse['Respuesta']=arrFinalUser
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fngetusers",e)
        return jsonify(mensajitos.err500)


def fnGetColabs():
    try:
        arrFinalColab=[]
        objQuery=dbColabs.find({})
        listColabs=list(objQuery)
        if len(listColabs)!=0:
            for objColab in listColabs:
                print(objColab)
                objFormateado={
                    "_id":str(objColab['_id']),
                    "strNombre":objColab["strNombre"],
                    "strApellido":objColab['strApellido'],
                    "strPuesto":objColab['strPuesto'],
                    "floatSueldo":objColab['floatSueldo'],
                    "strPuesto":objColab['strPuesto'],
                    "strRfc":objColab['strRfc'],
                }
                arrFinalColab.append(objFormateado)
        objResponse=mensajitos.succ200.copy()
        objResponse['Respuesta']=arrFinalColab
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fngetusers",e)
        return jsonify(mensajitos.err500)

def fnDeleteUsers(id):
    try:
        print("Los datos que eliminare: ", id)
        dbUsers.delete_one({"_id": ObjectId(id)})
        objResponse = mensajitos.succ200.copy()
        objResponse['Informacion_Borrada'] = True
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnDeleteUsers", e)
        return jsonify(mensajitos.err500)

def fnPostUsers(objUser):
    try:
        print("Los datos para insertar: ", objUser)
        strCorreo = objUser.get("strCorreo")
        strPassword = objUser.get("strPassword")
        strRol = objUser.get("strRol")
        resultado = dbUsers.insert_one({
            "strCorreo": strCorreo,
            "strPassword": strPassword,
            "strRol": strRol
        })
        objResponse = mensajitos.succ200.copy()
        objResponse['id_insertado'] = str(resultado.inserted_id)
        objResponse['Informacion_Insertada'] = True
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnPutUsers", e)
        return jsonify(mensajitos.err500)

def fnPutUsers(id, objData):
    try:
        print("ID a modificar:", id)
        print("Nuevos datos:", objData)
        
        datos_actualizar = {}
        if "strCorreo" in objData:
            datos_actualizar["strCorreo"] = objData["strCorreo"]
        if "strPassword" in objData:
            datos_actualizar["strPassword"] = objData["strPassword"]
        if "strRol" in objData:
            datos_actualizar["strRol"] = objData["strRol"]

        # Usamos $set para actualizar solo los campos enviados
        resultado = dbUsers.update_one(
            {"_id": ObjectId(id)},
            {"$set": datos_actualizar}
        )
        
        if resultado.matched_count == 0:
            return jsonify({"status": 404, "message": "Usuario no encontrado"})

        objResponse = mensajitos.succ200.copy()
        objResponse['Informacion_Actualizada'] = True
        return jsonify(objResponse)
        
    except Exception as e:
        print("Error en fnUpdateUser:", e)
        return jsonify(mensajitos.err500)
    
def fnBuscarUser(id):
    try:
        print("ID recibido para búsqueda:", id)
        
        # Validar si el ID recibido es un ObjectId válido de MongoDB
        if not ObjectId.is_valid(id):
            return jsonify({"status": 400, "message": "El ID proporcionado no es válido"})

        # Consulta en MongoDB usando find_one
        usuario = dbUsers.find_one({"_id": ObjectId(id)})

        # Si no existe el registro
        if not usuario:
            return jsonify({"status": 404, "message": "Usuario no encontrado", "Respuesta": None})

        # Convertir ObjectId a String para que pueda convertirse a JSON sin error
        usuario["_id"] = str(usuario["_id"])

        objResponse = mensajitos.succ200.copy()
        objResponse['Respuesta'] = usuario
        return jsonify(objResponse)

    except Exception as e:
        print("Error en fnBuscarUser:", e)
        return jsonify(mensajitos.err500)
    
def fnMensajeGet():
    try:
        return jsonify({"Mensaje": "Hola mundos"})
    except Exception as e:
        return jsonify({"Error":str(e)})