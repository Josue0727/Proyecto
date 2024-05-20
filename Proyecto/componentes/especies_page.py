import reflex as rx
from Proyecto.styles.styles import Size

def especies_page() -> rx.Component:
    return rx.box(
        rx.text("Esta es la página de Especies"),
        width="100%",
        padding=Size.big.value
    )
