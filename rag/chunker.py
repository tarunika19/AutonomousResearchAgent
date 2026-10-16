class TextChunker:
    """
    Splits large text into smaller overlapping chunks.
    """

    def __init__(self, chunk_size=500, overlap=100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(self, text):
        """
        Split text into overlapping chunks.
        """

        chunks = []

        start = 0

        while start < len(text):
            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks