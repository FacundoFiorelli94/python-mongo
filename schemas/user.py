
def UserEntity(item) -> dict:
    return {
            "id": str(item['_id']),
            "name": item['name'],
            "email": item['email'],
            "password": item['password']
        }

def UsersEntityList(entity) -> list:
    return [UserEntity(item) for item in entity]