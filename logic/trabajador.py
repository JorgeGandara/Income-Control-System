from logic.persona import persona

class trabajador(persona):
    def __init__(self, id: str="Id", nombre: str = "Nombre", apellido: str = "Apellido", direccion: str="Direccion", telefono: int="Telefono", email: str="Email", usuario: str = "usuario", contrasena: str = "contraseña", entesEncargados: list = [], disponibilidad: bool = True):
        super().__init__(id, nombre, apellido, direccion, telefono, email)
        self.usuario = usuario
        self.contrasena = contrasena
        self.entesEncargados = entesEncargados
        self.disponibilidad = disponibilidad

    @property
    def usuario(self) -> str:
        return self._usuario
    
    @usuario.setter
    def usuario(self, value) -> str:
        self._usuario = value

    @property
    def contrasena(self) -> str:
        return self._contrasena
    
    @contrasena.setter
    def contrasena(self, value) -> str:
        self._contrasena = value

    @property
    def entesEncargados(self) -> list:
        return self._entesEncargados
    
    @entesEncargados.setter
    def entesEncargados(self, value) -> list:
        self._entesEncargados = value

    @property
    def disponibilidad(self) -> bool:
        return self._disponibilidad
    
    @disponibilidad.setter
    def disponibilidad(self, value) -> bool:
        self._disponibilidad = value

    def __str__(self):
      if(self.disponibilidad==True):
        disp="Disponible"
      else:
        disp="No disponible"
      return f"Trabajador {self.id}: {self.nombre} {self.apellido}, {self.direccion}, {self.telefono}, {self.email}, {self.usuario}, {self.contrasena}, {disp}, encargados: {self.entesEncargados}, "
      
    def equals(self, other):
      if isinstance(other, trabajador):
        return super().equals(other) and self.usuario == other.usuario and self.contrasena == other.contrasena and self.entesEncargador == other.entesEncargados and self.disponibilidad == other.disponibilidad
        return False

    def iniciarSesion(self, usuario, contrasena):
      if(usuario==self.usuario and contrasena==self.contrasena):
        return True
      else:
        return False

    def cambiarDisponibilidad(self, bool):
      self.disponibilidad = bool