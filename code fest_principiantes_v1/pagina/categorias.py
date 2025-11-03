import flet as ft
from utils import resource_path
from ejercicios import EJERCICIOS  # Importamos tu estructura completa


def categorias_page(page: ft.Page):
    page.clean()

    # --- Calcular puntos totales resueltos ---
    puntos_totales = 0
    for categoria, ejercicios in EJERCICIOS.items():
        for e in ejercicios:
            if e["estado"].lower() == "resuelto":
                puntos_totales += e["puntaje"]

    # --- Configuración general ---
    page.title = "Categorías - Code Fest 2025"
    page.bgcolor = "#BBD8EF"
    page.window_width = 900
    page.window_height = 600
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_icon = "icono/icono1.ico"

    # --- Fuente personalizada ---
    page.fonts = {"Gagalin": resource_path("fuente/Gagalin-Regular.otf")}

    # --- Texto de puntos totales ---
    puntos_texto = ft.Container(
    content=ft.Text(
        f"Total: {puntos_totales} pts",
        size=22,
        color="white",
        font_family="Gagalin",
        weight=ft.FontWeight.BOLD,
    ),
    bgcolor="#1E3A8A",  # Azul profundo elegante
    border_radius=12,
    padding=ft.padding.symmetric(horizontal=15, vertical=8),
    margin=ft.margin.only(left=20, top=5),
    shadow=ft.BoxShadow(
        blur_radius=6,
        color=ft.Colors.BLACK54,
        offset=ft.Offset(2, 2),
    ),
)


    # --- Título principal ---
    titulo = ft.Text(
        "CATEGORÍAS",
        size=45,
        font_family="Gagalin",
        weight=ft.FontWeight.BOLD,
        color="black",
        text_align=ft.TextAlign.CENTER
    )

    # --- Botones de categorías ---
    btn_facil = ft.ElevatedButton(
        text="FÁCIL",
        width=200,
        height=120,
        bgcolor="#FFCF3D",
        color="black",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            text_style=ft.TextStyle(
                font_family="Gagalin",
                size=22,
                weight=ft.FontWeight.BOLD
            )
        ),
        on_click=lambda e: page.go("/facil")
    )

    btn_intermedio = ft.ElevatedButton(
        text="INTERMEDIO",
        width=200,
        height=120,
        bgcolor="#FFCF3D",
        color="black",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            text_style=ft.TextStyle(
                font_family="Gagalin",
                size=22,
                weight=ft.FontWeight.BOLD
            )
        ),
        on_click=lambda e: page.go("/intermedio")
    )

    btn_dificil = ft.ElevatedButton(
        text="DIFÍCIL",
        width=200,
        height=120,
        bgcolor="#FFCF3D",
        color="black",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            text_style=ft.TextStyle(
                font_family="Gagalin",
                size=22,
                weight=ft.FontWeight.BOLD
            )
        ),
        on_click=lambda e: page.go("/dificil")
    )

    # --- Botón de regreso ---
    btn_volver = ft.IconButton(
        icon=ft.Icons.ARROW_BACK,
        icon_size=45,
        icon_color="black",
        on_click=lambda e: page.go("/")
    )

    # --- Distribución superior: volver + puntos ---
    header = ft.Row(
        [btn_volver, puntos_texto],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    # --- Distribución de botones ---
    botones_categorias = ft.Row(
        [btn_facil, btn_intermedio, btn_dificil],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    # --- Estructura final ---
    page.add(
        ft.Column(
            [
                header,
                titulo,
                botones_categorias
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40
        )
    )
