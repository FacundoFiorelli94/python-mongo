from fastapi import APIRouter, Response
from config.db import coleccion_users_db
from models.user import User
from schemas.user import UserEntity, UsersEntityList
from passlib.hash import sha256_crypt
from bson.objectid import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

### All User Routes
@user.get('/users')
async def get_all_users():
    usersGet = UsersEntityList(coleccion_users_db.find())
    return {'status':' ok', 'data': usersGet, 'message': 'Listado de usuarios'}

### Id Find
@user.get('/users/{id}')
def find_users(id: str):
    return UserEntity(coleccion_users_db.find_one({"_id": ObjectId(id)}))
                           

### Post Routes (Crear Users)
@user.post('/users')
def create_users(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    #insert in db
    id = coleccion_users_db.insert_one(new_user)
    user = coleccion_users_db.find_one({"_id": id.inserted_id})
    return UserEntity(user)
    

### Put - Update Users
@user.put('/users/{id}')
def update_users(id: str, user: User):
    coleccion_users_db.find_one_and_update({"_id": ObjectId(id)}, {"$s  et": dict(user)})

### Delete - Delete Users
@user.delete('/users/{id}')
def delete_users(id: str):
    UserEntity(coleccion_users_db.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)