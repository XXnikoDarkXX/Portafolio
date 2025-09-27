import reflex as rx
from ..ui.primitives import card, pill, btn, wide_container, container
from ..ui.layout import page_shell
from ..ui.layout import page_shell_free  # usa el shell libre aqui

bg = {
        "normal": "rgba(0,0,0,0.12)",   # tal como ahora
        "dark":   "rgba(0,0,0,0.28)",   # más negro/transparente
        "ghost":  "rgba(255,255,255,0.04)" # clarito
    }
def exp_item(titulo, empresa, fechas, bullets,tone):
    return rx.box(
        
        rx.vstack(
            rx.hstack(
                rx.text(titulo, size="4"),
                rx.spacer(),
                pill(fechas),
            ),
            rx.hstack(pill(empresa)),
            rx.vstack(*[rx.text(f"- {b}", white_space="pre-wrap") for b in bullets], spacing="1"),
            spacing="2",
        ),
        padding_left="1rem",
        padding_top="1rem",
        border_left="2px solid rgba(255,255,255,0.15)",
        background_color=tone,
        width="100%",
    )


def index():
    # HERO: en móvil (base) apila vertical, en md+ se pone en fila
    hero = rx.hstack(
    rx.avatar(name="Tu Nombre", src="/profile.svg", size="9", radius="full"),
    rx.vstack(
        rx.text("Hola, soy Tu Nombre", size="7"),
        rx.hstack(pill("QA/DevOps"), pill("Python"), pill("Runner"), pill("Dog dad"), spacing="2", wrap="wrap"),
        rx.hstack(btn("GitHub","https://github.com/", True), btn("LinkedIn","https://www.linkedin.com/", True), spacing="2", wrap="wrap"),
        spacing="3",
        align={"base": "center", "md": "start"},   # ← centrado en móvil, “start” en desktop
    ),
    align="center",
    justify="center",                               # ← centramos el grupo
    width="100%",                                   # ← ocupa todo el ancho disponible
    spacing="4",
    direction={"base": "column", "md": "row"},
    )
    test_card = card(
        rx.text("Sandbox", size="6"),
        rx.text("Aqui puedes probar cosas rapidas."),
        btn("Accion demo", "#", True),
    )

    exp_card = card(
    rx.text("Experiencia", size="6"),
    
    exp_item(
        "RPA Consultant",
        "Ernest and Young",
        "Mar. 2021 - Junio. 2024",
        ["Mantenimiento, resolución de incidencia, desarrollo tanto de correctivos como evolutivos en los procesos", 
         "Documentación de procesos: PDD, TD, SDD, TTD",
        "Creación de nuevos procesos RPA: \n"+
        "  + Análisis de la solución con el cliente (levantamiento BC) Diseño, desarrollo y testeo de los procesos QA,"+
        "pruebas UAT para implementar en producción "
        ]
         ,bg["dark"]
    ),
    exp_item(
        "DevOps Jr",
        "Innova",
        "2021 - 2023",
        ["Contenedores Docker", "Monitoreo basico y alertas"],bg["ghost"]
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

    return page_shell_free(
    # Hero: ancho y con titulo a la izquierda
    wide_container(
        rx.vstack(
            rx.text("Bienvenido", size="8"),
            hero,
            spacing="3",
            align="start",        # titulo y hero alineados a la izquierda
            width="100%",
        )
    ),

    # Experiencia: limita ancho y centra
    wide_container(
    rx.box(
        exp_card,
        width="50%",
        max_width={"base": "100%", "md": "60rem", "lg": "70rem"},  # límite responsive
        margin_x="auto",  # centra
        )
    ),
    
    # Proyectos: titulo + grid ocupando ancho completo
    wide_container(
        rx.vstack(
            rx.text("Proyectos", size="6"),
            rx.box(proyectos, width="100%"),
            spacing="3",
            align="start",
            width="100%",
        )
    ),
)