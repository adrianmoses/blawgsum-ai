"""
Copywriter Agent to provide text completion and full content generation based on RAG
"""
import os
from dotenv import load_dotenv

from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain_openai import ChatOpenAI

load_dotenv()


class CopyWriter(object):

    def __init__(self, text):
        self.chat = ChatOpenAI(temperature=0)
        system_template = (
            "You are an expert copywriter who is tasked with generating and completing text"
        )
        self.system_message = SystemMessagePromptTemplate.from_template(template=system_template)
        self.text = text

    def completion(self):
        message_template = (
            "{text}"
        )
        human_message = HumanMessagePromptTemplate.from_template(template=message_template)

        chat_prompt = ChatPromptTemplate.from_messages([self.system_message, human_message])
        return {
            "completion": self.chat(
                chat_prompt.format_prompt(text=self.text).to_messages()
            ).content
        }

    def prompt(self):
        message_template = (
            "{text}"
        )
        human_message = HumanMessagePromptTemplate.from_template(template=message_template)

        chat_prompt = ChatPromptTemplate.from_messages([self.system_message, human_message])
        return {
            "prompt": self.chat(
                chat_prompt.format_prompt(text=self.text).to_messages()
            ).content
        }
