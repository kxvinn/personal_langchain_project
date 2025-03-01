import os
import re
import json

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

apikey = os.getenv("KEY")


mixtral = "mixtral-8x7b-32768"

#initalizing Groq client
chat = ChatGroq(model_name=mixtral, groq_api_key=apikey)

# system prompt
SYSTEM_PROMPT = """
Você é um assistente virtual inteligente e prestativo. Sua tarefa é fornecer respostas claras, concisas e úteis para as perguntas dos usuários. Siga estas diretrizes ao responder:

1. Seja contextual: Entenda o contexto da pergunta e forneça respostas relevantes.
2. Seja educado e amigável: Use um tom profissional, mas acessível.
3. Seja breve: Evite respostas longas e desnecessárias, a menos que o usuário peça mais detalhes.
4. Seja preciso: Se não souber a resposta, diga claramente que não sabe e ofereça ajuda em outro tópico.
5. Seja proativo: Antecipe possíveis dúvidas relacionadas e sugira informações adicionais quando apropriado.
"""


def get_groq_response(user_input):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),

        HumanMessage(content=user_input)
    ]


    response = chat(messages)

    return response.content
