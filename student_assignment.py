from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)

    # for idx, doc in enumerate(docs, start=1):
    #     chunks = text_splitter.split_text(doc.page_content) # doc.metadata['source'], doc.metadata['page']        
    #     print(len(chunks))
    # print(type(chunks[-1]))
    # return chunks[-1]
    split_docs = text_splitter.split_documents(docs)
    # for idx, doc in enumerate(split_docs):
    #     print(f"Document {idx + 1}:\n{doc.page_content}\n")

    return split_docs[-1]

def hw02_2(q2_pdf):
    pass

print(hw02_1(q1_pdf))