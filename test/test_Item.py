import unittest
from logic.item import item


class testItem(unittest.TestCase):
    incoming = item(id="0", name="Name", description="Description", allowedPlaces="Allowed places", status="Status")

    def test_instance(self):
        self.assertIsInstance(self.incoming, item, "Its instance!")

    def test_id(self):
        self.assertEqual(self.incoming.id, "0")

    def test_name(self):
        self.assertEqual(self.incoming.name, "Name")

    def test_description(self):
        self.assertEqual(self.incoming.description, "Description")

    def test_allowedPlaces(self):
        self.assertEqual(self.incoming.allowedPlaces, 'Allowed places')

    def test_status(self):
        self.assertEqual(self.incoming.status, 'Status')

    def test__str__(self):
        self.assertEqual(self.incoming.__str__(),
                         {'id': "0", 'name': 'Name', 'description': 'Description', 'allowedPlaces': 'Allowed places',
                          "status": "Status"})


if __name__ == '__main__':
    unittest.main()
