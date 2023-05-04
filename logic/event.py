# Diego Garcia
class event():
    def __init__(self, id: str = "0", name: str = "name", eventTime: int = 0, place: str = "place"):
        self._id = id
        self._name = name
        self._eventTime = eventTime
        self._place = place

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
    def eventTime(self) -> int:
        return self._eventTime

    @eventTime.setter
    def eventTime(self, value) -> int:
        self._eventTime = value

    @property
    def place(self) -> str:
        return self._place

    @place.setter
    def place(self, value) -> str:
        self._place = value

    def __str__(self):
        return {"id": self.id, "name": self.name, "eventTime": self.eventTime, "place": self.place}

    def equals(self, other):
        if isinstance(other, event):
            return self.id == other.id and self.name == other.name and self.eventTime == other.eventTime and self.place == other.place
        return False
