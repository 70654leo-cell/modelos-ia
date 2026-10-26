import os
from dotenv import load_dotenv
from llama_cpp import Llama

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class ModeloOpenbmb:
    def __init__(self):
        # Obtener la ruta del archivo .env
        model_path = os.getenv("OPENBMB_KEY")
        
        self.modelo = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4,
            verbose=False
        )

    def generar_respuesta(self, prompt):
        output = self.modelo(
            prompt,
            max_tokens=512,
            stop=["Q:"],
            echo=False
        )
        return output['choices'][0]['text']