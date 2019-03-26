import unittest

from OOP.classe import Vehicles, Car, Moto #impossible d'importer  

Bob = Car(4,'rouge',4,2000,10)
Bill= Moto(True, 125,'noire',2,500,7)

class TestVehicles(unittest.TestCase):
	def test_getWeight_car(self):
		resultat = Bob.getWeight()
		self.assertEqual(resultat, 2000)


	def test_getConso_car(self):
		resultat = Bob.getConso()
		self.assertEqual(resultat, 10)

	def test__str__moto(self):
		resultat = Bill.__str__()
		self.assertEqual(resultat, "Moto de 500kg.")

	def test__str__moto(self):
		resultat = Bob.__str__()
		self.assertEqual(resultat, "Voiture de 2001kg.") #test volontairement erroné	
		





if __name__ == '__main__':
	unittest.main()
