import flet as ft # Importamos el modulo principal
from utils import resource_path

def main_page(page: ft.Page): # Definimos la funcion principal
    page.clean()

    page.title = "Code Fest - 2025"
    page.window_full_screen = True

    page.window_width = 900 #Ancho de la pantalla
    page.window_height = 600 #Largo de la pantalla
    page.window_resizable = False
    page.bgcolor = "#65A84A" # Color de fondo
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    


    page.fonts = {"Gagalin": resource_path("fuente/Gagalin-Regular.otf")}
    #Titulo Principal
    titulo = ft.Text( #Se define del tipo flet
        "CODE FEST - 2025.\nSISTEMA DE CONTROL DE EJERCICIOS. PRINCIPIANTES",
        size=40, #Tamaño Fuente
        font_family="Gagalin", #Fuente externa
        color="black", #Color de texto
        text_align=ft.TextAlign.CENTER
    )

    tarjeta = ft.Container( #Contenedor principal, adentro estará el titulo
        content=ft.Column(
            [titulo],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=600,
        height=250,
        bgcolor="white",
        border_radius=15,
        padding=20,
        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.BLACK26)
    )

    # --- Botones principales ---
    btn_empezar = ft.ElevatedButton(
        text="Empezar",
        bgcolor="#FFCF3D",
        color="black",
        width=200,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD, font_family="Gagalin")
        ),
        on_click=lambda e: page.go("/categorias")  # 🔹 Redirige a la página de categorías
    )

    btn_instrucciones = ft.ElevatedButton(
        text="Instrucciones",
        bgcolor="#BBD8EF",
        color="black",
        width=200,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD, font_family="Gagalin")
        ),
        on_click=lambda e: page.go("/instrucciones")
    )

    botones = ft.Row(
        controls=[btn_empezar, btn_instrucciones],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=40
    )

    page.add(
        ft.Column(
            controls=[tarjeta, botones],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40
        )
    )
