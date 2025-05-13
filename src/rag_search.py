"""
Поиск релевантных фрагментов по вопросу (FAISS)
"""
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Tuple

# TODO: реализовать функцию поиска

def search_relevant_chunks(question, index, texts, model):
    # TODO: реализовать поиск
    pass

def search_relevant_sentences(question: str, index: faiss.IndexFlatL2, sentences: List[str], model: SentenceTransformer, top_k: int = 5) -> List[Tuple[str, float]]:
    """Ищет топ-k релевантных предложений по вопросу через FAISS"""
    q_emb = model.encode([question], convert_to_numpy=True, normalize_embeddings=True)
    D, I = index.search(q_emb, top_k)
    results = []
    for idx, dist in zip(I[0], D[0]):
        results.append((sentences[idx], dist))
    return results
