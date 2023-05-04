import unittest
from logic.place import place


class testPlace(unittest.TestCase):
    place = place(id="0", name="Name", type='Type', location='Location')

    def test_instance(self):
        self.assertIsInstance(self.place, place, "Its instance!")

    def test_id(self):
        self.assertEqual(self.place.id, "0")

    def test_name(self):
        self.assertEqual(self.place.name, "Name")

    def test_type(self):
        self.assertEqual(self.place.type, "Type")

    def test_location(self):
        self.assertEqual(self.place.location, "Location")

    def test__str__(self):
        self.assertEqual(self.place.__str__(), {"id": "0", 'name': 'Name', 'type': 'Type', 'location': 'Location'})


if __name__ == '__main__':
    unittest.main()
