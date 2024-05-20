import reflex as rx
import Proyecto.styles.styles as styles
from Proyecto.views.navbar import navbar
from Proyecto.views.header import header
from Proyecto.componentes.clave_page import clave_page

def index_content() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            width="100%"
        )
    )

def clave_page_content() -> rx.Component:
    return rx.center(
        clave_page()
    )

def page_with_navbar(content: rx.Component) -> rx.Component:
    return rx.box(
        navbar(),
        content
    )

app = rx.App(
    stylesheets=styles.stylesheets,
    styles=styles.base_style
)


app.add_page(
    page_with_navbar(index_content()),  
    title="EcoMaderas",
    description="Interfaz inicial de EcoMaderas, aquí podrás encontrar una app web interactiva que te permitirá identificar maderas",
    route="/"
)

app.add_page(
    page_with_navbar(clave_page_content()),  
    title="Clave",
    description="Página de Clave",
    route="/clave"  
)

app._compile()

