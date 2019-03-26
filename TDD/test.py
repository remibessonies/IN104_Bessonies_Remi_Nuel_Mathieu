import unittest

from ..OOP.classe import Vehicles, Car, Moto

Bob = Vehicles('rouge',4,2000,10)

class TestVehicles(unittest.TestCase):
	def test_getWeight(self):
		resultat = Bob.getWeight()
		self.assertEqual(resultat, 2000)


if __name__ == '__main__':
	unittest.main()
