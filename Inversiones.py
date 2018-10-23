import os

try:
	from product import prices
except:
	print("No se encontro producto")
finally:
	prices = {
		'sillaplastica' : 5,
		'sillametalica' : 6,
		'mesaredonda8'  : 10,
		'mesaredonda10' : 20,
		 }

choice = None
clientList = []
clientID = 0

def clear():
	os.system('clear')

clear()

######################################################################
def listProducts():
	print("\n\t"+"="*32)
	print("""\tPRODUCTO\t| PRECIO""")
	print("\t"+"="*32)

	for product, price in prices.items():
		print("\t" + str(product) + "\t| " + str(price) + " lps.")

	print("\t"+"="*32)
	input("\tPresionar enter...")

######################################################################
def findClient(chmod=False):
	global clienList
	select = None

	def find(name=False, apellido=False, phone=False):
		check = False
		def check(state=False):
			if state == True:
				check = True
			else:
				pass


		def onList():
			print("\n"+"="*45)
			print("\n-=-=-=[ CLIENTE ENCONTRADO ]=-=-=-")
			
			if(chmod):
				print("\n-=-=-=-[ CAMBIAR INFORMACION ]=-=-=-")
				client.newRent(True)
				input("Presionar enter...")
				clear()
			else:
				client.printInformation()
				input("Presionar enter...")
				clear()
		

		def outList():
			print("\n"+"="*45)
			print("\n-=-=-=[ CLIENTE NO ENCOTRADO ]=-=-=-")
			input("Presionar enter...")
			clear()


		if name == True:
			nameClient      = str(input("\nNombre del cliente: "))
			for client in clientList:
				check(True) if (nameClient == client.name) else check(False)

		elif apellido == True:
			apellidoClient = str(input("\nApellido del cliente: "))
			for client in clientList:
				check(True) if (apellidoClient == client.apellido) else check(False)
		elif phone == True:
			phoneClient     = int(input("\nNumero del cliente: "))
			for client in clientList:
				check(True) if (phoneClient == client.phone) else check(False)
		
		outList() if check == False else onList()

	
	while select != 4:
		print("\n"+"="*45)
		if chmod == True:
		
			print("\t[ MODIFICAR CLIENTE ]\n")
		else:
			print("\t[ BUSCAR CLIENTE ]\n")
		print(" 1) Nombre\n 2) Apellido\n 3) Telefono\n 4) Volver al menu")
		print("="*45)

		select = int(input("Por: "))
		if select < 1 or select > 4:
			clear()
			print("\n"+"="*45)
			print("\n[!!] La opcion es invalida.")
			print("="*45)
		elif select <= 3:
			if select == 1:
				find(name=True)
			elif select == 2:
				find(apellido=True)
			else:
				find(phone=True)


