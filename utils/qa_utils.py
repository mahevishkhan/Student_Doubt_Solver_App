from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_answer_from_context(question, context):
    prompt = f"""
You are an educational assistant. You are given combined content from a video and a PDF.

Only answer if the content needed to answer the question is present in the given context.
If not, respond: "❌ The answer to your question is not present in the provided video or PDF."

Context:
{context}

Question: {question}
Answer:
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful educational assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()
