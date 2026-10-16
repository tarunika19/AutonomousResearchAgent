from rag.vector_store import VectorStore
from rag.chunker import TextChunker
from rag.pdf_reader import PDFReader
from google import genai


class RAGPipeline:

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

        import os

        reader = PDFReader()
        chunker = TextChunker(chunk_size=500, overlap=100)

        all_chunks = []

        for filename in os.listdir("documents"):

            if filename.endswith(".pdf"):

                pdf_path = os.path.join("documents", filename)

                print(f"Reading {filename}")

                text = reader.read_pdf(pdf_path)

                chunks = chunker.split_text(text)

                all_chunks.extend(chunks)

        print(f"\nTotal chunks: {len(all_chunks)}")

        self.vector_store = VectorStore()
        self.vector_store.create_embeddings(all_chunks)
        self.vector_store.save()
    def ask(self, question):

        retrieved_chunks = self.vector_store.search(question, k=3)

        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
You are an expert teaching assistant.

Answer ONLY using the context below.

If the answer is not found in the context, say:

"I cannot find this information in the lecture notes."

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text