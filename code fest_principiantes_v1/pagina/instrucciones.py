import flet as ft
from utils import resource_path

def instrucciones_page(page: ft.Page):
    page.clean()

    page.title = "Instrucciones - Code Fest 2025"
    page.bgcolor = "#BBD8EF"
    page.window_width = 900
    page.window_height = 600
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_icon = "icono/icono1.ico"

    # Fuente personalizada
    page.fonts = {"Gagalin": resource_path("fuente/Gagalin-Regular.otf")}

    titulo = ft.Text(
        "Instrucciones",
        size=40,
        font_family="Gagalin",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color="black"
    )

    instrucciones = ft.Column(
        [
            ft.Text(
                "Bienvenido al torneo de programación organizado por el Club de Informática de Uninorte!",
                font_family="Gagalin",
                size=18,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            ),
            ft.Text(
                "Reglas y recomendaciones.",
                size=20,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            ),
            ft.Text(
                "Queda prohibido el uso de celulares durante el torneo, así como el uso de Inteligencia Artificial.",
                size=18,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            ),
            ft.Text(
                "Tiene un máximo de dos horas para resolver la mayor cantidad de ejercicios posible. El resultado se basa en los puntos acumulados.",
                size=18,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            ),
            ft.Text(
                "Cuando termine un ejercicio, solicite revisión por parte de un ayudante para validarlo.",
                size=18,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            ),
            ft.Text(
                "Mantenga el programa abierto para no perder el progreso.",
                size=18,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            ),
            ft.Text(
                "Se permite cualquier lenguaje de programación para la resolución.",
                size=18,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            ),
            ft.Text(
                "Puede comenzar con cualquier ejercicio, sin importar la categoría.",
                size=18,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            ),
            ft.Text(
                "Advertencia: Al ingresar al ejercicio, se iniciara un temporizador regresivo, el tiempo que puede durar el ejercicio estará en su vista previa.",
                size=18,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            ),
            ft.Text(
                "Se les proporciona el uso de pistas, cada pista descuenta determinados puntos de la totalidad del ejercicio.",
                size=18,
                text_align=ft.TextAlign.LEFT,
                 color="black"
            )
        ],
        spacing=12
    )

    btn_volver = ft.ElevatedButton(
        text="Volver",
        width=150,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            text_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD, font_family="Gagalin")
        ),
        on_click=lambda e: page.go("/")
    )

    page.add(
        ft.Column(
            controls=[titulo, instrucciones, btn_volver],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
