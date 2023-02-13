from fastapi import FastAPI, APIRouter
from backend.models.models import *
from backend.database.database_mongo import tasks_db
from bson import ObjectId
from typing import List


router = APIRouter()

#Root
@router.get("/", tags=["Read root"])
async def home():
    return {"Ping":"Pong"}

#Homepage
@router.get("/v1/tasks",tags=["Manage Tasks"])
async def get_all_tasks():
    all_tasks = Tasks_Entity(tasks_db.find())
    if all_tasks:
        return message_response(all_tasks,"Retrive all tasks from database.")
    return message_error("Error","Unable to found tasks.")

#Get all tags
@router.get("v1/tags", tags=["Manage Tasks"])
async def get_all_tags():
    tags = tasks_db.distinct("tag")
    if tags:
        return message_response(tags,"Retrive all tags")
    return message_error("Error:","Unable to found tags")

@router.get("v1/tags/{tag}", tags=["Manage Tasks"])
async def get_all_task_by_specific_tag(tag):
    tasks = Tasks_Entity(tasks_db.find({"tag": tag}))
    if tasks:
        return message_response(tasks,"Tasks by tag: {}".format(tag))
    return message_error("Error:","Unable to fount task with tag: {}".format(tag))



#Get task by task id
@router.get("v1/task/{id}", tags=["Manage Tasks"])
async def get_task_by_id(id):
    
    task = Task_Entity(tasks_db.find_one({"_id": ObjectId(id)}))
    if task:
        return message_response(task,"Task found successfully.")
    return message_error("Error:","Unable to found task id: {}".format(id))

#Create a New task
@router.post("/v1/task", tags=["Manage Tasks"])
async def create_new_task(task: Task):
    task_new = tasks_db.insert_one(dict(task))
    if task_new:
        return message_response(Tasks_Entity(tasks_db.find({"description": task.description})),"Task Created successfully.")
    else:
        return message_error("Error:","Unable to create new task.")

#Update Existing task
@router.put("v1/task/{id}", tags=["Manage Tasks"])
async def update_existing_task(id, task:Task):
    task_update = tasks_db.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(task)})
    if task_update:
        return message_response(Tasks_Entity(tasks_db.find({"_id":ObjectId(id)})),"Task Updated.")
    else:
        return message_error("Error","Unable to update task id: {}".format(id)) 
    
#Delete Existing Task
@router.delete("/v1/task/{id}", tags=["Manage Tasks"])
async def delete_task(id):
    delete_task = tasks_db.find_one_and_delete({"_id":ObjectId(id)})
    if delete_task:
        return message_response("Task ID: {} deleted successfully.".format(id),"Task Deleted.")
    return message_error("Unable to delete task ID: {}".format(id),"Task not found or not exists.")


#test
@router.post("/v1/test_app", tags=["Manage Tests"])
async def create_new_task(task):
    return task

    
    