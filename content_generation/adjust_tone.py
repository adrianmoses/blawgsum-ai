from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


chat = ChatOpenAI(temperature=0)
system_template = (
    "You are an expert copywriter who is tasked with adjusting the tone of the user's provided text."
)
system_message = SystemMessagePromptTemplate.from_template(template=system_template)


def adjust_tone_of_text(text: str, tone: str):
    message_template = (
        "Adjust the following text to have a {tone} tone: {text}"
    )
    human_message = HumanMessagePromptTemplate.from_template(template=message_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
    return {
        "adjusted_tone": chat(
            chat_prompt.format_prompt(text=text, tone=tone).to_messages()
        ).content
    }
