import os
from pathlib import Path

def load_documents(folder_path):
    documents = []
    for file in Path(folder_path).glob("*.txt"):
        with open(file, 'r', encoding='utf-8') as f:
            documents.append(f.read())









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
from backend.document_loader import load_documents
from backend.qa_engine import QABot

st.title("Local SOP Chatbot")

uploaded_files = st.file_uploader("Upload SOPs", type=["txt"], accept_multiple_files=True)
question = st.text_input("Ask a question")

if uploaded_files:
    docs = [file.read().decode("utf-8") for file in uploaded_files]
    bot = QABot(docs)

    if question:
        answer = bot.answer_question(question)
        st.write("### Answer")
        st.write(answer)
