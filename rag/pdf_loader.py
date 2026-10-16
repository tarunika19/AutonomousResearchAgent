import os
from pypdf import PdfReader


class PDFLoader:

    def load_documents(self, folder_path):

        documents = []

        for file in os.listdir(folder_path):

            if file.endswith(".pdf"):

                path = os.path.join(folder_path, file)

                reader = PdfReader(path)

                text = ""

                for page in reader.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

                documents.append(
                    {
                        "filename": file,
                        "text": text
                    }
                )

        return documents