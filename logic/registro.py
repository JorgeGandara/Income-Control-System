#from ABC import ABC, abstractmethod
from logic.cliente import cliente
from logic.lugar import lugar

class registro():
  #@abstractmethod
  def __init__(self, sujeto: cliente = "cliente", area: lugar = "lugar"):
    if type(sujeto) != str:
      print("Por favor ingrese un cliente valido.")
      return
    if type(area) != str:
      print("Por favor ingrese un area valida.")
      return      
    self.sujeto: str = sujeto
    self.area: str = area
    
  @property
  def area(self) -> str:
    return self._area
    
  @area.setter
  def area(self, area_nuevo: str) -> None:
    if area_nuevo > 0 and isinstance(area_nuevo, str):
        self._area = area_nuevo
    else:
        print("Por favor ingrese un area valida.")

  @property
  def sujeto(self) -> str:
    return self._sujeto
    
  @sujeto.setter
  def sujeto(self, sujeto_nuevo: str) -> None:
    if isinstance(sujeto_nuevo, str):
      self._sujeto = sujeto_nuevo
    else:
      print("Por favor ingrese un sujeto valido.")
      
  #@abstractmethod
  def __str__(self):
      return f"Ente: {self.area}, {self.sujeto}"