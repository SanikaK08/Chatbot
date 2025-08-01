from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

def load_pdf(data):
    loader=DirectoryLoader(data,
                           glob="*.pdf",
                           loader_cls=PyPDFLoader)
    
    documents=loader.load()
    return documents


def text_split(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=50,chunk_overlap=10)
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks


def download_huggingface_embedding():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings