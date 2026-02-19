from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.supabase import SupabaseVectorStore
from llama_index.llms.groq import Groq
import os
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Configure Groq LLM once
Settings.llm = Groq(
    model="llama-3.3-70b-versatile",
    api_key=os.environ.get("GROQ_API_KEY"),
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Read prompt templates once
with open("../prompts/answer_prompt.txt") as f:
    ANSWER_PROMPT = f.read()
with open("../prompts/quiz_prompt.txt") as f:
    QUIZ_PROMPT = f.read()

# Load your LlamaIndex (retrieval engine)
def get_query_engine(index):
    return index.as_query_engine()

# Generate LLM output
def generate_response(prompt):
    return Settings.llm.complete(prompt)

def format_history(history: list) -> str:
    """Convert session history into a readable string for the prompt."""
    if not history:
        return "No previous conversation."
    lines = []
    for msg in history:
        role = "User" if msg["role"] == "user" else "Assistant"
        lines.append(f"{role}: {msg['text']}")
    return "\n".join(lines)

def answer_question(query_engine, user_question, history=None):
    chunks = query_engine.query(user_question)
    chat_history = format_history(history or [])
    prompt = ANSWER_PROMPT.format(
        retrieved_chunks=chunks,
        chat_history=chat_history,
        user_question=user_question,
    )
    return generate_response(prompt)

def generate_quiz(query_engine, user_question):
    chunks = query_engine.query(user_question)
    prompt = QUIZ_PROMPT.format(retrieved_chunks=chunks)
    return generate_response(prompt)