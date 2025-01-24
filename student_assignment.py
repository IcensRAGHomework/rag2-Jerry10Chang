from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)

    for idx, doc in enumerate(docs, start=1):
        chunks = text_splitter.split_text(doc.page_content) # doc.metadata['source'], doc.metadata['page']
        last_chunk = {
            "file_name": q1_pdf,
            "page_number": idx,
            "content": chunks[-1]  # 取得當前頁面的最後一個 chunk
        }
    return last_chunk["content"]

def hw02_2(q2_pdf):
    pass

print(hw02_1(q1_pdf))