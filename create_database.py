from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai 
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

CHROMA_PATH = "chroma"
DATA_PATH = "data"

def ensure_directories():
    """Create necessary directories if they don't exist."""
    for directory in [DATA_PATH, CHROMA_PATH]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

def load_documents():
    # Ensure data directory exists
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
        print(f"Created {DATA_PATH} directory")
        return []

    documents = []
    for filename in os.listdir(DATA_PATH):
        if filename.endswith('.md'):
            try:
                file_path = os.path.join(DATA_PATH, filename)
                loader = TextLoader(file_path, encoding='utf-8')
                documents.extend(loader.load())
                print(f"Loaded {filename} successfully")
            except Exception as e:
                print(f"Error loading {filename}: {str(e)}")
    return documents

def split_text(documents: list[Document]):
    if not documents:
        print("No documents to split!")
        return []
        
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    if chunks:
        document = chunks[0]
        print("\nExample chunk content:")
        print(document.page_content)
        print("\nMetadata:", document.metadata)

    return chunks

def save_to_chroma(chunks: list[Document]):
    if not chunks:
        print("No chunks to save to Chroma!")
        return

    # Ensure Chroma directory exists
    if not os.path.exists(CHROMA_PATH):
        os.makedirs(CHROMA_PATH)
        print(f"Created {CHROMA_PATH} directory")
    else:
        shutil.rmtree(CHROMA_PATH)
        os.makedirs(CHROMA_PATH)
        print(f"Recreated {CHROMA_PATH} directory")

    api_key = os.getenv("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    
    try:
        db = Chroma.from_documents(
            chunks, embeddings, persist_directory=CHROMA_PATH
        )
        db.persist()
        print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")
    except Exception as e:
        print(f"Error saving to Chroma: {str(e)}")

def main():
    # Ensure all necessary directories exist
    ensure_directories()
    
    print("Loading documents...")
    documents = load_documents()
    
    if not documents:
        print("No documents were loaded. Please check your data directory.")
        return
        
    print("\nSplitting text...")
    chunks = split_text(documents)
    
    print("\nSaving to Chroma...")
    save_to_chroma(chunks)
    print("Done!")

if __name__ == "__main__":
    main()