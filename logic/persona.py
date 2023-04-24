from logic.ente import ente

class persona(ente):
    def __init__(self,id: str = "0", nombre: str = "Nombre", apellido: str = "Apellido", direccion: str="Direccion", telefono: int="Telefono", email: str="Email"):
      super().__init__(id, nombre)
      self.apellido = apellido
      self.direccion = direccion
      self.telefono = telefono
      self.email = email

    # Getter y Setter para el atributo apellido
    @property
    def apellido(self) -> str:
        return self.apellido

    @apellido.setter
    def apellido(self, value) -> str:
        self.apellido = value
      
    # Getter y Setter para el atributo direccion
    @property
    def direccion(self) -> str:
        return self.direccion

    @direccion.setter
    def direccion(self, value) -> str:
        self.direccion = value

    # Getter y Setter para el atributo telefono
    @property
    def telefono(self) -> int:
        return self.telefono

    @telefono.setter
    def telefono(self, value) -> int:
        self.telefono = value

    # Getter y Setter para el atributo email
    @property
    def email(self) -> str:
        return self.email

    @email.setter
    def email(self, value) -> str:
        self.email = value

    def __str__(self):
      return f"Persona {self.id}: {self.nombre} {self.apellido}, {self.direccion}, {self.telefono}, {self.email}"
      
    def equals(self, other):
      if isinstance(other, persona):
        return self.id == other.id and self.nombre == other.nombre and self.direccion == other.direccion and self.telefono == other.telefono and self.email == other.email
        return False


