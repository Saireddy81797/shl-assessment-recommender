from app.retrieval.catalog_loader import load_catalog

catalog = load_catalog()

def search_catalog(query, k=5):
    query = query.lower()

    scored = []

    for item in catalog:
        text = f"{item['name']} {item['description']}".lower()

        score = sum(word in text for word in query.split())

        scored.append((score, item))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [item for _, item in scored[:k]]
