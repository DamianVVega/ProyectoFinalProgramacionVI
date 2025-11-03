import flet as ft
from pagina.resolver import resolver_page
from ejercicios import EJERCICIOS
from utils import resource_path


def facil_page(page: ft.Page):
    page.clean()
    page.title = "Fácil - Code Fest 2025"
    page.bgcolor = "#FFCF3D"
    page.window_width = 900
    page.window_height = 600
    page.window_resizable = False
    page.window_icon = "icono/icono1.ico"
    page.fonts = {"Gagalin": resource_path("fuente/Gagalin-Regular.otf")}

    # ---- Título principal ----
    titulo = ft.Container(
        content=ft.Text(
            "Categoría: FÁCIL",
            size=38,
            font_family="Gagalin",
            text_align=ft.TextAlign.CENTER,
            color="black",
        ),
        bgcolor="#BBD8EF",
        padding=15,
        border_radius=12,
        width=600
    )

    ejercicios = EJERCICIOS["facil"]
    contenedores = []

    for ej in ejercicios:
        # Obtener el estado actual desde la sesión (si existe)
        estado_actual = page.session.get(f"facil_{ej['id']}_estado")
        if estado_actual is None:
            estado_actual = ej["estado"]

        # Determinar si está bloqueado
        bloqueado = estado_actual in ["fallado", "logrado"]

        # ---- Color según estado ----
        if estado_actual == "resuelto":
            cont_bgcolor = "#BDBDBD"  # gris
        elif estado_actual == "expirado":
            cont_bgcolor = "#E57373"  # rojo
        else:
            cont_bgcolor = "#65A84A"  # verde (por defecto)

        # ---- Contenido del contenedor ----
        columna_items = [
            ft.Text(
                ej["titulo"],
                font_family="Gagalin",
                size=22,
                weight=ft.FontWeight.BOLD,
                color="black"
            ),
            ft.Text(
                "Temas relacionados: "+ej["temas_relacionados"],
                font_family="Gagalin",
                size=18,
                color="black"
            ),
            ft.Text(
                f"Duración: {ej['duracion']} minutos | Puntaje: {ej['puntaje']} puntos | Estado: {estado_actual}",
                font_family="Gagalin",
                size=16,
                color="black",
                italic=True
            )
        ]

        # ---- Botón de apertura ----
        # Se oculta si el ejercicio está resuelto o expirado
        if estado_actual not in ["resuelto", "expirado"]:
            columna_items.append(
                ft.ElevatedButton(
                    text="Abrir ejercicio",
                    bgcolor="#BBD8EF" if not bloqueado else "#BDBDBD",
                    color="black",
                    width=180,
                    disabled=bloqueado,
                    on_click=None if bloqueado else lambda e, ex=ej: resolver_page(page, "facil", ex["id"])
                )
            )

        # ---- Crear el contenedor del ejercicio ----
        contenedores.append(
            ft.Container(
                content=ft.Column(
                    columna_items,
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                bgcolor=cont_bgcolor,
                border_radius=15,
                padding=20,
                width=600,
                shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.BLACK45, offset=ft.Offset(2, 2))
            )
        )

    # ---- Botón para volver ----
    btn_volver = ft.IconButton(
        icon=ft.Icons.ARROW_BACK,
        icon_color="black",
        icon_size=45,
        on_click=lambda e: page.go("/categorias")
    )

    # ---- Estructura principal ----
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Row([btn_volver], alignment=ft.MainAxisAlignment.START),
                    titulo,
                    ft.Column(
                        contenedores,
                        spacing=15,
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25,
                scroll=ft.ScrollMode.AUTO
            ),
            expand=True
        )
    )
