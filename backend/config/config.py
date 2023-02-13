import os


class config_env:
    
    DEFAULT_DB_NAME: str = "todo_app"
    DB_NAME: str = os.getenv("db", DEFAULT_DB_NAME)
    DB_HOST: str = "mongodb://todo_app"
    DEFAULT_DB_PORT: int = 27017
    DB_PORT: int = int(os.getenv("db_port",DEFAULT_DB_PORT))

config_env = config_env()