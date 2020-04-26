from pymongo import MongoClient

#Clase Dao- coneccion a base de datos y a fines
class DbConection():

#  Constructor de coneccion a base de datos
    def __init__(self, database, password):
        self.client = MongoClient("mongodb+srv://RICA:"+password+"@cluster0-hgvcm.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client.get_database(database)

#   Prueba de coneccion a base de datos, lectura de datos
    def Prueba(self):
        records = self.db.applicants
        print(list(records.find()))

#   Insercion de multiples datos a base de datos
    def insert(self, collect, jsonlist):
        coll = self.db[collect]
        inserts = coll.insert_many(jsonlist)
        print(inserts) 
        

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

collect = 'applicants'
#instanciacion de objetos dao y prueba de funcionamiento
instance = DbConection('RicaDb','*Perceptio2020')
#Lectura a lista de aplications
instance.Prueba()
#Insercion a colection a base de datos
instance.insert(collect, json)

