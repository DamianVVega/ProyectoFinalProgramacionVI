import flet as ft
import asyncio
from utils import resource_path
from ejercicios import EJERCICIOS
from pista1 import BannerPista1
from pista2 import BannerPista2


def resolver_page(page: ft.Page, categoria: str, index: int):
    page.clean()
    page.title = "Resolver Ejercicio"
    page.bgcolor = "#65A84A"
    page.window_width = 900
    page.window_height = 600
    page.window_resizable = False
    page.window_icon = "icono/icono1.ico"
    page.fonts = {"Gagalin": resource_path("fuente/Gagalin-Regular.otf")}

    # Buscar ejercicio
    ejercicio = next((ej for ej in EJERCICIOS[categoria] if ej["id"] == index), None)
    if not ejercicio:
        page.add(ft.Text("Ejercicio no encontrado", size=24, color="red"))
        return

    # Variables
    tiempo_restante = ejercicio["duracion"] * 60
    pausado = False
    intentos_fallidos = 0
    codigo_ayudante = ejercicio.get("codigo", "")

    # 🔹 Variables de control de pistas
    pista1_usada = False
    pista2_usada = False

    # 🔹 Texto de puntaje con diseño mejorado
    puntos_texto = ft.Container(
        content=ft.Text(
            f"Puntos a reclamar: {ejercicio['puntaje']}",
            size=22,
            color="white",
            font_family="Gagalin",
            weight=ft.FontWeight.BOLD,
        ),
        bgcolor="#1E3A8A",
        border_radius=12,
        padding=ft.padding.symmetric(horizontal=15, vertical=8),
        margin=ft.margin.only(left=20, top=5),
        shadow=ft.BoxShadow(
            blur_radius=6,
            color=ft.Colors.BLACK54,
            offset=ft.Offset(2, 2),
        ),
    )

    # Contenido de pistas
    texto_pista1 = BannerPista1(categoria, index)
    texto_pista2 = BannerPista2(categoria, index)

    def cerrar_pista(contenedor):
        contenedor.visible = False
        page.update()

    cont_pista1 = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("💡 Pista 1", weight=ft.FontWeight.BOLD, size=22, color="#000000"),
                        ft.ElevatedButton("Cerrar", bgcolor="#E53935", color="white",
                                          on_click=lambda e: cerrar_pista(cont_pista1))
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(height=2, color="#FBC02D"),
                texto_pista1
            ],
            spacing=10
        ),
        bgcolor="#FFF9C4",
        padding=15,
        border_radius=12,
        shadow=ft.BoxShadow(color="#BDBDBD", blur_radius=5, offset=ft.Offset(2, 2)),
        visible=False,
    )

    cont_pista2 = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("💡 Pista 2", weight=ft.FontWeight.BOLD, size=22),
                        ft.ElevatedButton("Cerrar", bgcolor="#E53935", color="white",
                                          on_click=lambda e: cerrar_pista(cont_pista2))
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(height=2, color="#FFB74D"),
                texto_pista2
            ],
            spacing=10
        ),
        bgcolor="#FFE0B2",
        padding=15,
        border_radius=12,
        shadow=ft.BoxShadow(color="#BDBDBD", blur_radius=5, offset=ft.Offset(2, 2)),
        visible=False,
    )

    # Penalizaciones
    def aplicar_penalizacion(pista_num):
        nonlocal pista1_usada, pista2_usada
        if categoria == "facil":
            penalizaciones = {1: 2, 2: 3}
        elif categoria == "intermedio":
            penalizaciones = {1: 5, 2: 5}
        elif categoria == "dificil":
            penalizaciones = {1: 5, 2: 10}
        else:
            penalizaciones = {1: 0, 2: 0}

        if pista_num == 1 and not pista1_usada:
            ejercicio["puntaje"] -= penalizaciones[1]
            pista1_usada = True
        elif pista_num == 2 and not pista2_usada:
            ejercicio["puntaje"] -= penalizaciones[2]
            pista2_usada = True

        if ejercicio["puntaje"] < 0:
            ejercicio["puntaje"] = 0
        puntos_texto.content.value = f"Puntos a reclamar: {ejercicio['puntaje']}"
        page.update()

    def mostrar_pista1(e):
        aplicar_penalizacion(1)
        cont_pista1.visible = True
        cont_pista2.visible = False
        page.update()

    def mostrar_pista2(e):
        aplicar_penalizacion(2)
        cont_pista2.visible = True
        cont_pista1.visible = False
        page.update()

    # ----- Elementos visuales -----
    titulo = ft.Text(
        f"Ejercicio {ejercicio['id']} - {ejercicio['titulo']}",
        size=40,
        font_family="Gagalin",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color="black",
    )

    # descripcion = ft.Text(
    #     ejercicio["descripcion"],
    #     size=20,
    
    
    #     text_align=ft.TextAlign.CENTER,
    #     color="black",
    # )

    tiempo_texto = ft.Text("Temporizador", size=18, font_family="Gagalin", color="black")
    contador_texto = ft.Text("00 : 00", size=32, font_family="Gagalin", color="black")
    mensaje = ft.Text("", size=18, font_family="Gagalin", color="black")

    codigo_input = ft.TextField(
    label="Código de validación (6 dígitos)",
    width=300,
    text_align=ft.TextAlign.CENTER,
    keyboard_type=ft.KeyboardType.NUMBER,
    password=True,  # 🔒 ocultar caracteres
)

    codigo_pausa_input = ft.TextField(
    label="Código pausa",
    width=160,
    text_align=ft.TextAlign.CENTER,
    keyboard_type=ft.KeyboardType.NUMBER,
    password=True,  # 🔒 ocultar caracteres
)


    # Temporizador
    async def contador():
        nonlocal tiempo_restante
        while tiempo_restante > 0:
            if not pausado:
                minutos = tiempo_restante // 60
                segundos = tiempo_restante % 60
                contador_texto.value = f"{minutos:02d} : {segundos:02d}"
                page.update()
                await asyncio.sleep(1)
                tiempo_restante -= 1
            else:
                await asyncio.sleep(0.5)
        ejercicio["estado"] = "expirado"
        mensaje.value = "⏰ Tiempo agotado. El ejercicio ha expirado."
        mensaje.color = "red"
        page.update()
        await asyncio.sleep(1.2)
        page.go("/categorias")

    page.run_task(contador)

    def validar_codigo(e):
        nonlocal intentos_fallidos
        if codigo_input.value.strip() == codigo_ayudante and codigo_ayudante != "":
            ejercicio["estado"] = "resuelto"
            mensaje.value = "✅ Código correcto. Ejercicio validado."
            mensaje.color = "green"
            page.update()
            page.go("/categorias")
        else:
            intentos_fallidos += 1
            mensaje.value = f"❌ Código incorrecto. Intento {intentos_fallidos}/3."
            mensaje.color = "red"
            codigo_input.value = ""
            page.update()
            if intentos_fallidos >= 3:
                ejercicio["estado"] = "expirado"
                mensaje.value = "❌ Demasiados intentos fallidos. Ejercicio invalidado."
                mensaje.color = "red"
                page.update()
                page.go("/categorias")

    def pausar_reanudar(e):
        nonlocal pausado
        cod = codigo_pausa_input.value.strip()
        if cod == codigo_ayudante and codigo_ayudante != "":
            pausado = not pausado
            if pausado:
                mensaje.value = "⏸️ Temporizador pausado."
                btn_pausa.text = "Reanudar"
                btn_pausa.bgcolor = "#4CAF50"
            else:
                mensaje.value = "▶️ Temporizador reanudado."
                btn_pausa.text = "Pausar"
                btn_pausa.bgcolor = "#E53935"
            mensaje.color = "blue"
        else:
            mensaje.value = "❌ Código de pausa incorrecto."
            mensaje.color = "red"
        codigo_pausa_input.value = ""
        page.update()

    def salir_del_ejercicio(e):
        ejercicio["estado"] = "expirado"
        mensaje.value = "🚪 Has salido del ejercicio. Se ha marcado como expirado."
        mensaje.color = "red"
        page.update()
        page.go("/categorias")

    # Botón para copiar la descripción
    def copiar_descripcion(e):
        page.set_clipboard(ejercicio["descripcion"])
        mensaje.value = "📋 Descripción copiada al portapapeles."
        mensaje.color = "black"
        page.update()

    btn_validar = ft.ElevatedButton("Confirmar código", bgcolor="#FFCF3D", color="black",
                                    width=220, height=55, on_click=validar_codigo)
    btn_pausa = ft.ElevatedButton("Pausar", bgcolor="#E53935", color="white",
                                  width=120, height=45, on_click=pausar_reanudar)
    btn_salir = ft.ElevatedButton("Salir del ejercicio", bgcolor="#C62828", color="white",
                                  width=180, height=45, on_click=salir_del_ejercicio)
    btn_pista1 = ft.ElevatedButton("Mostrar Pista 1", bgcolor="#FFF176", color="black",
                                   width=160, height=40, on_click=mostrar_pista1)
    btn_pista2 = ft.ElevatedButton("Mostrar Pista 2", bgcolor="#FFD54F", color="black",
                                   width=160, height=40, on_click=mostrar_pista2)
    btn_copiar_descripcion = ft.ElevatedButton("Copiar descripción", bgcolor="#4CAF50",
                                               color="white", width=180, height=45,
                                               on_click=copiar_descripcion)

    # --- Contenido principal sin scroll ---
    contenido_container = ft.Container(
        content=ft.Column(
            [
                puntos_texto,
                cont_pista1,
                cont_pista2,
                titulo,
                #descripcion,
                ft.Row([btn_pista1, btn_pista2, btn_copiar_descripcion],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                ft.Row([tiempo_texto, contador_texto], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([codigo_input, btn_validar], alignment=ft.MainAxisAlignment.CENTER),
                mensaje,
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor="#65A84A",
        padding=ft.padding.all(20),
    )

    # --- Barra inferior con el mismo fondo ---
    barra_inferior = ft.Container(
        bgcolor="#65A84A",
        padding=ft.padding.symmetric(horizontal=20, vertical=15),
        content=ft.Row(
            [
                btn_salir,
                ft.Row([codigo_pausa_input, btn_pausa], alignment=ft.MainAxisAlignment.END),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # --- Layout principal ---
    layout = ft.Column(
        [
            contenido_container,
            barra_inferior,
        ],
        expand=True,
        spacing=0,
    )

    page.add(layout)
