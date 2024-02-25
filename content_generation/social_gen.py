from dotenv import load_dotenv

from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate

from langchain_openai import OpenAI
from langchain.pydantic_v1 import BaseModel, Field

load_dotenv()


class TweetsResponse(BaseModel):
    tweets: list[str] = Field(description="list of generated tweets")


class LinkedInPostsResponse(BaseModel):
    linkedin_posts: list[str] = Field(description="list of generated linkedin posts")


class SocialGenerator(object):
    system_template = (
        "You are an expert social media marketer who is tasked with generating social media content relevant to the "
        "user "
    )

    def __init__(self, title: str, body: str, ):
        self.model = OpenAI(temperature=0)
        self.body = body
        self.title = title

    def twitter(self):
        parser = JsonOutputParser(pydantic_object=TweetsResponse)
        message_template = (
            "Generate 10 marketing tweets based on the contents of this blog post's title and body.\n\n"
            "{format_instructions}\n\nThe title is {title} and the body is {body}"
        )
        prompt = PromptTemplate(
            template=message_template,
            input_variables=["title", "body"],
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        prompt_and_model = prompt | self.model
        output = prompt_and_model.invoke({
            "title": self.title,
            "body": self.body
        })
        twitter_parsed_message = []

        try:
            twitter_parsed_message = parser.invoke(output)
            print(twitter_parsed_message)
        except OutputParserException as e:
            print(str(e))

        return {
            "twitter": twitter_parsed_message
        }

    def linkedin(self):
        parser = JsonOutputParser(pydantic_object=LinkedInPostsResponse)
        message_template = (
            "Generate 10 LinkedIn Posts based on the contents of this blog post's title and body.\n\n"
            "{format_instructions}\n\nThe title is: {title} and the body is: {body}"
        )
        prompt = PromptTemplate(
            template=message_template,
            input_variables=["title", "body"],
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        prompt_and_model = prompt | self.model
        output = prompt_and_model.invoke({
            "title": self.title,
            "body": self.body
        })
        return {
            "linkedin": parser.invoke(output)
        }
