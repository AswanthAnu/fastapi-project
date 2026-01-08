import os
from dotenv import load_env

load_env()

class Settings:
    PROJECT_NAME = 'Car Price API'
    API_KEY = os.getenv('API_KEY')
    JWT_KEY = os.getenv('JWT_KEY')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
    REDIS_URL = os.getenv('REDIS_URL')
    MODEL_PATH = os.getenv('MODEL_PATH')

settings = Settings()