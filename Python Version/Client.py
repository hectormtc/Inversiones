from Product import *

class Client(Product):
	def __init__(self, fname="", lname="", addr="", phone="",
			   deposit="", ID=0, STATE=True, PAY=False):
		self.fname    = fname
		self.lname    = lname
		self.address  = addr
		self.phone    = phone
		self.deposit  = deposit
		self.ID       = ID
		self.STATE    = STATE
		self.PAY      = PAY
		self.newRent()


	def newRent(self, chmod=False):
		if chmod == True:
			self.printInformation()
			self.rentProduct(True)
		else:
			self.rentProduct()


	def printClient(self, quote=False):
		if quote == False:
			print("="*45)
			print("ID       : ", self.getID())
			print("Estado   : ", ("Entregado" if self.isRent() else "Pendiente"))
			print("Pago     : ", ("Pagado"    if self.isPay()  else "Pendiente"))
			print("-"*20)
			print("Nombre   : ", self.getName(), self.getLast())
			print("Tel/Cel  : ", self.getPhone())
			print("Direccion: ", self.getAddress())
			print("Deposito : ", self.getDeposit())


	def isPay(self):
		return self.PAY	


	def inPay(self):
		self.PAY = True


	def notPay(self):
		self.PAY = False


	def isRent(self):
		return self.STATE


	def inRent(self):
		self.STATE = True


	def notRent(self):
		self.STATE = False
#SETTERs

	def setId(self, idClient):
		self.ID = idClient


	def setName(self, fname):
		self.fname = fname


	def setLast(self, lname):
		self.lname = lname


	def setAddress(self, addr):
		self.address = addr


	def setPhone(self, phn):
		self.phone = phn


	def setDeposit(self, depot):
		self.deposit = depot


	def setPAY(self, pay):
		self.PAY = pay
#GETTERS
	
	def getPay(self):
		return self.PAY


	def getName(self):
		return self.fname


	def getLast(self):
		return self.lname


	def getPhone(self):
		return self.phone


	def getAddress(self):
		return self.address


	def getDeposit(self):
		return self.deposit


	def getID(self):
		return self.ID


	def inputClient(self):
		self.fname   = str(input("Nombre   : "))
		self.lname   = str(input("Apellido : "))
		self.phone   = str(input("Tel/Cel  : "))
		self.address = str(input("Direccion: "))
		self.deposit = str(input("Deposito : "))

		#self.pay       = str(input("Pagado?(s/n): "))
		#self.delivered = str(input("Entregado?(s/n): "))

		#self.inPay()  if (self.pay == "s") else self.notPay()
		#self.inRent() if (self.delivered == "s") else self.notRent()



#Los plebes
#Soy cocodrilo
#Narices de ramo
#La pista privada
#Laurita garza
#Quiero que cante conmigo

#El borrecho tucanes o tigres
#Cuando al panteon

