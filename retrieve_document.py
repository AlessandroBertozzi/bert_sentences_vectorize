from scrolling import scrolling
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
import json

# take environment variables from .env.
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

print("https://" + DB_HOST + ":" + DB_PORT)
# Database connection
client = Elasticsearch(
    "https://" + DB_HOST + ":" + DB_PORT,
    basic_auth=(DB_USER, DB_PASS),
    verify_certs=True,
    request_timeout=10
)

query = {
    "match_all": {}
}

filtered_documents = list()
result = scrolling(client, index="scre_cache", query=query, scroll_size=500)

for document in result:

    abstract = ""
    for abstract in document['normalized_abstract']:
        if abstract['lang'] == 'en':
            abstract = abstract['text']
        else:
            abstract = ""

    title = ""
    for title in document['normalized_title']:
        if title['lang'] == 'en':
            title = title['text']
        else:
            title = ""

    if abstract != "" and title != "":
        filtered_document = {
            "id": document['_id'],
            "title": title,
            "abstract": abstract,
        }

        filtered_documents.append(filtered_document)

print(len(filtered_documents))
# _id
# abstract in eng: normalized_abstract in eng
# title: normalized_title in eng

with open("documents_test.json", "w") as file:
    json.dump(filtered_documents, file)
