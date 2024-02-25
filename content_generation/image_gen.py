from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def generate_image(text: str):
    # 1024x1024, 1024x1792 or 1792x1024
    response = client.images.generate(
        model="dall-e-3",
        prompt=text,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    return {
        "generated_image": image_url
    }
