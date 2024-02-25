from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain_openai import ChatOpenAI
from langchain.schema import Document
from langchain_community.document_transformers import GoogleTranslateTransformer

import os
from dotenv import load_dotenv

load_dotenv()

def convert_language_to_code(language: str):
    language_codes = {
        "english": "en",
        "spanish": "es",
        "french": "fr",
        "german": "de",
        "italian": "it",
        "portuguese": "pt",
        "dutch": "nl",
        "russian": "ru",
        "japanese": "ja",
        "chinese": "zh",
        "korean": "ko",
        "arabic": "ar",
        "turkish": "tr",
        "hindi": "hi",
        "indonesian": "id",
        "vietnamese": "vi",
        "thai": "th",
        "greek": "el",
        "hebrew": "he",
        "swedish": "sv",
        "danish": "da",
        "norwegian": "no",
        "finnish": "fi",
        "czech": "cs",
        "polish": "pl",
        "hungarian": "hu",
        "romanian": "ro",
        "ukrainian": "uk",
        "catalan": "ca",
        "vietnamese": "vi",
        "tagalog": "tl",
        "malay": "ms",
        "swahili": "sw",
        "afrikaans": "af",
        "esperanto": "eo",
        "latin": "la",
        "welsh": "cy",
        "scots gaelic": "gd",
        "irish": "ga",
        "icelandic": "is",
        "farsi": "fa",
        "serbian": "sr",
        "croatian": "hr",
        "bosnian": "bs",
        "slovak": "sk",
        "slovenian": "sl",
        "estonian": "et",
        "latvian": "lv",
        "lithuanian": "lt",
        "maltese": "mt",
        "albanian": "sq",
        "macedonian": "mk",
        "kurdish": "ku",
        "armenian": "hy",
        "georgian": "ka",
        "basque": "eu",
        "galician": "gl",
        "catalan": "ca",
        "corsican": "co",
    }
    return language_codes.get(language.lower(), "en")


def translate_text(text: str, target_language: str):
    documents = [Document(page_content=text)]
    translator = GoogleTranslateTransformer(project_id=os.environ["GOOGLE_CLOUD_PROJECT_ID"])
    docs = translator.transform_documents(documents, target_language_code=convert_language_to_code(target_language))
    return {
        "translate": next((doc.page_content for doc in docs if doc.page_content), "No translation available")
    }

