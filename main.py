from dbClass import DbConection
from bulk_load import BulkLoad


db_connection = DbConection('testCarga','RicaDb','sPOPee8nKt7MBAvC')
bulkload = BulkLoad('data_base.xlsx')

data = bulkload.read_column()
db_connection.insertOne('applicants',data)