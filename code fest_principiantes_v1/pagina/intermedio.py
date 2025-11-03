import flet as ft
from ejercicios import EJERCICIOS
from pagina.resolver import resolver_page
from utils import resource_path

def intermedio_page(page: ft.Page):
    page.clean()
    page.title = "Intermedio - Code Fest 2025"
    page.bgcolor = "#FFCF3D"
    page.window_width = 900
    page.window_height = 600
    page.window_resizable = False
    page.window_icon = "icono/icono1.ico"
    page.fonts = {"Gagalin": resource_path("fuente/Gagalin-Regular.otf")}

    # ---- Título ----
    titulo = ft.Container(
        content=ft.Text(
            "Categoría: INTERMEDIO",
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

    ejercicios = EJERCICIOS["intermedio"]
    contenedores = []

    for ej in ejercicios:
        estado_actual = page.session.get(f"intermedio_{ej['id']}_estado")
        if estado_actual is None:
            estado_actual = ej["estado"]

        bloqueado = estado_actual in ["fallado", "logrado"]

        # ---- Colores según estado ----
        if estado_actual == "resuelto":
            cont_bgcolor = "#BDBDBD"  # gris
        elif estado_actual == "expirado":
            cont_bgcolor = "#E57373"  # rojo
        else:
            cont_bgcolor = "#65A84A"  # verde

        # ---- Contenido del contenedor ----
        columna_items = [
            ft.Text(ej["titulo"], font_family="Gagalin", size=22,
                    weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("Temas relacionados: "+ej["temas_relacionados"], font_family="Gagalin", size=18, color="black"),
            ft.Text(
                f"Duración: {ej['duracion']} minutos | Puntaje: {ej['puntaje']} puntos | Estado: {estado_actual}",
                font_family="Gagalin",
                size=16,
                color="black",
                italic=True
            )
        ]

        # ---- Botón ----
        if estado_actual not in ["resuelto", "expirado"]:
            columna_items.append(
                ft.ElevatedButton(
                    text="Abrir ejercicio",
                    bgcolor="#BBD8EF" if not bloqueado else "#BDBDBD",
                    color="black",
                    width=180,
                    disabled=bloqueado,
                    on_click=None if bloqueado else lambda e, ex=ej: resolver_page(page, "intermedio", ex["id"])
                )
            )

        # ---- Contenedor ----
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

    # ---- Botón volver ----
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
                    ft.Column(contenedores, spacing=15, alignment=ft.MainAxisAlignment.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25,
                scroll=ft.ScrollMode.AUTO
            ),
            expand=True
        )
    )
