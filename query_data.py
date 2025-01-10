import argparse
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are SwitchboardAssistant, an expert guide for entrepreneurs seeking resources and support in Southeastern Ontario.

You need to give the respons in a good way, and bullet points and more than 1 object only. 
"""

def process_query(query_text, chat_history=None):
    try:
        # Initialize OpenAI embeddings with minimal configuration
        embedding_function = OpenAIEmbeddings(
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Initialize Chroma with the embedding function
        db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embedding_function
        )
        
        # Rest of your code...
        results = db.similarity_search_with_relevance_scores(query_text, k=3)
        
        if not results:
            return {"error": "No relevant resources found"}, chat_history
        
        context = "\n".join([doc.page_content for doc, _ in results])
        prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        
        if chat_history:
            formatted_history = "\n".join([f"User: {q}\nAssistant: {r}" for q, r in chat_history[-3:]])
        else:
            formatted_history = ""
        
        # Initialize ChatOpenAI with explicit API key
        chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
        
        response = chat.predict(prompt.format(
            context=context,
            question=query_text,
            history=formatted_history
        ))
        
        updated_history = chat_history if chat_history else []
        updated_history.append((query_text, response))
        
        return {"response": response}, updated_history
        
    except Exception as e:
        print(f"Error in process_query: {str(e)}")  # Add logging
        return {"error": f"An error occurred: {str(e)}"}, chat_history

# Rest of your code remains the same...