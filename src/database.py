"""
Database interface
"""
import os
from pymongo import MongoClient
from src.utils import isodatetime
from bson.objectid import ObjectId

MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_DATABASE = os.getenv('MONGO_DATABASE', 'igreja')

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


def fetch(collection: str, query: dict = None) -> list:
    """
    Busca na collection todos os documentos que satisfazem a query.
    Caso a query esteja vazia todos os documentos serão retornados.

    Args:
        collection (str): collection onde os documentos serão buscados
        query (dict): query usada para filtrar os documentos

    Returns:
        list: retorna documentos em lista
    """
    return list(db.get_collection(collection).find(query))


def insert_document(collection: str, document: dict) -> tuple:
    """
    Insere um novo documento em uma collection

    Raises:
        ValueError: o parametro document está vazio

    Args:
         collection (str): a collection onde os documentos serao buscados
         document (dict): query usada para filtrar os documentos

    Returns:
        tuple: (id_do_documento_inserido, data_documento_criado)
    """
    document['created_at'] = isodatetime()
    response = db.get_collection(collection).insert_one(document)
    inserted_id = str(response.inserted_id)

    return inserted_id, document['created_at']


def set_document_by_id(collection: str, document_id: str,
                       update_fields: dict) -> str:
    """
    Atualiza documentos baseado no id. Em caso de sucesso, retorna a data
    da atualizacao. Em caso de falha, retorna None

    Args:
        collection (str): collection onde os documentos estao armazenados
        document_id (str): id do documento
        update_fields (dict): campos a serem atualizados

    Returns:
        str: data da alteração
    """
    update_fields['updated_at'] = isodatetime()
    db.get_collection(collection).update_one({
        '_id': ObjectId(document_id)
    }, {
        '$set': update_fields
    })

    return update_fields['updated_at']
