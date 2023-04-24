#from ABC import ABC, abstractmethod

class ente():
  #@abstractmethod
  def __init__(self, id: str = "0", nombre: str = "nombre"):
    self.id = id
    self.nombre = nombre
    
  @property
  def id(self) -> str:
    return self.id
    
  @id.setter
  def id(self, value) -> str:
    self.id = value

  @property
  def nombre(self) -> str:
    return self.nombre
    
  @nombre.setter
  def nombre(self, value) -> str:
    self.nombre = value
    
  #@abstractmethod
  def __str__(self):
      return f"Ente: {self.id}, {self.nombre}"