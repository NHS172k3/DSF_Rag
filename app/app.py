"""
app.py  —  DSF Chatbot
Run:  streamlit run app.py
Expects utils.py in the same directory.
GROQ_API_KEY + DB_CONNECTION_STRING must be set as environment variables
(e.g. via Streamlit Cloud Secrets, Railway, Render, etc.)
"""

import os

import streamlit as st
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.vector_stores.supabase import SupabaseVectorStore

import utils  # LLM + embed settings configured at import time

# ── page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="DSF Chatbot", page_icon="🤖", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg:      #f5f2eb;
    --surface: #ede9e0;
    --border:  #d4cfc4;
    --ink:     #1a1814;
    --muted:   #7a7569;
    --accent:  #c84b31;
    --radius:  4px;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background: var(--bg) !important;
    color: var(--ink) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2.5rem !important; max-width: 720px !important; }

.app-title {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1;
    margin-bottom: 0.15rem;
}
.app-title span { color: var(--accent); }
.app-sub {
    font-size: 0.72rem;
    color: var(--muted);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1.75rem;
}

.chat-window {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.25rem;
    min-height: 380px;
    max-height: 460px;
    overflow-y: auto;
    margin-bottom: 1rem;
}
.chat-window::-webkit-scrollbar { width: 3px; }
.chat-window::-webkit-scrollbar-thumb { background: var(--border); }

.empty-state {
    height: 300px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.8rem; color: var(--muted);
    font-family: 'Syne', sans-serif;
    letter-spacing: 2px; text-transform: uppercase;
}

.msg { margin-bottom: 1.1rem; display: flex; flex-direction: column; gap: 0.2rem; }
.msg.user  { align-items: flex-end; }
.msg.bot   { align-items: flex-start; }
.msg-label {
    font-size: 0.6rem; letter-spacing: 2px;
    text-transform: uppercase; color: var(--muted);
    font-family: 'Syne', sans-serif;
}
.bubble {
    max-width: 82%; padding: 0.7rem 1rem;
    font-size: 0.9rem; line-height: 1.6;
    border-radius: var(--radius);
}
.bubble.user { background: var(--ink); color: var(--bg); }
.bubble.bot  { background: #fff; border: 1px solid var(--border); color: var(--ink); }

.stTextInput input {
    background: #fff !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    color: var(--ink) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
}
.stTextInput input:focus {
    border-color: var(--accent) !important;
    box-shadow: none !important;
}

.stButton button, [data-testid="stFormSubmitButton"] button {
    background: var(--accent) !important;
    color: #fff !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.75rem !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: var(--radius) !important;
    padding: 0.5rem 1.2rem !important;
    transition: opacity 0.15s !important;
}
.stButton button:hover, [data-testid="stFormSubmitButton"] button:hover { opacity: 0.82 !important; }

.ghost button {
    background: transparent !important;
    color: var(--muted) !important;
    border: 1px solid var(--border) !important;
    font-size: 0.7rem !important;
}
.ghost button:hover { color: var(--ink) !important; }

hr { border-color: var(--border) !important; }
.stCaption { color: var(--muted) !important; font-size: 0.7rem !important; }
</style>
""", unsafe_allow_html=True)


# ── password gate ──────────────────────────────────────────────────────────────
def check_password():
    if st.session_state.get("authenticated"):
        return  # already in, continue running the rest of the app

    st.markdown(
        '<div class="app-title">DSF <span>Chat</span></div>'
        '<div class="app-sub">Enter password to continue</div>',
        unsafe_allow_html=True,
    )
    with st.form("login_form"):
        pw = st.text_input("Password", type="password", placeholder="••••••••")
        submitted = st.form_submit_button("Enter")

    if submitted:
        if pw == os.environ.get("APP_PASSWORD", ""):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Wrong password.", icon="🔒")

    st.stop()  # only reached when NOT authenticated

check_password()


# ── load index (cached) ────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def get_engine():
    db_conn = os.environ.get("DB_CONNECTION_STRING")
    vector_store = SupabaseVectorStore(
        postgres_connection_string=db_conn,
        collection_name="vector_db",
        dimension=384,
    )
    storage_context = StorageContext.from_defaults(
        persist_dir="./index_store",
        vector_store=vector_store,
    )
    index = VectorStoreIndex.from_vector_store(
        vector_store,
        storage_context=storage_context,
    )
    return utils.get_query_engine(index)


try:
    query_engine = get_engine()
except Exception as e:
    st.error(f"Could not load index: {e}")
    st.stop()


# ── header ─────────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="app-title">DSF <span>Chat</span></div>'
    '<div class="app-sub">Document Intelligence · Groq · LlamaIndex</div>',
    unsafe_allow_html=True,
)


# ── session state ──────────────────────────────────────────────────────────────
MAX_HISTORY = 20
if "history" not in st.session_state:
    st.session_state.history = []


# ── chat window ────────────────────────────────────────────────────────────────
html = '<div class="chat-window" id="chat-end">'
if not st.session_state.history:
    html += '<div class="empty-state">Ask a question to get started</div>'
else:
    for msg in st.session_state.history:
        role  = msg["role"]
        text  = msg["text"].replace("<", "&lt;").replace(">", "&gt;")
        label = "You" if role == "user" else "Bot"
        html += (
            f'<div class="msg {role}">'
            f'  <div class="msg-label">{label}</div>'
            f'  <div class="bubble {role}">{text}</div>'
            f'</div>'
        )
html += "</div>"
st.markdown(html, unsafe_allow_html=True)
st.markdown(
    "<script>const c=document.getElementById('chat-end');if(c)c.scrollTop=c.scrollHeight;</script>",
    unsafe_allow_html=True,
)


# ── input ──────────────────────────────────────────────────────────────────────
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input(
            "q", placeholder="Ask anything about your documents…",
            label_visibility="collapsed",
        )
    with col2:
        submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    st.session_state.history.append({"role": "user", "text": user_input})

    with st.spinner("Thinking…"):
        try:
            response_text = str(utils.answer_question(query_engine, user_input, history=st.session_state.history[:-1]))
        except Exception as e:
            response_text = f"⚠ {e}"

    st.session_state.history.append({"role": "bot", "text": response_text})

    if len(st.session_state.history) > MAX_HISTORY:
        st.session_state.history = st.session_state.history[-MAX_HISTORY:]

    st.rerun()

elif submitted:
    st.warning("Type a message first.", icon="✏️")


# ── footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
c1, c2 = st.columns([1, 4])
with c1:
    st.markdown('<div class="ghost">', unsafe_allow_html=True)
    if st.button("🗑 Clear"):
        st.session_state.history = []
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
with c2:
    n = len(st.session_state.history)
    st.caption(f"{n // 2} turn(s) in session" if n else "No messages yet")