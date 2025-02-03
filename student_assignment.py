from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    split_docs = text_splitter.split_documents(docs)
    return split_docs[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    full_text = "\n".join(doc.page_content for doc in docs)

    text_splitter = RecursiveCharacterTextSplitter(chunk_overlap=0, chunk_size=20, separators=[r'(?m)(?=^\s*第\s.*(?:條|章).*)'], is_separator_regex=True)
    split_docs = text_splitter.split_text(full_text)
    return len(split_docs)
