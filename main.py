from typing import Union

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from content_generation.spell_and_grammar_check import spell_and_grammar_check
from content_generation.translate import translate_text
from content_generation.adjust_tone import adjust_tone_of_text
from content_generation.summarize import summarize_text
from content_generation.copywriter import CopyWriter
from content_generation.image_gen import generate_image
from content_generation.social_gen import SocialGenerator

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5000",
    "https://internal-ladybug-dear.ngrok-free.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Content(BaseModel):
    text: str


class TranslateContent(BaseModel):
    text: str
    target_language: str


class AdjustToneContent(BaseModel):
    text: str
    tone: str


class ImagePrompt(BaseModel):
    text: str


class SocialGenPrompt(BaseModel):
    title: str
    body: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# api
@app.post("/api/check")
def check(content: Content):
    return spell_and_grammar_check(content.text)


@app.post("/api/summarize")
def summarize(content: Content):
    return summarize_text(content.text)


@app.post("/api/translate")
def translate(translate_content: TranslateContent):
    return translate_text(translate_content.text,
                          translate_content.target_language)


@app.post("/api/adjust-tone")
def adjust_tone(adjust_tone_content: AdjustToneContent):
    return adjust_tone_of_text(adjust_tone_content.text, adjust_tone_content.tone)


@app.post("/api/completion")
def complete(content: Content):
    return CopyWriter(content.text).completion()


@app.post("/api/prompt")
def prompt(content: Content):
    return CopyWriter(content.text).prompt()


@app.post("/api/image-gen")
def image_generation(image_prompt: ImagePrompt):
    return generate_image(image_prompt.text)


@app.post("/api/generate-social")
def social_generation(content: SocialGenPrompt):
    social_gen = SocialGenerator(content.title, content.body)
    return social_gen.twitter()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
