from logic.persona import persona

class cliente(persona):
    def __init__(self, id: str="Id", nombre: str = "Nombre", apellido: str = "Apellido", direccion: str="Direccion", telefono: int="Telefono", email: str="Email", tiempoPermanencia: int = 0, evento: str = "evento", lugaresPermitidos: str="Lugares permitidos"):
      super().__init__(id, nombre, apellido, direccion, telefono, email)
      self.tiempoPermanencia = tiempoPermanencia	
      self.evento = evento
      self.lugaresPermitidos = lugaresPermitidos
    
    @property
    def tiempoPermanencia(self) -> int:
        return self._tiempoPermanencia
    
    @tiempoPermanencia.setter
    def tiempoPermanencia(self, value) -> int:
        self._tiempoPermanencia = value

    @property
    def evento(self) -> str:
        return self._evento
    
    @evento.setter
    def evento(self, name) -> str:
        self._evento = name

    @property
    def lugaresPermitidos(self) -> str:
        return self._lugaresPermitidos
    
    @lugaresPermitidos.setter
    def lugaresPermitidos(self, names) -> str:
        self._lugaresPermitidos = names
      
    def __str__(self):
        return (f'Cliente {self.id}: {self.nombre} {self.apellido}, {self.direccion}, {self.telefono}, {self.email}, {self.tiempoPermanencia} dias, Evento: {self.evento}, {self.lugaresPermitidos}')
      
    def equals(self, other):
      if isinstance(other, persona):
        return super().equals(other) and self.id == other.id and self.nombre == other.nombre and self.appelido == other.appelido and self.direccion == other.direccion and self.telefono == other.telefono and self.email == other.email and self.evento == other.evento
        return False


  