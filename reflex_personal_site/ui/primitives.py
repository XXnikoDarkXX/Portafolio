import reflex as rx

def container(*children):
    return rx.box(
        rx.vstack(*children, spacing="4", align="center"),
        width="100%",
        max_width="100rem",  # o 120rem si lo quieres más ancho
        margin_x="auto",
        padding_x={"base": "1rem", "sm": "2rem", "md": "3rem"},
        padding_y={"base": "1rem", "sm": "2rem", "md": "3rem"},
    )


def card(*children):
    return rx.box(
        rx.vstack(*children, spacing="2", align="start"),
        width="100%",
        padding="1rem",
        border="1px solid rgba(255,255,255,0.08)",
        border_radius="0.75rem",
        background_color="rgba(255,255,255,0.04)",
        box_shadow="0 6px 20px rgba(0,0,0,0.25)",
    )

def pill(text):
    return rx.box(
        rx.text(text),
        padding_x="0.6rem", padding_y="0.25rem",
        border_radius="9999px",
        background_color="rgba(255,255,255,0.10)",
        border="1px solid rgba(255,255,255,0.12)"
    )

def btn(text, href="#", external=False):
    return rx.link(
        rx.box(
            rx.text(text),
            padding_x="0.9rem", padding_y="0.55rem",
            border_radius="0.6rem",
            border="1px solid rgba(255,255,255,0.18)",
            background_color="rgba(255,255,255,0.06)",
            _hover={"background_color":"rgba(255,255,255,0.12)"},
        ),
        href=href, is_external=external
    )
def wide_container(*children):
    return rx.box(
        rx.vstack(*children, spacing="4"),
        width="100%",
        max_width="110rem",                       # antes 120–130rem → un pelín más estrecho
        margin_x="auto",
        padding_x={"base":"1rem","sm":"2rem","md":"3rem"},  # margen interno lateral
    )