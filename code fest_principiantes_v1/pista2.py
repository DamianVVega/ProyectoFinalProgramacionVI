import flet as ft
from ejercicios import EJERCICIOS

class BannerPista2(ft.Container):
    def __init__(self, categoria: str, index: int):
        super().__init__()
        self.bgcolor = "#FFE082"  # Amarillo más oscuro
        self.padding = 10
        self.border_radius = 8
        self.visible = False
        self.alignment = ft.alignment.center
        self.content = ft.Text("", size=16, weight="bold", color="black", text_align=ft.TextAlign.CENTER)

        self.categoria = categoria
        self.index = index
        self.cargar_pista()

    def cargar_pista(self):
        ejercicio = next((ej for ej in EJERCICIOS[self.categoria] if ej["id"] == self.index), None)
        if ejercicio and ejercicio.get("pista2", "").strip():
            self.content.value = ejercicio["pista2"].strip()
            self.visible = True
        else:
            self.visible = False

    def mostrar(self):
        self.visible = True
        self.update()

    def ocultar(self):
        self.visible = False
        self.update()
