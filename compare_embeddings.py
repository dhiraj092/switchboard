from langchain_openai import OpenAIEmbeddings
from langchain.evaluation import load_evaluator
from dotenv import load_dotenv
import openai
import os

load_dotenv()

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    embedding_function = OpenAIEmbeddings(openai_api_key=api_key)
    
    vector = embedding_function.embed_query("design")
    print(f"Vector for 'design': {vector}")
    print(f"Vector length: {len(vector)}")

    evaluator = load_evaluator("pairwise_embedding_distance")
    words = ("Business_Stages", "Idea")
    result = evaluator.evaluate_string_pairs(prediction=words[0], prediction_b=words[1])
    print(f"Comparing ({words[0]}, {words[1]}): {result}")

if __name__ == "__main__":
    print("Starting main...")
    main()
    print("Script completed!")