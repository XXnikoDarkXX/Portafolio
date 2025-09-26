import reflex as rx
from .pages.home import index
from .pages.about import about
from .pages.projects import projects
from .pages.contact import contact

app = rx.App()
app.add_page(index, route="/", title="Inicio · Tu Nombre")
app.add_page(about, route="/about", title="Sobre mi · Tu Nombre")
app.add_page(projects, route="/projects", title="Proyectos · Tu Nombre")
app.add_page(contact, route="/contact", title="Contacto · Tu Nombre")
