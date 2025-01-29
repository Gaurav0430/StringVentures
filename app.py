import streamlit as st
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pypdf import PdfReader
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Chat with PDF", layout="wide")
st.title("📄 Chat with PDF using Google Generative AI")


api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

def process_pdf():
    pdf_reader = PdfReader(uploaded_file)
    text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/msmarco-distilbert-base-v4")
    st.session_state.vector_store = FAISS.from_texts(chunks, embeddings)
    
    return len(pdf_reader.pages)

def get_relevant_context(query, vector_store, k=3):
    relevant_docs = vector_store.similarity_search(query, k=k)
    context = "\n".join([doc.page_content for doc in relevant_docs])
    return context

if uploaded_file:
    st.success("📄 PDF Uploaded Successfully!")
    num_pages = process_pdf()
    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**Total Pages:** {num_pages}")


    user_question = st.text_input("Ask a question about the PDF:")
    if user_question:
        if st.session_state.vector_store is not None:

            context = get_relevant_context(user_question, st.session_state.vector_store)
            
            prompt = f"""Based on the following context from the PDF document, please answer the question.
            
            Context:
            {context}
            
            Question: {user_question}
            
            Please provide a clear and concise answer based only on the information provided in the context."""

            response = model.generate_content(prompt)
            

            st.session_state.chat_history.append(("You", user_question))
            st.session_state.chat_history.append(("AI", response.text))
            
            st.write("AI:", response.text)

    if st.session_state.chat_history:
        st.subheader("Chat History")
        for i, (role, msg) in enumerate(st.session_state.chat_history):
            st.text_area(f"{role} {i+1}", value=msg, height=100, disabled=True)