import reflex as rx

def container(*children):
    return rx.box(
        rx.vstack(*children, spacing="3"),
        width="100%", max_width="80rem", margin_x="auto",
        padding_x=["1rem","2rem","3rem"], padding_y=["1rem","2rem","3rem"],
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
