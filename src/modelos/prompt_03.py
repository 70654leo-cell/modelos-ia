from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


class Prompt_03:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)

    def generar_respuestas(self):
        prompt_template = ChatPromptTemplate.from_messages([
            (
                "system",
                """
Eres un profesor universitario de programación.

Instrucciones:
- Responde siempre en español.
- Utiliza lenguaje sencillo.
- Explica los conceptos paso a paso.
- Incluye un ejemplo en Python.
- No utilices tecnicismos innecesarios.
"""
            ),
            (
                "user",
                "Explica qué es un bucle for en Python."
            )
        ])

        prompt = prompt_template.format_messages()
        respuesta = self.modelo.invoke(prompt)
        
        return respuesta.content