from excel import OpenExcel


class BulkLoad():

    def __init__(self, path):
        self.file = OpenExcel(path)
        self.rows = self.file.getRows()

    def read_column(self):
        json = {
            "telefonos": [
                3147289900
            ],
            "especialidades": [
                "FI-BL"
            ],
            "comentarios": [
                ""
            ],
            "cedula": "",
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
        }
        data = []
        for i in range(2, self.rows):
            row = self.file.read(i)
            try:
                json["cedula"] = row[0]
                json["nombres"] = row[1]
                json["apellidos"] = row[2]
                json["ciudad"] = row[3]
                json["skype"] = row[4]
                json["email"] = row[5]
                try:
                    json["telefonos"] = str(int(str(row[6]).replace(" ",''))) # Lista?
                except ValueError:
                    try:
                        json["telefonos"] = int(row[6])
                    except ValueError:
                        str(row[6])
                json["especialidades"] = row[7]
                json["cv"] = "http://190.248.92.106:3100/api/cv/"+row[5].strip()+".pdf/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBZG1pbiIsImlhdCI6OTk5OTk5OTk5OSwiZXhwIjo5OTk5OTk5OTk5fQ.QbQCFQNCnf43SMztVVk6HeRPXvp1jun4hfUx5kBZzfI"
                json["comentarios"] = row[9]
                json["nivel"] = row[10]
                json["calificacion"] = row[11]
                json["state"] = row[12]
                json["origen"] = row[13]
                json["disponibilidad"] = row[14]
                json["ultimafecha"] = row[15]
                json["ubicacion"] = row[16]
            except ValueError:
                continue
            data.append(json)
            json = {}

        return data
            #data.append(json)
        
        #return data


# instance = BulkLoad('data_base.xlsx')
# instance.read_column()

