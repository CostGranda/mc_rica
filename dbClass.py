from pymongo import MongoClient

#Clase Dao- coneccion a base de datos y a fines
class DbConection():

#  Constructor de coneccion a base de datos
    def __init__(self, user, database, password):
        self.client = MongoClient("mongodb+srv://"+user+":"+password+"@cluster0-2ikpa.mongodb.net/"+database+"?retryWrites=true&w=majority")
        self.db = self.client.get_database(database)

#   Obtiene todos los documentos de una coleccion dada
    def getAll(self, collection):
        records = self.db[collection]
        print(list(records.find()))

#   Insercion de multiples datos a base de datos
    def insertMany(self, collection, jsonlist):
        coll = self.db[collection]
        inserts = coll.insert_many(jsonlist)
        print(inserts) 

#   Insertar un registro
    def insertOne(self, collection, json ):
        coll = self.db[collection]
        insert = coll.insert_one(json)
        print(insert)
        

#instance2 = DbConection('test','IammasterAlfa5')
#instance2.Prueba()


json = [{
    "telefonos": [
        3147289900
    ],
    "especialidades": [
        "FI-BL"
    ],
    "comentarios": [
        ""
    ],
    "cedula": 1017242314,
    "nombres": "Carlos Andrés",
    "apellidos": "Lopera Betancur",
    "ciudad": "Medellín",
    "email": "carlos@gmail.com",
    "disponibilidad": "2020-11-18",
    "cv": "http://ria-env-2.vvpamseyk3.sa-east-1.elasticbeanstalk.com/api/cv/1017242314.pdf/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBZG1pbiIsImlhdCI6OTk5OTk5OTk5OSwiZXhwIjo5OTk5OTk5OTk5fQ.QbQCFQNCnf43SMztVVk6HeRPXvp1jun4hfUx5kBZzfI",
    "calificacion": 1,
    "state": "En proceso",
    "origen": "Manual",
    "content": ""
},
{
    "telefonos": [
        3023001558
    ],
    "especialidades": [
        "ABAP-HANA"
    ],
    "comentarios": [
        "Es un buen muchacho"
    ],
    "cedula": 1036670455,
    "nombres": "Fabio Sebastian",
    "apellidos": "Montoya Arrubla",
    "ciudad": "Medellín",
    "email": "fabio.montoya@perceptio.net",
    "disponibilidad": "2020-11-18",
    "cv": "http://ria-env-2.vvpamseyk3.sa-east-1.elasticbeanstalk.com/api/cv/1017242314.pdf/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBZG1pbiIsImlhdCI6OTk5OTk5OTk5OSwiZXhwIjo5OTk5OTk5OTk5fQ.QbQCFQNCnf43SMztVVk6HeRPXvp1jun4hfUx5kBZzfI",
    "calificacion": 5,
    "state": "En proceso",
    "origen": "Manual",
    "content": ""
}
]

jsonOne = {
    "telefonos": [
        3023001558
    ],
    "especialidades": [
        "ABAP-HANA"
    ],
    "comentarios": [
        "Es un buen muchacho"
    ],
    "cedula": 1036670456,
    "nombres": "Fabio Sebastian",
    "apellidos": "Montoya Arrubla",
    "ciudad": "Medellín",
    "email": "fabio.montoya@perceptio.net",
    "disponibilidad": "2020-11-18",
    "cv": "http://ria-env-2.vvpamseyk3.sa-east-1.elasticbeanstalk.com/api/cv/1017242314.pdf/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBZG1pbiIsImlhdCI6OTk5OTk5OTk5OSwiZXhwIjo5OTk5OTk5OTk5fQ.QbQCFQNCnf43SMztVVk6HeRPXvp1jun4hfUx5kBZzfI",
    "calificacion": 5,
    "state": "En proceso",
    "origen": "Manual",
    "content": ""
}

collection = 'applicants'

#instanciacion de objetos dao y prueba de funcionamiento
#instance = DbConection('','RicaDb','*Perceptio2020')
#Lectura a lista de aplications
#instance.getAll(collection)
#Insercion a colection a base de datos
#instance.insertMany(collect, json)
#Insertar un registro
#instance.insertOne(collection, jsonOne)

