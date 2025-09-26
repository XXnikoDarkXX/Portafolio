import reflex as rx
from ..ui.primitives import card
from ..ui.layout import page_shell

def about():
    return page_shell(
        rx.vstack(
            rx.text("Sobre mi", size="8"),
            card(
                rx.text("Ingeniero QA/DevOps con experiencia en microservicios y Robot Framework."),
                rx.text("Me gusta crear herramientas utiles y documentacion clara."),
            ),
            spacing="4",
        )
    )
