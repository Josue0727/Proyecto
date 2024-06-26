import reflex as rx
from Proyecto.styles.styles import Size

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Bienvenidos a EcoMaderas, su app de confianza :3",
            size="4",
            padding_bottom=Size.default.value
        ),
        rx.flex(
            rx.link(

                rx.image(
                    src="Grupo.jpeg",
                    alt="Grupooo",
                    width="14em",
                    height="14em"
                        ),
                href="/home",  
            ),
            rx.vstack(
                rx.text(
                    "Bienvenidos a EcoMaderas, herramienta de identificación de maderas del río Carare - Minero, la belleza Santander Colombia"
                ),
                rx.text(
                    "uwu"
                    
                )
            )
        )
    )

