import reflex as rx
from Proyecto.styles.styles import Size
from Proyecto.styles.colors import color, textcolor

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.image(
            src="LogoO.png",
            alt="Logo de ExoMaderas",
            width=Size.so_big.value,
            height=Size.so_big.value
        ),
        rx.text("           @EcoMaderas 2024"),
        rx.spacer(),
        rx.link(rx.button(" Clave", bg=color.secondary.value, color=textcolor.secondary.value, padding=Size.big.value, font_size=Size.default.value), href="/clave"),
        rx.link(rx.button(" Especies", bg=color.secondary.value, color=textcolor.secondary.value, padding=Size.big.value, font_size=Size.default.value), href="/especies"),
        rx.link(rx.button(" Definiciones", bg=color.secondary.value, color=textcolor.secondary.value, padding=Size.big.value, font_size=Size.default.value), href="/definiciones"),
        width="100%"
        ),
        bg=color.primary.value,
        position="sticky",
        border_bottom=f"0.25em solid {color.secondary.value}",
        padding_x=Size.big.value,
        padding_y=Size.big.value,
        z_indez="999",
        top="0",
        width="100%"
    )




