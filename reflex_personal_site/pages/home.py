import reflex as rx
from ..ui.primitives import card, pill, btn
from ..ui.layout import page_shell

def index():
    # HERO: en móvil (base) apila vertical, en md+ se pone en fila
    hero = rx.hstack(
        rx.avatar(name="Tu Nombre", src="/profile.svg", size="9", radius="full"),
        rx.vstack(
            rx.text("Hola, soy Tu Nombre", size="7"),
            rx.hstack(pill("QA/DevOps"), pill("Python"), pill("Runner"), pill("Dog dad"), spacing="2", wrap="wrap"),
            rx.hstack(btn("GitHub","https://github.com/", True), btn("LinkedIn","https://www.linkedin.com/", True), spacing="2", wrap="wrap"),
            spacing="3", align="start",
        ),
        align="center",
        spacing="4",
        direction={"base": "column", "md": "row"},  # <- responsive
    )

    # GRID: 1 columna en móvil, 2 en sm, 3 en md
    proyectos = rx.grid(
        card(rx.text("Proyecto A"), rx.text("Desc A"), btn("Ver repo ->", "#", True)),
        card(rx.text("Proyecto B"), rx.text("Desc B"), btn("Ver repo ->", "#", True)),
        card(rx.text("Proyecto C"), rx.text("Desc C"), btn("Ver repo ->", "#", True)),
        columns={"base": "1", "sm": "2", "md": "3"},  # <- responsive
        spacing="3",
    )

    return page_shell(
        rx.vstack(
            rx.text("Bienvenido", size="8"),
            hero,
            rx.text("Proyectos", size="6"),
            proyectos,
            spacing="4",
        )
    )
