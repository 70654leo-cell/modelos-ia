from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI

class ModeloGoogle:
    def __init__(self):
        load_dotenv()  # Cargar variables de entorno desde el archivo .env
        self.modelo = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.content