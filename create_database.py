import argparse
import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Constants
DATA_FOLDER = "data"
EXCEL_FILE = "Switchboard Resources from Partners_August 2024.xlsx"
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def load_excel_as_dataframe():
    """
    Load the Excel file into a Pandas DataFrame.
    :return: A DataFrame containing the Excel data.
    """
    file_path = os.path.join(DATA_FOLDER, EXCEL_FILE)
    if not os.path.exists(file_path):
        print(f"Excel file '{EXCEL_FILE}' not found in '{DATA_FOLDER}'.")
        return pd.DataFrame()

    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return pd.DataFrame()

def search_dataframe(data, query):
    """
    Search the DataFrame for relevant rows based on the query.
    :param data: DataFrame containing the Excel data.
    :param query: User's query string.
    :return: Filtered DataFrame matching the query.
    """
    if data.empty:
        return pd.DataFrame()

    matches = data.apply(
        lambda row: query.lower() in " ".join(str(value).lower() for value in row if pd.notna(value)), axis=1
    )
    return data[matches]

def generate_response(context, question):
    """
    Generates a response using OpenAI's model based on the provided context and question.
    :param context: Contextual information retrieved from the database.
    :param question: User's query.
    :return: The model's response.
    """
    try:
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context, question=question)
        model = ChatOpenAI()
        return model.predict(prompt)
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Unable to generate a response at this time."

def chatbot():
    """
    Interactive chatbot for SwitchboardBuddy.
    """
    print("Welcome to SwitchboardBuddy! 🌟 I'm here to help you connect with resources for your business.\n")

    # Load Excel data
    data = load_excel_as_dataframe()
    if data.empty:
        print("No data found. Please ensure the Excel file is correctly placed in the 'data' folder.\n")
        return

    while True:
        query = input("How can I assist you today? (Type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Goodbye! 👋")
            break

        # Search the DataFrame for matching rows
        results = search_dataframe(data, query)
        if not results.empty:
            print("\nHere are some resources that match your query:")
            for _, row in results.iterrows():
                title = row.get("Title", "No Title")
                link = row.get("Button Link", "No Link")
                print(f"- **{title}**: [Learn more]({link})")
            continue

        # No match found
        print("\nNo matching resources found. Let me generate a helpful response.")
        response = generate_response("No relevant context found in the data.", query)
        print(f"Response: {response}")

def main():
    """
    Main function to handle CLI arguments and execute the chatbot logic.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, nargs="?", help="The query text.")
    args = parser.parse_args()

    if args.query_text:
        # Non-interactive mode
        data = load_excel_as_dataframe()
        if not data.empty:
            results = search_dataframe(data, args.query_text)
            if not results.empty:
                print("\nHere are some resources that match your query:")
                for _, row in results.iterrows():
                    title = row.get("Title", "No Title")
                    link = row.get("Button Link", "No Link")
                    print(f"- **{title}**: [Learn more]({link})")
                return

        # No match found, generate response
        response = generate_response("No relevant context found in the data.", args.query_text)
        print(f"Response: {response}")
    else:
        # Interactive mode
        chatbot()

if __name__ == "__main__":
    main()
