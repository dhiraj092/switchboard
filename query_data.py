import argparse
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Verify API key is loaded
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables")

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are SwitchboardAssistant, an expert guide for entrepreneurs seeking resources and support in Southeastern Ontario. Your role is to help connect entrepreneurs with the right resources at the right time in their business journey.

Key points about your role:
- You provide guidance based on Switchboard's resource database
- You help identify appropriate resources based on business stage and needs
- You maintain a friendly, professional, and supportive tone
- You are concise and direct in your recommendations

Using only the following context to help the user:
{context}

Previous conversation:
{history}

Question: {question}

Provide a relevant response that:
1. Addresses the user's specific needs
2. References specific resources from the Switchboard database
3. Explains why these resources are relevant to their situation
4. Includes any relevant contact information or next steps
5. Offers to help narrow down or expand the search if needed
6. Provide links

Response should be concise, practical, and focus on actionable next steps.
"""

def process_query(query_text, chat_history=None):
    try:
        # Initialize OpenAI embeddings with explicit API key
        embedding_function = OpenAIEmbeddings(
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Initialize Chroma with embeddings
        db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embedding_function
        )
        
        # Perform similarity search
        results = db.similarity_search_with_relevance_scores(query_text, k=3)
        
        if not results:
            return {"error": "No relevant resources found in the Switchboard database"}, chat_history
        
        context = "\n".join([doc.page_content for doc, _ in results])
        prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        
        if chat_history:
            formatted_history = "\n".join([f"User: {q}\nAssistant: {r}" for q, r in chat_history[-3:]])
        else:
            formatted_history = ""
        
        # Initialize ChatOpenAI with explicit API key    
        chat = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        response = chat.predict(prompt.format(
            context=context,
            question=query_text,
            history=formatted_history
        ))
        
        updated_history = chat_history if chat_history else []
        updated_history.append((query_text, response))
        
        return {"response": response}, updated_history
        
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}, chat_history

def chat():
    chat_history = []
    print("Welcome to Switchboard! 👋 I'm here to help connect you with the right resources for your business journey. What type of support are you looking for?")
    
    while True:
        query_text = input("You: ")
        if query_text.lower() in ["exit", "quit", "bye"]:
            print("Thank you for using Switchboard. Visit www.myswitchboard.ca for more resources!")
            break

        result, chat_history = process_query(query_text, chat_history)

        if "error" in result:
           print(f"Assistant: {result['error']}")
        else:
           print("Assistant:", result["response"])

def main():
    parser = argparse.ArgumentParser(description="Switchboard Resource Assistant")
    parser.add_argument("--query", type=str, help="Direct text query for resource matching")
    args = parser.parse_args()

    if args.query:
        result, _ = process_query(args.query)
        print("\n" + "="*50)
        if "error" in result:
            print(f"\nError: {result['error']}")
        else:
            print("\nRecommended Resources:")
            print(result["response"])
        print("\n" + "="*50)
    else:
        chat()

if __name__ == "__main__":
    main()