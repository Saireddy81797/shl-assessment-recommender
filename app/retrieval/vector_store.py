from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from app.retrieval.catalog_loader import load_catalog

model = SentenceTransformer("all-MiniLM-L6-v2")

catalog = load_catalog()

texts = [
    f"{item['name']} {item['description']}"
    for item in catalog
]

embeddings = model.encode(texts)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def search_catalog(query, k=5):
    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        k
    )

    results = []

    for idx in indices[0]:
        results.append(catalog[idx])

    return results
