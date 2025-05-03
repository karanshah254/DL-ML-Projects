import os
import streamlit as st
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import CharacterTextSplitter
import tempfile

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")

st.set_page_config(page_title="Chat with PDF - Groq", layout="centered")

st.title("📘 Chat with PDF (File) using Groq + LangChain")
st.markdown("Choose a PDF source and ask questions about its content.")

# File uploader
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# Initialize session state
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(pages)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_db = FAISS.from_documents(docs, embeddings)

    st.session_state.vector_db = vector_db
    st.success("✅ PDF processed! You can now ask questions.")

# Question input
if st.session_state.vector_db:
    query = st.text_input("Ask a question about the PDF")

    if st.button("Submit") and query:
        retriever = st.session_state.vector_db.as_retriever()
        relevant_docs = retriever.get_relevant_documents(query)

        llm = ChatOpenAI(model="llama3-8b-8192")
        qa_chain = load_qa_chain(llm, chain_type="stuff")

        with st.spinner("Thinking..."):
            answer = qa_chain.run(input_documents=relevant_docs, question=query)

        st.markdown(f"### 🤖 Answer:\n{answer}")
