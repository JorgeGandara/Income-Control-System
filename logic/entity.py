# from ABC import ABC, abstractmethod

class entity():
    # @abstractmethod
    def __init__(self, id: str = "0", name: str = "name"):
        self._id = id
        self._name = name

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

    # @abstractmethod
    def __str__(self):
        return {"id": self.id, "name": self.name}
