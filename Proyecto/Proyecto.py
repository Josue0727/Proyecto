import reflex as rx
import Proyecto.styles.styles as styles
from Proyecto.styles.styles import Size
from Proyecto.views.navbar import navbar
from Proyecto.views.header import header

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                sidth="100%"
            )
        )
    )


app = rx.App(
    stylesheets=styles.stylesheets,
    styles=styles.base_style
)

app.add_page(
    index,
    title="EcoMaderas",
    description="Interfaz inicial de EcoMaderas, aquí podrás encontrar una appa web interactiva que te permitirá identificar maderas"
)

app._compile()

