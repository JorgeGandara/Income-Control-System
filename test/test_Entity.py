import unittest

from logic.entity import entity


class testEntity(unittest.TestCase):
    incoming = entity(id="0", name="Name")

    def test_instance(self):
        self.assertIsInstance(self.incoming, entity, "Its instance!")

    def test_id(self):
        self.assertEqual(self.incoming.id, "0")

    def test_name(self):
        self.assertEqual(self.incoming.name, "Name")

    def test__str__(self):
        self.assertEqual(self.incoming.__str__(), {'id': "0", 'name': 'Name'})


if __name__ == '__main__':
    unittest.main()
