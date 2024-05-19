import reflex as rx
from enum import Enum
from .fonts import Font as Font
from .colors import textcolor, color

class Size(Enum):
    small = "0.5em"
    default = "1em"
    big = "2em"
    very_big = "4em"
    so_big = "6em"

stylesheets = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Ruluko&display=swap"
]

base_style = {
    "font_family": Font.default.value,
    "color": textcolor.primary.value,
    "background": color.primary.value
}
