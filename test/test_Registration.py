import unittest
from logic.registration import registration
from logic.client import client
from logic.place import place


class testItem(unittest.TestCase):
    incoming = registration(subject=client("0", 'Name', "Last name", "Address", "Phone", "Email", 0, "Event", "Allowed places"), area=place("0", "Name", 'Type', 'Location'))

    def test_instance(self):
        self.assertIsInstance(self.incoming, registration, "Its instance!")

    def test_client(self):
        self.assertEqual(self.incoming.subject, ("0", 'Name', "Last name", "Address", "Phone", "Email", 0, "Event", "Allowed places"))

    def test_area(self):
        self.assertEqual(self.incoming.area, ("0", "Name", 'Type', 'Location'))

    def test__str__(self):
        self.assertEqual(self.incoming.__str__(), {'client': "Client", 'area': 'Area'})


if __name__ == '__main__':
    unittest.main()
