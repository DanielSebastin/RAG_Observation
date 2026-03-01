import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class Generator:

    def __init__(self,model="llama-3.1-8b-instant"):
        self.client=Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model=model

    def build_prompt(self,query,chunks):

        context="\n\n".join([c["text"] for c in chunks])

        prompt=f"""
You are a helpful assistant.
Answer the question ONLY using the provided context.
If the answer is not in the context, say "Not found in document."

Context:
{context}

Question:
{query}

Answer:
"""
        return prompt

    def generate(self,query,retrieved_chunks):

        prompt=self.build_prompt(query,retrieved_chunks)

        response=self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role":"user","content":prompt}
            ]
        )

        return response.choices[0].message.content