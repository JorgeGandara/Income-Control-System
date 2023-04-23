import unittest
from logic.evento import evento


class TestEvento(unittest.TestCase):
    person = evento(id="0", nombre='Nombre', tiempoEvento = 0, lugar = "Lugar")

    def test_instance(self):
        self.assertIsInstance(self.person, evento, "Its instance!")

    def test_id(self):
        self.assertEqual(self.person.id, "0")

    def test_nombre(self):
        self.assertEqual(self.person.nombre, "Nombre")

    def test_tiempoEvento(self):
        self.assertEqual(self.person.tiempoEvento, 0)

    def test_lugar(self):
        self.assertEqual(self.person.lugar, 'Lugar')

    def test__str__(self):
        self.assertEqual(self.person.__str__(), {'id': "1", 'nombre': 'Nombre', 'tiempoEvento': 0, 'lugar': 'Lugar'})

if __name__ == '__main__':
    unittest.main()