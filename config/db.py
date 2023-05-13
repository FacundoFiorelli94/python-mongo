
from pymongo import MongoClient

conn = MongoClient("mongodb+srv://fakku15fz:Facundo08@cluster0.udbvvaf.mongodb.net/")

db = conn.usersdb
coleccion_users_db = db['usersdb']
result = coleccion_users_db.find()

