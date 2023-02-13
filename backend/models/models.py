from pydantic import BaseModel
import datetime



class Task(BaseModel):
    
    tag: str
    description: str
    creation_date: str = datetime.datetime.now().strftime("%d/%m/%y")
    check: bool = False
    
def message_response(data, message):
    
    return {
        "data": data,
        "status_code": 200,
        "message": message
    }

def message_error(data, message):
    
    return{
        "data": data,
        "status_code": 400,
        "message": message
    }
    
def Task_Entity(task)->dict:
    
    return {
        "id": str(task["_id"]),
        "tag": task["tag"],
        "description": task["description"],
        "creation_date": task["creation_date"],
        "check": task["check"],
    }
    
def Tasks_Entity(entity)->list:
    
    return [Task_Entity(task) for task in entity]

def TestResponse(data):
    return {
        "data": data
    }