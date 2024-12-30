import os
from typing import List
from pymilvus import (
    connections,
    FieldSchema,
    DataType,
    Collection,
    CollectionSchema,
    Index,
    utility
)

from dotenv import load_dotenv
# load env vars
load_dotenv()

def connect():
    connections.connect(
        alias=os.getenv('DB_ALIAS'), 
        db_name=os.getenv('DB_NAME'), 
        host=os.getenv('DB_HOST'), 
        port=os.getenv('DB_PORT')
        )
    
def createCollection(name: str):
    
    # purpose of this code is just re creating collection each time 
    # for demo purposes
    if (utility.has_collection(name)):
        Collection(name).drop()

    fields = [
        FieldSchema('id', DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema('representation', DataType.VARCHAR, max_length=6000),
        FieldSchema('embedding', DataType.FLOAT_VECTOR, dim=384)
    ]

    schema = CollectionSchema(fields, 'Example for test vector db')
    myCollection = Collection(name, schema)

    index_params = {
        "index_type": "IVF_FLAT",
        "metric_type": "L2",  # "L2" - Euclidian distance, "IP" - inner product 
        "params": {"nlist": 128}
    }

    # Create the index on the "embedding" field
    Index(myCollection, "embedding", index_params)
    
def insertEmbeddings(collection: Collection, embeddings: List):    
    collection.insert(embeddings)
    collection.flush()    
    

