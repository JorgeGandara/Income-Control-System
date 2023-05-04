from logic.entity import entity


class person(entity):
    def __init__(self, id: str = "0", name: str = "name", lastName: str = "lastName", address: str = "address",
                 phone: str = "phone", email: str = "email"):
        super().__init__(id, name)
        self._lastName = lastName
        self._address = address
        self._phone = phone
        self._email = email

    # Getter y Setter para el atributo apellido
    @property
    def lastName(self) -> str:
        return self._lastName

    @lastName.setter
    def lastName(self, value) -> str:
        self._lastName = value

    # Getter y Setter para el atributo direccion
    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value) -> str:
        self._address = value

    # Getter y Setter para el atributo telefono
    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value) -> str:
        self._phone = value

    # Getter y Setter para el atributo email
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value) -> str:
        self._email = value

    def __str__(self):
        return {"id": self.id, "name": self.name, "lastName": self.lastName, "address": self.address,
                "phone": self.phone, "email": self.email}

    def equals(self, other):
        if isinstance(other, person):
            return self.id == other.id and self.name == other.name and self.lastName == self.lastName and other.address == other.address and self.phone == other.phone and self.email == other.email
        return False
