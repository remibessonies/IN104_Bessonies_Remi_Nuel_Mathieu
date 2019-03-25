class Vehicles:
	def __init__(self,color,nb_wheels,weight,consommation):
		self.color= color
		self.nb_wheels = nb_wheels
		self.weight = weight
		self.consommation = consommation

	def getWeight(self):
		return self.weight

	def getConso(self):
		return self.consommation




class Car(Vehicles):
	def __init__(self,nb_seat,color,nb_wheels,weight,consommation):
		self.nb_seat = nb_seat
		Vehicles.__init__(self,color,nb_wheels,weight,consommation)

	def __str__(self):
		return ("Voiture de "+str(self.getWeight())+"kg.")
	def conso(self):
		print("Consommation de la voiture : "+str(self.getConso())+ "L au 100")



class Moto(Vehicles):
	def __init__(self,en_y,cylindré,color,nb_wheels,weight,consommation):
		self.en_y = en_y
		self.cylindré= cylindré
		Vehicles.__init__(self,color,nb_wheels,weight,consommation)


	def __str__(self):
		return ("Moto de "+str(self.getWeight())+"kg.")
	def conso(self):
		print("Consommation de la moto : "+str(self.getConso())+ "L au 100")


Bob = Car(4,'rouge',4,2000,10)
print(Bob.__str__())
print(Bob.conso())

	
Bill= Moto(True, 125,'noire',2,500,7)		
print(Bill.__str__())
print(Bill.conso())

