from rag.pdf_reader import PDFReader
from rag.chunker import TextChunker

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

chunker = TextChunker(
    chunk_size=500,
    overlap=100
)

chunks = chunker.split_text(text)

print(f"Total Chunks: {len(chunks)}")

print()

print("=" * 60)
print("FIRST CHUNK")
print("=" * 60)

print(chunks[0])

print()

print("=" * 60)
print("SECOND CHUNK")
print("=" * 60)

print(chunks[1])