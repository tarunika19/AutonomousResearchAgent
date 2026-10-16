from google import genai
import os


class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(
            api_key=self.api_key
        )

    def has_api_key(self):
        return self.api_key is not None

    def chat(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text