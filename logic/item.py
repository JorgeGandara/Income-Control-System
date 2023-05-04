from logic.entity import entity


class item(entity):
    def __init__(self, id: str = "0", name: str = "name", description: str = "description",
                 allowedPlaces: str = "allowedPlaces", status: str = "status"):
        super().__init__(id, name)
        self._description = description
        self._allowedPlaces = allowedPlaces
        self._status = status

    # Getter y Setter para el atributo descripcion
    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value) -> str:
        self._description = value

    # Getter y Setter para el atributo lugaresPermitidos
    @property
    def allowedPlaces(self) -> str:
        return self._allowedPlaces

    @allowedPlaces.setter
    def allowedPlaces(self, value) -> str:
        self._allowedPlaces = value

    # Getter y Setter para el atributo estado
    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value) -> str:
        self._status = value

    def __str__(self):
        return {"id": self.id, "name": self.name, "description": self.description, "allowedPlaces": self.allowedPlaces, "status": self.status}

    def equals(self, other):
        if isinstance(other, item):
            return self.id == other.id and self.name == other.name and self.description == other.description and self.allowedPlaces == other.allowedPlaces and self.status == other.status
        return False
