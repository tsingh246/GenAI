import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


# from langchain.text_splitter import CharacterTextSplitter
def get_pdf_text(pdf_files):
    text= ""
    for pdf_file in pdf_files:
        # Read the PDF file
        pdf_reader = PdfReader(pdf_file)
        # Extract text from each page
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text

def get_text_chunks(text):
    # Create a text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    # Split the text into chunks
    text_chunks = text_splitter.split_text(text)
    return text_chunks    

def create_vector_store(text_chunks):
    # Create embeddings
    embeddings = OpenAIEmbeddings()
    # Create a vector store using FAISS
    vector_store = FAISS.from_texts(text_chunks, embeddings)
    return vector_store

def main():
    load_dotenv(".env")
    st.set_page_config(page_title="Multi PDF Chat", page_icon=":books:", layout="wide")
    st.header("Multi PDF Chat Application")
    st.write("This is a simple application to chat with multiple PDFs.")
    st.text_input("Ask your question about your documents here:")
    with st.sidebar:
        st.subheader("Upload PDFs")
        pdf_docs=st.file_uploader("Choose PDF files", accept_multiple_files=True, type=["pdf"])
        print("get pdf fpcs **********",pdf_docs)
        if st.button("Process PDFs"):
            with st.spinner("Processing PDFs..."):
                if pdf_docs:
                    for pdf in pdf_docs:
                        st.write(f"Uploading {pdf.name}...")

                        st.success(f"{pdf.name} uploaded successfully!")
                else:
                    st.error("Please upload at least one PDF file.")
                
                #Get PDF text content
                raw_text = get_pdf_text(pdf_docs)
                #st.write("Extracted Text:",raw_text)
            
                # Get the text chunks
                text_chunks = get_text_chunks(raw_text)
                #st.write("Text Chunks:", text_chunks)
                 # Create vector store
                vector_store = create_vector_store(text_chunks)   
                st.write("Vector Store Created Successfully!")
                st.write("Vector Store:", vector_store)
                st.write(FAISS.get_by_ids(vector_store, [0, 1, 2]))  # Example to get first three vectors
                

        
    
 
if __name__ == "__main__":
    main()
