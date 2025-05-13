"""
Индексация документов для RAG (Sentence Transformers + FAISS)
"""
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from typing import List, Tuple

# TODO: реализовать функции для создания и сохранения индекса

def build_faiss_index(texts, model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
    # TODO: реализовать индексацию
    pass

def build_faiss_index_from_sentences(sentences: List[str], model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2") -> Tuple[faiss.IndexFlatL2, np.ndarray]:
    """Строит эмбеддинги для предложений и индексирует их в FAISS"""
    model = SentenceTransformer(model_name)
    embeddings = model.encode(sentences, show_progress_bar=True, convert_to_numpy=True, normalize_embeddings=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index, embeddings
