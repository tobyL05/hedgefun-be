import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

class Agent():
    
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def generate_prompt(self, **kwargs):
        pass

    def query(self,prompt):
        return str(self.model.generate_content(prompt).text)