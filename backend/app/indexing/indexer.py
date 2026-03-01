from app.utils.loader import load_document
from app.chunking.fixed import fixed_chunk
from app.chunking.semantic import semantic_chunk
from app.embeddings.embedder import Embedder
from app.vectorstore.qdrant_store import QdrantStore
from qdrant_client import QdrantClient
from app.evaluation.benchmark import measure_time


class Indexer:

    def __init__(self,embedding_model="all-MiniLM-L6-v2"):
        self.embedder=Embedder(embedding_model)

    def ingest(self,document_path):

        print("Loading document...")
        text=load_document(document_path)

        print("Creating fixed chunks...")
        fixed_chunks=fixed_chunk(text,chunk_size=500,overlap=100)

        print("Creating semantic chunks...")
        semantic_chunks=semantic_chunk(text,max_chunk_size=500)

        print("Creating fixed chunks...")
        fixed_chunks,fixed_chunk_time = measure_time(
            fixed_chunk,
            text,
            500,
            100
        )

        print("Creating semantic chunks...")
        semantic_chunks,semantic_chunk_time = measure_time(
            semantic_chunk,
            text,
            500
        )

        print("Embedding fixed chunks...")
        fixed_embeddings,fixed_embed_time = measure_time(
            self.embedder.embed,
            fixed_chunks
        )

        print("Embedding semantic chunks...")
        semantic_embeddings,semantic_embed_time = measure_time(
            self.embedder.embed,
            semantic_chunks
        )

        vector_size=fixed_embeddings.shape[1]

        # 🔥 CREATE ONLY ONE CLIENT
        client=QdrantClient(path="qdrant_storage")

        print("Storing fixed chunks in Qdrant...")
        fixed_store=QdrantStore(client,"rag_fixed",vector_size)
        fixed_store.add_points(fixed_embeddings,fixed_chunks)

        print("Storing semantic chunks in Qdrant...")
        semantic_store=QdrantStore(client,"rag_semantic",vector_size)
        semantic_store.add_points(semantic_embeddings,semantic_chunks)
        
        print("Fixed chunks:", len(fixed_chunks))
        print("Semantic chunks:", len(semantic_chunks))
        
        print("Fixed chunks:", len(fixed_chunks))
        print("Semantic chunks:", len(semantic_chunks))

        print("Ingestion Complete.")