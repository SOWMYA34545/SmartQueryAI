
import os
from dotenv import load_dotenv
from google import genai
from ddgs import DDGS

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing from the .env file."
    )

client = genai.Client(api_key=api_key)


def search_web(question):
    with DDGS() as ddgs:
        results = list(
            ddgs.text(
                query=question,
                region="in-en",
                safesearch="moderate",
                max_results=8
            )
        )

    return results


def ask_question(question):
    results = search_web(question)

    if not results:
        return "No web search results were found."

    web_context = ""

    for i, result in enumerate(results, start=1):
        web_context += (
            f"\nSOURCE {i}\n"
            f"TITLE: {result.get('title', '')}\n"
            f"URL: {result.get('href', '')}\n"
            f"CONTENT: {result.get('body', '')}\n"
            "-----------------------------\n"
        )

    prompt = f"""
You are a web question-answering assistant.

Answer the user's question using ONLY the web search
results provided below.

USER QUESTION:
{question}

WEB SEARCH RESULTS:
{web_context}

RULES:
1. Give the direct answer first.
2. Use the search results as evidence.
3. Do not invent information.
4. At the end, list useful sources with their URLs.
5. If the answer is not found in the search results, respond with:
"Sorry, I could not find an answer to your question in the provided web search results."


Answer:
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text or "No answer was generated."