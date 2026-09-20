import tempfile
from pathlib import Path
import streamlit as st
from ingestion import load_pdfs, split_documents
from rag import answer_question, build_vector_store

st.set_page_config(page_title="Financial Document Intelligence", page_icon="📄", layout="wide")
st.title("📄 Financial Document Intelligence RAG")
st.caption("Ask grounded questions over financial PDFs.")

if "store" not in st.session_state:
    st.session_state.store = None

files = st.file_uploader("Upload financial PDFs", type=["pdf"], accept_multiple_files=True)

if st.button("Index documents", type="primary"):
    if not files:
        st.warning("Upload at least one PDF first.")
    else:
        with tempfile.TemporaryDirectory() as tmp:
            paths = []
            for f in files:
                p = Path(tmp) / f.name
                p.write_bytes(f.getbuffer())
                paths.append(str(p))
            with st.spinner("Extracting, chunking and embedding..."):
                pages = load_pdfs(paths)
                chunks = split_documents(pages)
                st.session_state.store = build_vector_store(chunks)
            st.success(f"Indexed {len(pages)} pages into {len(chunks)} chunks.")

question = st.text_input("Ask a question", placeholder="What was the reported revenue in the latest annual report?")
if st.button("Ask") and question:
    if st.session_state.store is None:
        st.warning("Index documents before asking a question.")
    else:
        with st.spinner("Retrieving evidence and generating answer..."):
            answer, sources = answer_question(st.session_state.store, question)
        st.subheader("Answer")
        st.write(answer)
        with st.expander("Retrieved evidence"):
            for i, doc in enumerate(sources, 1):
                st.markdown(f"**{i}. {doc.metadata.get('source_file','unknown')} — page {doc.metadata.get('page_number','?')}**")
                st.write(doc.page_content[:1500])
