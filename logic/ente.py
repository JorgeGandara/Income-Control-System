#from ABC import ABC, abstractmethod

class ente():
  #@abstractmethod
  def __init__(self, id: int = 0, nombre: str = "nombre"):
    if type(id) != int:
      print("Por favor ingrese un id valido.")
      return
    if type(nombre) != str:
      print("Por favor ingrese un nombre valido.")
      return
    self.id: int = id
    self.nombre: str = nombre
    
  @property
  def id(self) -> int:
    return self._id
    
  @id.setter
  def id(self, id_nuevo: int) -> None:
    if id_nuevo > 0 and isinstance(id_nuevo, int):
        self._id = id_nuevo
    else:
        print("Por favor ingrese un id valido.")

  @property
  def nombre(self) -> str:
    return self._nombre
    
  @nombre.setter
  def nombre(self, nombre_nuevo: str) -> None:
    if isinstance(nombre_nuevo, str):
      self._descripcion = nombre_nuevo
    else:
      print("Por favor ingrese un nombre valido.")
    
  #@abstractmethod
  def __str__(self):
      return f"Ente: {self.id}, {self.nombre}"