#pip install langchain-groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

#https://console.groq.com/keys

class ModeloGroq:
    def __init__(self):
        load_dotenv()  # Cargar variables de entorno desde el archivo .env
        self.modelo = ChatGroq(model="openai/gpt-oss-20b", temperature=1.0)

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text