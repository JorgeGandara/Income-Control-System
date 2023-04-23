import unittest
from logic.cliente import cliente


class TestCliente(unittest.TestCase):
    person = cliente(id="0", nombre='Nombre',apellido = "Apellido", direccion="Direccion", telefono="Telefono", email="Email", tiempoPermanencia = 0, lugaresPermitido = "Lugares permitidos")

    def test_instance(self):
        self.assertIsInstance(self.person, cliente, "Its instance!")

    def test_id(self):
        self.assertEqual(self.person.id, "0")

    def test_nombre(self):
        self.assertEqual(self.person.nombre, "Nombre")

    def test_apellido(self):
        self.assertEqual(self.person.apellido, "Apellido")

    def test_direccion(self):
        self.assertEqual(self.person.direccion, "Direccion")

    def test_telefono(self):
        self.assertEqual(self.person.telefono, "Telefono")

    def test_email(self):
        self.assertEqual(self.person.email, "Email")

    def test_tiempoPermanencia(self):
        self.assertEqual(self.person.tiempoPermanencia, 0)

    def test_lugarPermitido(self):
        self.assertEqual(self.person.lugaresPermitidos, 'Lugar')

    def test__str__(self):
        self.assertEqual(self.person.__str__(), {'id': "0", 'nombre': 'Nombre', 'apellido': "Apellido", 'direccion': 'Direccion', 'telefono': "Telefono", 'email': 'Email', 'tiempoPermanencia': 0, 'lugaresPermitidos': 'Lugares permitidos'})

if __name__ == '__main__':
    unittest.main()