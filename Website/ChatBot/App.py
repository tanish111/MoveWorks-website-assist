import streamlit as st
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstores = FAISS.from_texts(texts=text_chunks,embedding=embeddings)
    return vectorstores
    
def get_text():
    f = open('Data.txt')
    contents = f.read()
    return contents
def get_text_chunk(raw_text):
    text_spliter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_spliter.split_text(raw_text)
    return chunks
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Moveworks",page_icon=":books:")
    st.header("Chat with MoveWorks")
    st.text_input("Ask Questions")
    raw_text = get_text()
    text_chunk = get_text_chunk(raw_text)
    vectorstore = get_vectorstore(text_chunk)
    
    



if __name__ == '__main__':
    main()