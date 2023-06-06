from sentence_transformers import SentenceTransformer
import json
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "One must take into account the conditions that develop the lives of several women who are at risk, above all, in terms of mental health"
]

embeddings = model.encode(sentences)

with open("vectors.json", "w") as file:
    json.dump(embeddings.tolist()[0], file)

# print(embeddings)