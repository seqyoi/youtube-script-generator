from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

# Prompt template
template = """
You are a YouTube script writer.

Create a compelling YouTube video script.

Topic: {topic}
Tone: {tone}
Duration: {duration} minutes

Structure:
- Hook (first 5 seconds)
- Introduction
- Main content (well structured)
- Conclusion with CTA

Make it engaging and natural.
"""

prompt = PromptTemplate(
    input_variables=["topic", "tone", "duration"],
    template=template,
)

def generate_script(topic, tone, duration):
    final_prompt = prompt.format(
        topic=topic,
        tone=tone,
        duration=duration
    )

    response = model.generate_content(final_prompt)
    return response.text