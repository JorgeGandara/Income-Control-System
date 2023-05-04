import unittest
from logic.employee import employee


class testEmployee(unittest.TestCase):
    person = employee(id="0", name='Name', lastName="Last name", address="Address", phone="Phone", email="Email",
                      user='User', password="Password", availability=True)

    def test_instance(self):
        self.assertIsInstance(self.person, employee, "Its instance!")

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

    def test_user(self):
        self.assertEqual(self.person.user, 'User')

    def test_password(self):
        self.assertEqual(self.person.password, 'Password')

    def test_availability(self):
        self.assertEqual(self.person.availability, True)

    def test__str__(self):
        self.assertEqual(self.person.__str__(),
                         {'id': "0", 'name': 'Name', 'lastName': "Last name", 'address': 'Address', 'phone': "Phone",
                          'email': 'Email', 'user': 'User', 'password': 'Password','availability': True})


if __name__ == '__main__':
    unittest.main()
