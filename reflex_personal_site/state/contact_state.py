import reflex as rx

class ContactState(rx.State):
    name: str = ""
    email: str = ""
    message: str = ""
    sent: bool = False

    def send(self):
        self.sent = bool(self.name and self.email and self.message)
