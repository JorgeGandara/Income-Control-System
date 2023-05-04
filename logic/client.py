from logic.person import person


class client(person):
    def __init__(self, id: str = "0", name: str = "name", lastName: str = "lastName", address: str = "address",
                 phone: str = "phone", email: str = "email", stayTime: int = 0, event: str = "event",
                 allowedPlaces: str = "allowedPlaces", employeeOnCharge: str = "employeeOnCharge"):
        super().__init__(id, name, lastName, address, phone, email)
        self._stayTime = stayTime
        self._event = event
        self._allowedPlaces = allowedPlaces
        self._employeeOnCharge = employeeOnCharge

    @property
    def stayTime(self) -> int:
        return self._stayTime

    @stayTime.setter
    def stayTime(self, value) -> int:
        self._stayTime = value

    @property
    def event(self) -> str:
        return self._event

    @event.setter
    def event(self, name) -> str:
        self._event = name

    @property
    def allowedPlaces(self) -> str:
        return self._allowedPlaces

    @allowedPlaces.setter
    def allowedPlaces(self, names) -> str:
        self._allowedPlaces = names

    @property
    def employeeOnCharge(self) -> str:
        return self._employeeOnCharge

    @employeeOnCharge.setter
    def employeeOnCharge(self, names) -> str:
        self.employeeOnCharge = names

    def __str__(self):
        return {"id": self.id, "name": self.name, "lastName": self.lastName, "address": self.address,
                "phone": self.phone, "email": self.email, "stayTime": self.stayTime, "event": self.event,
                "allowedPlaces": self.allowedPlaces, "employeeOnCharge": self.employeeOnCharge}

    def equals(self, other):
        if isinstance(other, client):
            return super().equals(
                other) and self.id == other.id and self.name == other.name and self.lastName == other.lastName and self.address == other.address and self.phone == other.phone and self.email == other.email and self.stayTime == other.stayTime and self.event == other.event and self.allowedPlaces == other.allowedPlaces and self.employeeOnCharge == other.employeeOnCharge
        return False
