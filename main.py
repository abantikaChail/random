from pathlib import Path
import docx
import fitz  # PyMuPDF

def load_txt(file):
    return file.read().decode("utf-8")

def load_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def load_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def load_documents_from_files(uploaded_files):
    documents = []
    for file in uploaded_files:
        if file.name.endswith(".txt"):
            documents.append(load_txt(file))
        elif file.name.endswith(".pdf"):
            documents.append(load_pdf(file))
        elif file.name.endswith(".docx"):
            documents.append(load_docx(file))










from sentence_transformers import SentenceTransformer, util

class QABot:
    def __init__(self, documents):
        self.model = SentenceTransformer('all-mpnet-base-v2')
        self.docs = documents
        self.doc_embeddings = self.model.encode(documents, convert_to_tensor=True)

    def answer_question(self, question):
        question_embedding = self.model.encode(question, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(question_embedding, self.doc_embeddings)[0]
        top_k = scores.topk(3)
        answers = [self.docs[idx] for idx in top_k[1]]
        return "\n---\n".join(answers)







import streamlit as st
from backend.document_loader import load_documents_from_files
from backend.qa_engine import QABot

st.set_page_config(page_title="Local SOP Chatbot", layout="wide")
st.title("📘 Local SOP Chatbot")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_files = st.file_uploader(
    "Upload SOPs or documents (.txt, .pdf, .docx)", 
    type=["txt", "pdf", "docx"], 
    accept_multiple_files=True
)

question = st.text_input("Ask a situation-based question")

if uploaded_files and question:
    with st.spinner("Processing documents..."):
        docs = load_documents_from_files(uploaded_files)
        bot = QABot(docs)
        answer = bot.answer_question(question)

        # Save to chat history
        st.session_state.chat_history.append({"question": question, "answer": answer})

        st.success("Answer generated:")
        st.write(answer)

# Display chat history
if st.session_state.chat_history:
    st.markdown("### 💬 Chat History")
    for i, chat in enumerate(reversed(st.session_state.chat_history), 1):
        st.markdown(f"**Q{i}:** {chat['question']}")
        st.markdown(f"**A{i}:** {chat['answer']}")
        st.markdown("---")

