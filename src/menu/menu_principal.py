from src.modelos.modelo_google import ModeloGoogle
from src.modelos.modelo_groq import ModeloGroq
from src.modelos.modelo_local import ModeloLocal
from src.modelos.prompt_01 import Prompt01
from src.modelos.prompt_02 import Prompt_02

import os
from rich.console import Console
from rich.markdown import Markdown

class MenuPrincipal:
    def __init__(self):
        self.console = Console()
        self.opcion = 0

    @staticmethod
    def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear")

    # Espera a que el usuario presione Enter
    @staticmethod
    def pausar():
        input("\nPresiona Enter para volver al menú...")

    def mostrar_menu(self):
        print("=== Menú Principal ===")
        print("1. Modelo Google API KEY")
        print("2. Modelo Groq API KEY")
        print("3. Modelo Local (Ollama)")
        print("4. Modelo OpenBMB")
        print("5. Prompt básico")
        print("6. Prompt avanzado")
        print("0. Salir")

    def ejecutar_opcion(self):
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            self.opcion = input("Seleccione una opción: ")

            if self.opcion == "1":
                modelo_google = ModeloGoogle()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_google.generar_respuesta(prompt)
                print("Respuesta del modelo Google:")
                self.console.print(Markdown(respuesta))  # Mostrar la respuesta en formato Markdown 

            elif self.opcion == "2":
                modelo_groq = ModeloGroq()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_groq.generar_respuesta(prompt)
                print("Respuesta del modelo Groq:")
                self.console.print(Markdown(respuesta))  # Mostrar la respuesta en formato Markdown

            elif self.opcion == "3":
                modelo_local = ModeloLocal()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_local.generar_respuesta(prompt)
                print("Respuesta del modelo Local:")
                self.console.print(Markdown(respuesta))  # Mostrar la respuesta en formato Markdown

            elif self.opcion == "4":
                from src.modelos.modelo_openbmb import ModeloOpenbmb
                modelo_openbmb = ModeloOpenbmb()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_openbmb.generar_respuesta(prompt)
                print("Respuesta del modelo OpenBMB:")
                self.console.print(Markdown(respuesta))  # Mostrar la respuesta en formato Markdown

            elif self.opcion == "5":
                prompt_01 = Prompt01()
                respuesta = prompt_01.generar_respuestas()
                print("Respuesta del Prompt básico:")
                self.console.print(Markdown(respuesta))  # Mostrar la respuesta en formato Markdown

            elif self.opcion == "6":
                prompt_02 = Prompt_02()
                respuesta = prompt_02.generar_respuestas()
                print("Respuesta del Prompt avanzado:")
                self.console.print(Markdown(respuesta))  # Mostrar la respuesta en formato Markdown

            elif self.opcion == "0":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

            self.pausar()# Pausa antes de volver al menú