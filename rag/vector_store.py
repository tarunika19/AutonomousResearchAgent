import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.chunks = []

    def create_embeddings(self, chunks):
        """
        Convert text chunks into embeddings and store them in FAISS.
        """
        embeddings = self.model.encode(chunks)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(np.array(embeddings, dtype=np.float32))

        self.chunks = chunks

    def search(self, query, k=3):
        """
        Search for the most relevant chunks.
        """
        query_embedding = self.model.encode([query])

        distances, indices = self.index.search(
            np.array(query_embedding, dtype=np.float32),
            k,
        )

        results = []

        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results

    def save(self, index_path="vector_index.faiss",
         metadata_path="metadata.pkl"):

        faiss.write_index(self.index, index_path)
        with open(metadata_path, "wb") as f:
            pickle.dump(self.chunks, f)

    def load(self, index_path="vector_index.faiss",
         metadata_path="metadata.pkl"):

        self.index = faiss.read_index(index_path)
        with open(metadata_path, "rb") as f:
             self.chunks = pickle.load(f)