import reflex as rx
from Proyecto.styles.styles import Size

def clave_page() -> rx.Component:
    return rx.box(
        rx.text("Esta es la página de Clave"),
        width="100%",
        padding=Size.big.value
    )

def especies_page() -> rx.Component:
    return rx.box(
        rx.text("Esta es la página de Especies"),
        width="100%",
        padding=Size.big.value
    )

def definiciones_page() -> rx.Component:
    return rx.box(
        rx.text("Esta es la página de Definiciones"),
        width="100%",
        padding=Size.big.value
    )