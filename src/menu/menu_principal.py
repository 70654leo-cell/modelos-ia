from src.modelos.modelo_google import ModeloGoogle
from src.modelos.modelo_groq import ModeloGroq
from src.modelos.modelo_local import ModeloLocal

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

            elif self.opcion == "0":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

            self.pausar()# Pausa antes de volver al menú