from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Cohere

from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = Cohere(model="command", max_tokens=256, temperature=0.75)
spell_check_prompt = PromptTemplate.from_template("""
    You are a spell checker that looks for mistakes in the user's provided text. 
    You take in all the user input and auto correct it. Just reply to user input with the correct spelling. 
    If the user input is spelled correctly, just reply "ok". Here's the user input: {text}
""")

grammar_check_prompt = PromptTemplate.from_template("""
    You are a grammar checker that looks for mistakes in the user's provided text. 
    You take in all the user input and auto correct it. Just reply to user input with the correct grammar. 
    If the user input is grammatically correct, just reply "ok". Here's the user input: {text}
""")


spell_check_chain = spell_check_prompt | model
grammar_check_chain = grammar_check_prompt | model

chat = ChatOpenAI(temperature=0)
system_template = (
    "You are a spell and grammar checker that looks for mistakes in the user's provided text."
)
system_message = SystemMessagePromptTemplate.from_template(template=system_template)
message_template = (
    "You take in all the user input and auto correct it. Just reply to user input with the correct spelling and grammar. If the user input is spelled and grammatically correct, just reply 'ok'. Here's the user input: {text}"
)
human_message = HumanMessagePromptTemplate.from_template(template=message_template)
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message, human_message])

def spell_and_grammar_check(text: str):
    return {
        "spell_and_grammar_check": chat(
            chat_prompt.format_prompt(text=text).to_messages()
        ).content,
        "spell_check": spell_check(text),
        "grammar_check": grammar_check(text)
    }


def grammar_check(text: str):
    return grammar_check_chain.invoke({"text": text})


def spell_check(text: str):
    return spell_check_chain.invoke({"text": text})
