import reflex as rx
from ..ui.primitives import card, pill, btn
from ..ui.layout import page_shell


def exp_item(titulo, empresa, fechas, bullets):
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(titulo, size="4"),
                rx.spacer(),
                pill(fechas),
            ),
            rx.hstack(pill(empresa)),
            rx.vstack(*[rx.text(f"- {b}") for b in bullets], spacing="1"),
            spacing="2",
        ),
        padding_left="1rem",
        border_left="2px solid rgba(255,255,255,0.15)",
    )


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
    test_card = card(
        rx.text("Sandbox", size="6"),
        rx.text("Aqui puedes probar cosas rapidas."),
        btn("Accion demo", "#", True),
    )

    exp_card = card(
    rx.text("Experiencia", size="6"),
    exp_item(
        "QA Engineer",
        "Acme Corp",
        "2023 - Presente",
        ["E2E con Robot Framework", "CI/CD en GitHub Actions"]
    ),
    exp_item(
        "DevOps Jr",
        "Innova",
        "2021 - 2023",
        ["Contenedores Docker", "Monitoreo basico y alertas"]
    ),
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
            exp_card, 
            test_card,
            rx.text("Proyectos", size="6"),
            proyectos,
            spacing="4",
        )
    )
