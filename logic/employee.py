from logic.person import person
from logic.client import client


class employee(person):
    def __init__(self, id: str = "id", name: str = "name", lastName: str = "lastName", address: str = "address",
                 phone: str = "phone", email: str = "email", user: str = "user", password: str = "password", availability: bool = True):
        super().__init__(id, name, lastName, address, phone, email)
        self._user = user
        self._password = password
        self._availability = availability

    @property
    def user(self) -> str:
        return self._user

    @user.setter
    def user(self, value) -> str:
        self._user = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value) -> str:
        self._password = value

    @property
    def availability(self) -> bool:
        return self._availability

    @availability.setter
    def availability(self, value) -> bool:
        self._availability = value

    def __str__(self):
        return {"id": self.id, "name": self.name, "lastName": self.lastName, "address": self.address,
                "phone": self.phone, "email": self.email, "user": self.user, "password": self.password, "availability": self.availability}

    def equals(self, other):
        if isinstance(other, employee):
            return super().equals(other) and self.user == other.user and self.password == other.password and self.availability == other.availability
        return False

    def iniciarSesion(self, user, password):
        if user == self.user and password == self.password:
            return True
        else:
            return False

    def cambiarDisponibilidad(self, bool):
        self.availability = bool
