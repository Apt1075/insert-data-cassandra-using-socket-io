import pymongo
def connection_reader():
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    client_reader = pymongo.MongoClient('mongodb://nimbumirchimng2:nm#db002mng@secutrak-2023-10-29-04-44-292.c4pqfsdaiccz.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    mydb_reader = client_reader["nimbu_mirchee_db1"]
    # mydb = myclient["Secutrak"]
    # courier = mydb['courier_trip_detail']
    # cursor = courier.find()
    # documents = list(cursor)
    return mydb_reader


def connection_writer():
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    client_writer = pymongo.MongoClient('mongodb://nimbumirchimng2:nm#db002mng@secutrak-2023-10-29-04-44-29.c4pqfsdaiccz.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    mydb_writer = client_writer["nimbu_mirchee_db1"]
    # mydb = myclient["Secutrak"]
    # courier = mydb['courier_trip_detail']
    # cursor = courier.find()
    # documents = list(cursor)
    return mydb_writer

