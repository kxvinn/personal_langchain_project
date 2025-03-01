import os
import re
import json

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

apikey = os.getenv("KEY")


mixtral = "mixtral-8x7b-32768"

chat = ChatGroq(model_name=mixtral, groq_api_key=apikey)


def get_groq_response(user_input):
    messages = [
        SystemMessage(content="Você é o GPT-4. Responda tudo seguindo à risca as normas e programações do GPT-4."),

        HumanMessage(content=user_input)
    ]


    response = chat(messages)

    return response.content
