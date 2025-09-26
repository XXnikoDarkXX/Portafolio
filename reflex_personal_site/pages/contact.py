import reflex as rx
from ..ui.primitives import card, btn
from ..ui.layout import page_shell
from ..state.contact_state import ContactState

def contact():
    form = rx.cond(
        ContactState.sent,
        card(rx.text("Mensaje enviado."), btn("Volver al inicio", "/")),
        card(
            rx.vstack(
                rx.input(placeholder="Tu nombre", value=ContactState.name, on_change=ContactState.set_name),
                rx.input(placeholder="Tu email", type="email", value=ContactState.email, on_change=ContactState.set_email),
                rx.text_area(placeholder="En que te puedo ayudar", value=ContactState.message, on_change=ContactState.set_message, min_height="8rem"),
                btn("Enviar"),
                rx.button("Enviar", on_click=ContactState.send),
                spacing="2",
            ),
        ),
    )
    return page_shell(rx.vstack(rx.text("Contacto", size="8"), form, spacing="4"))
