import json
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import spacy

# initialize models
nlp = spacy.load("en_core_web_md")
model = SentenceTransformer('all-MiniLM-L6-v2')

# load data
with open("documents_test.json", "r") as file:
    data = json.load(file)

final_embeddings = list()
for document in tqdm(data):
    doc = nlp(document['abstract'])
    sentences = [sent.text for sent in doc.sents]
    embeddings = model.encode(sentences)

    for sentence, embedding in zip(sentences, embeddings):

        doc_embedded = {
            "id": document['id'],
            "sentence": sentence,
            "embedding": embedding.tolist(),
        }

        final_embeddings.append(doc_embedded)


with open("final_embeddings.json", "w") as file:
    json.dump(final_embeddings, file)

