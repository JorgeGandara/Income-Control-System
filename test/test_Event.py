import unittest
from logic.event import event


class testEvent(unittest.TestCase):
    person = event(id="0", name='Name', eventTime=0, place="Place")

    def test_instance(self):
        self.assertIsInstance(self.person, event, "Its instance!")

    def test_id(self):
        self.assertEqual(self.person.id, "0")

    def test_name(self):
        self.assertEqual(self.person.name, "Name")

    def test_eventTime(self):
        self.assertEqual(self.person.eventTime, 0)

    def test_place(self):
        self.assertEqual(self.person.place, 'Place')

    def test__str__(self):
        self.assertEqual(self.person.__str__(), {'id': "0", 'name': 'Name', 'eventTime': 0, 'place': 'Place'})


if __name__ == '__main__':
    unittest.main()
