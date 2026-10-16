import rag.pdf_reader as pdf_reader
import os

print("Current working directory:", os.getcwd())

pdf_path = "documents/L1.pdf"

print("PDF path:", pdf_path)
print("PDF exists:", os.path.exists(pdf_path))

reader = pdf_reader.PDFReader()

text = reader.read_pdf(pdf_path)

print("Length of extracted text:", len(text))

print("=" * 60)
print(text[:1000])
print("=" * 60)