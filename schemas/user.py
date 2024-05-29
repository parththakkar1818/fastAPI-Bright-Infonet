# Normal way
def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "rollNumber":item["rollNumber"],
        "standard":item["standard"],
        "marks":item["marks"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
