from rag.pdf_reader import PDFReader
from rag.chunker import TextChunker
from rag.vector_store import VectorStore

print("=" * 60)
print("READING PDF")
print("=" * 60)

reader = PDFReader()
text = reader.read_pdf("documents/L1.pdf")

print(f"Characters extracted: {len(text)}")

print()

print("=" * 60)
print("CHUNKING")
print("=" * 60)

chunker = TextChunker(chunk_size=500, overlap=100)
chunks = chunker.split_text(text)

print(f"Chunks created: {len(chunks)}")

print()

print("=" * 60)
print("CREATING VECTOR STORE")
print("=" * 60)

store = VectorStore()

print("Creating embeddings...")

store.create_embeddings(chunks)

print("Embeddings created successfully!")

print()

query = "What is resilience?"

print(f"Searching for: {query}")

results = store.search(query)

print()

for i, chunk in enumerate(results, start=1):
    print("=" * 60)
    print(f"Result {i}")
    print("=" * 60)
    print(chunk)