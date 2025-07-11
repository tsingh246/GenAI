import streamlit as st

def main():
    st.set_page_config(page_title="Multi PDF Chat", page_icon=":books:", layout="wide")
    st.header("Multi PDF Chat Application")
    st.write("This is a simple application to chat with multiple PDFs.")
    st.text_input("Ask your question about your documents here:")
    with st.sidebar:
        st.subheader("Upload PDFs")
        st.file_uploader("Choose PDF files")
        st.button("Process PDFs")
    
 
if __name__ == "__main__":
    main()
