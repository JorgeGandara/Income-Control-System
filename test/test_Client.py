import unittest
from logic.client import client


class testClient(unittest.TestCase):
    person = client(id="0", name='Name', lastName="Last name", address="Address", phone="Phone", email="Email",
                    stayTime=0, event="Event", allowedPlaces="Allowed places", employeeOnCharge="Employee on charge")

    def test_instance(self):
        self.assertIsInstance(self.person, client, "Its instance!")

    def test_id(self):
        self.assertEqual(self.person.id, "0")

    def test_name(self):
        self.assertEqual(self.person.name, "Name")

    def test_lastName(self):
        self.assertEqual(self.person.lastName, "Last name")

    def test_address(self):
        self.assertEqual(self.person.address, "Address")

    def test_phone(self):
        self.assertEqual(self.person.phone, "Phone")

    def test_email(self):
        self.assertEqual(self.person.email, "Email")

    def test_stayTime(self):
        self.assertEqual(self.person.stayTime, 0)

    def test_event(self):
        self.assertEqual(self.person.event, 'Event')

    def test_allowedPlaces(self):
        self.assertEqual(self.person.allowedPlaces, 'Allowed places')

    def test_employeeOnCharge(self):
        self.assertEqual(self.person.employeeOnCharge, 'Employee on charge')

    def test__str__(self):
        self.assertEqual(self.person.__str__(),
                         {'id': "0", 'name': 'Name', 'lastName': "Last name", 'address': 'Address', 'phone': "Phone",
                          'email': 'Email', 'stayTime': 0, 'event': 'Event', 'allowedPlaces': 'Allowed places',
                          "employeeOnCharge": "Employee on charge"})


if __name__ == '__main__':
    unittest.main()
