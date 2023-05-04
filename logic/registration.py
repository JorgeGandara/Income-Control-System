# from ABC import ABC, abstractmethod
from logic.client import client
from logic.place import place


class registration(client, place):
    def __init__(self, subject: client = "client", area: place = "place"):
        super().__init__()
        if type(subject) != str:
            print("Please enter a valid client.")
            return
        if type(area) != str:
            print("Please enter a valid area.")
            return
        self._subject: client = subject
        self._area: place = area

    @property
    def area(self) -> place:
        return self._area

    @area.setter
    def area(self, new_area: str) -> None:
        if new_area > 0 and isinstance(new_area, str):
            self._area = new_area
        else:
            print("Please enter a valid area.")

    @property
    def subject(self) -> client:
        return self._subject

    @subject.setter
    def subject(self, new_subject: str) -> None:
        if isinstance(new_subject, str):
            self._subject = new_subject
        else:
            print("Please enter a valid subject.")

    def __str__(self):
        return {"subject": self.subject, "area": self.area}
