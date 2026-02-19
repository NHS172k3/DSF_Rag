from dotenv import load_dotenv
import os
from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.supabase import SupabaseVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from llama_index.core import Settings

load_dotenv()

DB_connection_string = os.environ.get("DB_CONNECTION_STRING")

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Settings.llm = Groq(
#     model="llama-3.3-70b-versatile",
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

documents = SimpleDirectoryReader(
    input_dir="./parsed",
    recursive=True
).load_data()

vector_store = SupabaseVectorStore(
    postgres_connection_string=DB_connection_string,
    collection_name="vector_db",
    dimension=384,
)

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context
)

# After creating the index
index.storage_context.persist(persist_dir="./index_store")
