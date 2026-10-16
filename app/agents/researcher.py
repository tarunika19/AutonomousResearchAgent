from app.gemini_client import GeminiClient


class ResearchAgent:

    def __init__(self):
        self.client = GeminiClient()

    def research(self, topic):

        prompt = f"""
You are an expert researcher.

Write a detailed technical explanation about

{topic}

Requirements

- Explain clearly
- Include examples
- Use bullet points where helpful
- Mention advantages
- Mention disadvantages
- Mention real-world applications

Return only the explanation.
"""

        return self.client.chat(prompt)