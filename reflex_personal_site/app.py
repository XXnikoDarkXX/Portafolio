import reflex as rx

# -------- STATE --------
class ContactState(rx.State):
    name: str = ""
    email: str = ""
    message: str = ""
    sent: bool = False
    def send(self):
        self.sent = bool(self.name and self.email and self.message)

# -------- UI PRIMITIVES --------
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

# -------- COMMON SECTIONS --------
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
        background_image="radial-gradient(80rem 40rem at 20% -10%, #1b2a6b33, transparent), radial-gradient(80rem 40rem at 120% 10%, #6b1b4a33, transparent)",
        background_color="#0b1020",
        min_height="100vh",
        color="rgba(255,255,255,0.92)",
    )

# -------- PAGES --------
def index():
    hero = rx.hstack(
        rx.avatar(name="Tu Nombre", src="/profile.svg", size="9", radius="full"),
        rx.vstack(
            rx.text("Hola, soy Tu Nombre", size="7"),
            rx.hstack(
                pill("QA/DevOps"), pill("Python"), pill("Runner"), pill("Dog dad"),
                spacing="2", wrap="wrap",
            ),
            rx.hstack(
                btn("GitHub", "https://github.com/", True),
                btn("LinkedIn", "https://www.linkedin.com/", True),
                btn("CV (PDF)", "#"),
                spacing="2", wrap="wrap",
            ),
            spacing="3", align="start",
        ),
        align="center", wrap="wrap", spacing="4",
    )
    highlight = card(
        rx.text("Que hago", size="5"),
        rx.text("Construyo QA pipelines, automatizaciones en Python y despliegues cloud sencillos.", size="4"),
    )
    return page_shell(
        rx.vstack(
            rx.text("Bienvenido", size="8"),
            hero,
            highlight,
            spacing="4",
        )
    )

def about():
    return page_shell(
        rx.vstack(
            rx.text("Sobre mi", size="8"),
            card(
                rx.text("Ingeniero QA/DevOps con experiencia en microservicios y Robot Framework."),
                rx.text("Me gusta crear herramientas utiles y escribir documentacion clara."),
            ),
            spacing="4",
        )
    )

def project_card(title, desc, href):
    return card(
        rx.text(title, size="5"),
        rx.text(desc),
        btn("Ver repo ->", href, True),
    )

def projects():
    return page_shell(
        rx.vstack(
            rx.text("Proyectos", size="8"),
            rx.grid(
                project_card("RF E2E Starter",
                             "Plantilla de Robot Framework con reporteria y buenas practicas.",
                             "https://github.com/username/rf-e2e-starter"),
                project_card("AutoDeploy VPS",
                             "CLI en Python para desplegar contenedores y renovar certificados.",
                             "https://github.com/username/autodeploy-vps"),
                project_card("Invest Dash",
                             "Mini dashboard para fondos y cartera personal.",
                             "https://github.com/username/invest-dash"),
                columns="3", spacing="3",
            ),
            spacing="4",
        )
    )

def contact():
    form = rx.cond(
        ContactState.sent,
        card(
            rx.text("Mensaje enviado. Gracias por contactar.", size="4"),
            btn("Volver al inicio", "/"),
        ),
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
    return page_shell(
        rx.vstack(
            rx.text("Contacto", size="8"),
            form,
            spacing="4",
        )
    )

# -------- APP --------
app = rx.App()
app.add_page(index, route="/", title="Inicio · Tu Nombre")
app.add_page(about, route="/about", title="Sobre mi · Tu Nombre")
app.add_page(projects, route="/projects", title="Proyectos · Tu Nombre")
app.add_page(contact, route="/contact", title="Contacto · Tu Nombre")
