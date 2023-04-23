import unittest
from logic.objeto import objeto


class TestObjeto(unittest.TestCase):
    person = objeto(id= "0", nombre= "Nombre", descripcion= "Descripcion", lugaresPermitidos= "Lugares permitidos", estado= "Estado")

    def test_instance(self):
        self.assertIsInstance(self.objeto, objeto, "Its instance!")

    def test_id(self):
        self.assertEqual(self.objeto.id, "0")

    def test_nombre(self):
        self.assertEqual(self.objeto.nombre, "Nombre")

    def test_tiempoEvento(self):
        self.assertEqual(self.objeto.descripcion, "Descripcion")

    def test_lugar(self):
        self.assertEqual(self.objeto.lugaresPermitidos, 'Lugares permitidos')

    def test_lugar(self):
        self.assertEqual(self.objeto.estado, 'Estado')

    def test__str__(self):
        self.assertEqual(self.objeto.__str__(), {'id': "0", 'nombre': 'Nombre', 'descripcion': 'Descripcion', 'lugaresPermitidos': 'Lugares permitidos', "estado":"Estado"})

if __name__ == '__main__':
    unittest.main()