######################################################################
class Client(object):
	
	ID = 0
	STATE = False
	

	def __init__(self, name, apellido, address, phone, deposit,
		     monto=[], total=[], subtotal=[], product=[], cantidad=[]):
		self.name     = name
		self.apellido = apellido
		self.address  = address
		self.phone    = phone
		self.deposit  = deposit
		self.monto    = monto
		self.total    = total
		self.subtotal = subtotal
		self.product  = product
		self.cantidad = cantidad
	

	def getProduct(self):
		return self.product


	def getMonto(self):
		return self.monto


	def getCantidad(self):
		return self.cantidad


	def getSubtotal(self):
		return self.subtotal


	def getName(self):
		return self.name


	def getTotal(self):
		return sum(self.subtotal)


	def getApellido(self):
		return self.apellido


	def getPhone(self):
		return self.phone


	def getAddress(self):
		return self.address


	def getDeposit(self):
		return self.deposit


	def setState(self, state):
		Client.STATE = state


	def newRent(self, chmod=False):
		if chmod == True:
			self.printInformation()
			self.rentProduct(True)
		else:
			self.rentProduct()


	def inputClient(self):
		self.name     = str(input("Nombre del cliente: "  ))
		self.apellido = str(input("Apellido del cliente: "))
		self.phone    = int(input("Celular/Telefono: "    ))
		self.address  = str(input("Direccion: "           ))


	def rentProduct(self, chmod=False):
		press = None
		global clientList
		listProducts()
		print("\n\t-=-=-=[ AGREGAR ALQUILER ]=-=-=-")
		
		while press != 'n':
			self.producto = str(input("\n\tPRODUCTO: "))
			self.amount = int(input("\tCANTIDAD: "  ))

			if self.producto in prices:
				self.product.append(self.producto)
				self.monto.append(prices[self.producto])
				self.cantidad.append(self.amount)
				self.subtotal.append(prices[self.producto] * self.amount)
			else:
				print("\t[!!] Producto no existe.\n")
			
			press = input("\n\t[Adicionar mas producto?](s/n): ")

		if chmod == False:
			self.saveClient()
		
		input("\n\tPresionar enter...")
		clear()
		self.printInformation()

		print("\n"+"="*45)
		print("\t-=-=-=[ ALQUILER AGREGADO ]=-=-=-")
		print("="*45)


	def saveClient(self):
		global clientList
		Client.ID += 1
		self.setState(True)
		clientList.append(Client(self.name,     self.apellido,
					 self.apellido, self.phone,
					 self.address,  self.monto,
					 self.total,    self.subtotal,
					 self.product,  self.cantidad))


	def printInformation(self):
		print("="*45)
		print("Nombre:",           self.getName(), self.getApellido())
		print("Telefono/Celular:", self.getPhone())
		print("Direccion:",        self.getAddress())
		print("Deposito:",         self.getDeposit())
		print("Estado:",           self.getState())
		print("ID:",               Client.ID)
		self.printProduct()


	def printProduct(self):
		print("\n"+"="*45)		
		print("\t-=-=-=-=ALQUILER=-=-=-=-")
		print("="*45)

		self.printItems = zip(self.getProduct(),
				      self.getCantidad(),
				      self.getSubtotal())

		print("PRODUCTO\t| Cantidad\t | Subtotal")
		print("="*45)
		
		for p, c, s in self.printItems:
			print(p, "\t  ", c,"\t\t  ", s)

		print("\t\t\t  TOTAL:    ",self.getTotal(),"lps.")
	

	def getState(self):
		if Client.STATE == True:
			return str("En alquiler")
		elif Client.STATE == False:
			return str("Entregado")


######################################################################
while choice != 6:
	print("\t" + """
	+============================+
	| INVERSIONES BONILLA TORRES |
	+============================+
	\tOpciones
	+============================+
	1) Crear alquiler
	2) Buscar alquiler
	3) Modificar alquiler
	4) Eliminar alquiler
	5) Mostrar precios
	6) Salir
	+============================+
	""")

	choice = int(input("\tIngrese la opcion: "))

	if choice < 1 or choice > 6:
		clear()
		print("\n\t[!!] La opcion es invalida.")
	elif choice <= 5:
		clear()
		if choice == 1:
			print("\n"+"="*45)
			print("\t-=-=-=CREAR ALQUILER=-=-=-")
			print("="*45)
			nombre   = str(input("Nombre del cliente: "  ))
			apellido = str(input("Apellido del cliente: "))
			phone    = int(input("Celular/Telefono: "    ))
			address  = str(input("Direccion: "           ))
			deposit  = str(input("Deposito: "            ))
			client = Client(nombre, apellido, phone, address, deposit)
			client.newRent()
		elif choice == 2:
			print("\n"+"="*45)
			print("\t-=-=-=BUSCAR ALQUILER=-=-=-")
			print("="*45)
			findClient()
		elif choice == 3:
			print("\n"+"="*45)
			print("\t-=-=-=MODIFICAR ALQUILER=-=-")
			print("="*45)
			findClient(True)
		elif choice == 4:
			print("\n"+"="*45)
			print("\t-=-=-=ELIMINAR ALQUIER=-=-=-")
			print("="*45)
		else:
			listProducts()
		
	
clear()

######################################################################
print("""\n\t+==============================+
\t| SISTEMA CERRADO EXITOSAMENTE |
\t+==============================+\n""")
