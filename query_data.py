import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Constants
PROMPT_TEMPLATE = """
You are SwitchboardBuddy, a chatbot designed to assist entrepreneurs by answering their questions and providing valuable resources. Respond conversationally and to the point.

---

Question: {question}

Answer:
"""

# Load the OpenAI API key from the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please add it to your .env file.")

def generate_response(question):
    """
    Generates a response using OpenAI's model based on the user's question.
    :param question: User's query.
    :return: The model's response.
    """
    try:
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(question=question)
        model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
        return model.predict(prompt)
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Unable to generate a response at this time."

def chatbot():
    """
    Interactive chatbot for SwitchboardBuddy.
    """
    print("Welcome to SwitchboardBuddy! 🌟 I'm here to help you connect with resources for your business.\n")

    while True:
        query = input("How can I assist you today? (Type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Goodbye! 👋")
            break

        response = generate_response(query)
        print(f"SwitchboardBuddy: {response}")

def main():
    """
    Main function to run the chatbot in interactive mode.
    """
    chatbot()

if __name__ == "__main__":
    main()
