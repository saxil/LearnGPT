
import os
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_ollama import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM

def create_vectorstore(module_path="modules"):
    """Creates a Chroma vector store from the markdown files in the module_path."""
    loader = DirectoryLoader(module_path, glob="*.md")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    embeddings = OllamaEmbeddings(model="mistral:latest")
    vectorstore = Chroma.from_documents(texts, embeddings)
    return vectorstore

def get_tutor_chain(vectorstore):
    """Creates a RetrievalQA chain for the tutor."""
    llm = OllamaLLM(model="mistral:latest") 
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever()
    )
    return qa_chain

