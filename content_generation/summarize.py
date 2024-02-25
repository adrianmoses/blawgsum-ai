import cohere

import os
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))


def summarize_text(text: str):
    return {
        "summary": co.summarize(text)
    }
