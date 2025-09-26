import reflex as rx
from ..ui.primitives import card, btn
from ..ui.layout import page_shell

def project_card(title, desc, href):
    return card(rx.text(title, size="5"), rx.text(desc), btn("Ver repo ->", href, True))

def projects():
    grid = rx.grid(
        project_card("RF E2E Starter", "Plantilla de Robot Framework con reporteria y buenas practicas.", "https://github.com/username/rf-e2e-starter"),
        project_card("AutoDeploy VPS", "CLI en Python para desplegar contenedores y renovar certificados.", "https://github.com/username/autodeploy-vps"),
        project_card("Invest Dash", "Mini dashboard para fondos y cartera personal.", "https://github.com/username/invest-dash"),
        columns="3", spacing="3",
    )
    return page_shell(rx.vstack(rx.text("Proyectos", size="8"), grid, spacing="4"))
