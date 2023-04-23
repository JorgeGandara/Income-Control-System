class lugar():
    def __init__(self, id: str="id", nombre: str = "nombre", tipo: str = "tipo", ubicacion: str="ubicacion"):
        self.id=id
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion      

    #get and the set are done to get the name 
    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, value) -> str:
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value) -> str:
        self._nombre = value
      
    @property
    def tipo(self) -> str:
        return self._tipo
    
    @tipo.setter
    def tipo(self, value) -> str:
        self._tipo = value

    @property
    def ubicacion(self) -> str:
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self, value) -> str:
        self._ubicacion = value

    def __str__(self):
      return f"Lugar: {self.id}: {self.nombre}, {self.tipo}, {self.ubicacion}"
      
    def equals(self, other):
      if isinstance(other, lugar):
        return self.id == other.id and self.nombre == other.nombre and self.tipo== other.tipo and self.ubicacion == other.ubicacion
        return False