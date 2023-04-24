from logic.ente import ente

class objeto(ente):
    def __init__(self, id: str = "0", nombre: str = "nombre", descripcion: str="descripcion", lugaresPermitidos: str="Lugares permitidos", estado: str= "Estado"):
      super().__init__(id, nombre)
      self.descripcion = descripcion
      self.lugaresPermitidos = lugaresPermitidos
      self.estado = estado

    # Getter y Setter para el atributo descripcion
    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value) -> str:
        self._descripcion = value
      
    # Getter y Setter para el atributo lugaresPermitidos
    @property
    def lugaresPermitidos(self) -> str:
        return self._lugaresPermitidos

    @lugaresPermitidos.setter
    def lugaresPermitidos(self, value) -> str:
        self._lugaresPermitidos = value

    # Getter y Setter para el atributo estado
    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, value) -> str:
        self._estado = value
      
    def __str__(self):
      return f"Objeto: {self.id}: {self.nombre}, {self.descripcion}, {self.estado}, Lugares permitidos: {self.lugaresPermitidos}"
      
    def equals(self, other):
      if isinstance(other, objeto):
        return self.id == other.id and self.nombre == other.nombre and self.descripcion== other.descripcion and self.estado == other.estado
        return False


