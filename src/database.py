"""
Database interface
"""
import os
from pymongo import MongoClient


MONGO_HOST = os.getenv('MONGO_HOST', 'igreja.qgtij.mongodb.net')
MONGO_DATABASE = os.getenv('MONGO_DATABASE', 'development')

if MONGO_HOST.startswith('localhost'):
    client = MongoClient()
else:
    MONGO_USER = os.getenv('MONGO_USER', 'black')
    MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'black')
    MONGO_OPTIONS = 'retryWrites=true&w=majority'
    MONGO_URL = f'{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/test'

    client = MongoClient(
        f'mongodb+srv://{MONGO_URL}?{MONGO_OPTIONS}'
    )

db = client.get_database(MONGO_DATABASE)

