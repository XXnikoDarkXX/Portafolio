import reflex as rx
from .primitives import container, btn

def navbar():
    return rx.box(
        rx.hstack(
            rx.text("Cuneta FC", color="white"),
            rx.spacer(),
            btn("Inicio", "/"),
            btn("Sobre mi", "/about"),
            btn("Proyectos", "/projects"),
            btn("Contacto", "/contact"),
            spacing="2",
        ),
        position="sticky", top="0", z_index="50",
        padding_y="0.8rem", padding_x="1rem",
        background_color="rgba(5,10,20,0.6)",
        border_bottom="1px solid rgba(255,255,255,0.08)",
        backdrop_filter="blur(8px)",
    )

def page_shell(content):
    return rx.box(
        navbar(),
        container(content),
        background_image=(
            "radial-gradient(80rem 40rem at 20% -10%, #1b2a6b33, transparent), "
            "radial-gradient(80rem 40rem at 120% 10%, #6b1b4a33, transparent)"
        ),
        background_color="#0b1020",
        min_height="100vh",
        color="rgba(255,255,255,0.92)",
    )

def page_shell_free(*children):
    return rx.box(navbar(), *children,
      background_color="#0b1020",
      min_height="100vh",
      color="rgba(255,255,255,0.92)",
    )

