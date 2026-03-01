from qdrant_client import QdrantClient
from app.embeddings.embedder import Embedder


class Retriever:

    def __init__(self,embedding_model="all-MiniLM-L6-v2"):
        self.embedder=Embedder(embedding_model)
        self.client=QdrantClient(path="qdrant_storage")

    def search_collection(self,collection_name,query,k=3):

        query_vector=self.embedder.embed([query])[0]

        results=self.client.query_points(
            collection_name=collection_name,
            query=query_vector.tolist(),
            limit=k
        )

        formatted=[]
        for hit in results.points:
            formatted.append({
                "score":hit.score,
                "text":hit.payload["text"]
            })

        return formatted

    def retrieve(self,query,k=3):

        print("\nSearching rag_fixed...")
        fixed_results=self.search_collection("rag_fixed",query,k)

        print("Searching rag_semantic...")
        semantic_results=self.search_collection("rag_semantic",query,k)

        return {
            "fixed":fixed_results,
            "semantic":semantic_results
        }
    def close(self):
        self.client.close()