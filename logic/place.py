class place():
    def __init__(self, id: str = "0", name: str = "name", type: str = "type", location: str = "location"):
        self._id = id
        self._name = name
        self._type = type
        self._location = location

        # get and the set are done to get the name

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value) -> str:
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> str:
        self._name = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value) -> str:
        self._type = value

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, value) -> str:
        self._location = value

    def __str__(self):
        return {"id": self.id, "name": self.name, "type": self.type, "location": self.location}

    def equals(self, other):
        if isinstance(other, place):
            return self.id == other.id and self.name == other.name and self.type == other.type and self.location == other.location
        return False
