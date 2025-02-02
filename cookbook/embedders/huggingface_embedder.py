from ethosian.agent import AgentKnowledge
from ethosian.vectordb.pgvector import PgVector
from ethosian.embedder.huggingface import HuggingfaceCustomEmbedder

embeddings = HuggingfaceCustomEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog.")

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Example usage:
knowledge_base = AgentKnowledge(
    vector_db=PgVector(
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        table_name="huggingface_embeddings",
        embedder=HuggingfaceCustomEmbedder(),
    ),
    num_documents=2,
)
