import numpy as np
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self,model_name="all-MiniLM-L6-v2"):
        self.model=SentenceTransformer(model_name)

    def embed(self,texts):
        embeddings=self.model.encode(texts)
        return np.array(embeddings).astype("float32")