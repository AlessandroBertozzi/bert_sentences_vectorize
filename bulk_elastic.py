from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv
import os
import json
from tqdm import tqdm

# take environment variables from .env.
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Database connection
client = Elasticsearch(
    "https://" + DB_HOST + ":" + DB_PORT,
    basic_auth=(DB_USER, DB_PASS),
    verify_certs=True,
    request_timeout=10
)


# load data
with open("final_embeddings.json", "r") as file:
    data = json.load(file)

bulk_list = list()
for document in tqdm(data):

    doc = {
        "_index": "semantic_search_test",
        "_source": {
            "document_id": document['id'],
            "bert_features": document['embedding'],
            "sentence": document['sentence']
        }
    }

    bulk_list.append(doc)
# print(bulk_list)

helpers.bulk(client, bulk_list)


