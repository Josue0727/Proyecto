import reflex as rx
from Proyecto.styles.styles import Size

def clave_page() -> rx.Component:
    return rx.box(
        rx.text("Esta es la página de la clave"),
        width="100%",
        padding=Size.big.value
    )

    app = rx.App()
    app.add_page(clave_page, title="Clave", state=ClaveState)
    app.run()

    