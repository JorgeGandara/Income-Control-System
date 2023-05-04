import unittest
from logic.person import person


class testPerson(unittest.TestCase):
    person = person(id="0", name='Name', lastName="Last name", address="Address", phone="Phone", email="Email")

    def test_instance(self):
        self.assertIsInstance(self.person, person, "Its instance!")

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

    def test__str__(self):
        self.assertEqual(self.person.__str__(),
                         {'id': "0", 'name': 'Name', 'lastName': "Last name", 'address': 'Address', 'phone': "Phone",
                          'email': 'Email'})


if __name__ == '__main__':
    unittest.main()
