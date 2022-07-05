#####PERSONA#####
from mailbox import NoSuchMailboxError


class Persona:
    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido
    
    def hablar(self):
        print(f"Estoy hablando y mi nombre es {self.nombre} {self.apellido}")
