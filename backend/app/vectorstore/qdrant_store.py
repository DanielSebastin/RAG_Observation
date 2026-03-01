from qdrant_client import QdrantClient
from qdrant_client.models import Distance,VectorParams,PointStruct
import uuid

class QdrantStore:
    def __init__(self,client,collection_name,vector_size):
        self.collection_name=collection_name
        self.client=client

        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

    def add_points(self,embeddings,chunks):
        points=[]
        for vector,text in zip(embeddings,chunks):
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector.tolist(),
                    payload={"text":text}
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )