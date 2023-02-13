import pymongo

#Connect to Database

client = pymongo.MongoClient("mongodb://database:27017",                    
                    username='rootuser',
                    password='rootpass',) #Host with Docker
database = client["todo_app"]

#Database Collections
tasks_db = database['tasks']