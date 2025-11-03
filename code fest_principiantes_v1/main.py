# Importamos todas las librerías que vamos a necesitar, más las páginas a utilizar
import flet as ft
from utils import resource_path  # 🔹 No olvides importar tu helper
from pagina.home import main_page
from pagina.instrucciones import instrucciones_page
from pagina.categorias import categorias_page
from pagina.facil import facil_page
from pagina.intermedio import intermedio_page
from pagina.dificil import dificil_page
from pagina.resolver import resolver_page

# --- Mapa de rutas ---
routes = {
    "/": main_page,
    "/instrucciones": instrucciones_page,
    "/categorias": categorias_page,
    "/facil": facil_page,
    "/intermedio": intermedio_page,
    "/dificil": dificil_page
}

# --- Controlador de cambio de ruta ---
def route_change(route_event: ft.RouteChangeEvent):
    page = route_event.page
    page.clean()

    current_page = routes.get(page.route, main_page)
    current_page(page)
    page.update()

# --- Función principal ---
def main(page: ft.Page):
    page.title = "Code Fest - 2025"
    page.window_icon = resource_path("icono/flag.ico")  # ✅ Aquí sí debe ir
    page.fonts = {"Gagalin": resource_path("fuente/Gagalin-Regular.otf")}
    page.bgcolor = "#65A84A"

    page.on_route_change = route_change
    page.on_view_pop = route_change
    page.go(page.route)  # Carga la primera ruta

# --- Ejecuta la app ---
ft.app(target=main, view=ft.AppView.FLET_APP)
