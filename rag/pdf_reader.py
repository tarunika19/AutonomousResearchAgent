from pypdf import PdfReader


class PDFReader:

    def read_pdf(self, pdf_path):
        """
        Reads a single PDF and returns its text.
        """

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text