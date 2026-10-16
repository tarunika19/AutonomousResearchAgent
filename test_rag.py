import os
from dotenv import load_dotenv

from rag.rag_pipeline import RAGPipeline

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

rag = RAGPipeline(api_key)

while True:

    question = input("\nAsk a question (type exit to quit): ")

    if question.lower() in ["exit", "quit", "q","e"]:
        break

    answer = rag.ask(question)

    print("\n")
    print("=" * 70)
    print(answer)
    print("=" * 70)