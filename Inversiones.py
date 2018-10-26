import os
import datetime

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

#LISTS
clientList      = []
clientDelivered = []
clientReceived  = []

#VARIABLES
global check
clientID        = 0


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
	input("\t\nPresionar enter...")


def showDelivered():
	for client in clientList:
		if client.STATE == True:
			print("[Cliente]",client.name, client.apellido)
	input("\t\nPresionar enter...")
	

######################################################################

def findClient(chmod=False, recv=False, delete=False):
	global clienList
	check = False
	select = None

	def check(state=False):
		if state == True:
			check = True
		else:
			pass

	def outList():
			print("\n"+"="*45)
			print("\n-=-=-=[ CLIENTE NO ENCOTRADO ]=-=-=-\n")
			input("\nPresionar enter...")
			clear()
	
	def deleteClient(client):
		clientList.remove(client)

	def find(name=False, apellido=False, phone=False):

		def nothing():
			pass

		def onList(client):
			print("\n"+"="*45)
			print("\n-=-=-=[ CLIENTE ENCONTRADO ]=-=-=-")
			print("[CLIENTES1]", client.name, client)
			
			if(chmod):
				print("\n-=-=-=[ CAMBIAR INFORMACION ]=-=-=-")
				client.printInformation()
				change = str(input("\t\nModificar alquiler?(s/n): "))

				if change == "s":
					client.newRent(True)

				clear()
				print("\n"+"="*45)
				print("\t-=-=-=[ ALQUILER MODIFICADO ]=-=-=-")
				print("="*45)

			elif recv == True:
				print("\n-=-=-=[ RECIBIR ALQUILER ]=-=-=-")
				client.printInformation()
				choice = str(input("\t\nRecibir alquiler?(s/n): "))
				
				if choice == "s":
					client.setState(False)

				clear()
				print("\n"+"="*45)
				print("\t-=-=-=[ ALQUILER RECIBIDO ]=-=-=-")
				print("="*45)
			
			elif delete == True:
				print("\n-=-=-=[ ELIMINAR ALQUILER ]=-=-=-")
				client.printInformation()
				choice = str(input("\t\nEliminar alquiler?(s/n): "))
				
				if choice == "s":
					deleteClient(client)
			
			else:
				client.printInformation()
				input("Presionar enter...")
				clear()
			check(True)


		if name == True:
			nameClient = str(input("\nNombre del cliente: "))
			
			for client in clientList:
				if nameClient == client.name:
					onList(client)
				else:
					nothing()

		elif apellido == True:
			apellidoClient = str(input("\nApellido del cliente: "))
			
			for client in clientList:
				onList(client) if apellidoClient == client.apellido else nothing()

		elif phone == True:
			phoneClient = int(input("\nNumero del cliente: "))
			
			for client in clientList:
				onList(client) if phoneClient == client.phone else nothing()

		outList() if check(False) else nothing()

	
	while select != 4:
		print("\n"+"="*45)

		if chmod == True:
			print("\t[ MODIFICAR CLIENTE ]\n")
		elif recv == True:
			print("\t[ RECIBIR CLIENTE ]\n")
		elif delete == True:
			print("\t[ ELIMINAR CLIENTE ]\n")
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
		else:
			clear()


######################################################################

class Client(object):
	def __init__(self, name, apellido, address, phone, deposit, ID,
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
		self.ID       = ID
		self.monto    = []
		self.total    = []
		self.subtotal = []
		self.product  = []
		self.cantidad = []
		self.STATE = False
	

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
		self.STATE = state

	def getID(self):
		return self.ID

	def getState(self):
		if self.STATE == True:
			return str("En alquiler")
		elif self.STATE == False:
			return str("Entregado")


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


	def rentProduct(self, chmod=False, quote=False):
		listProducts()

		if chmod == True or quote == True:
			self.monto    = []
			self.total    = []
			self.subtotal = []
			self.product  = []
			self.cantidad = []
		else:
			self.setState(True)
			
		print("\n\t-=-=-=[ AGREGAR ALQUILER ]=-=-=-")
		
		press = None
		while press != 'n':
			self.producto = str(input("\n\tPRODUCTO: "))
			self.amount   = int(input("\tCANTIDAD: "  ))

			if self.producto in prices:
				self.product.append(self.producto)
				self.monto.append(prices[self.producto])
				self.cantidad.append(self.amount)
				self.subtotal.append(prices[self.producto] * self.amount)
			else:
				print("\t[!!] Producto no existe.\n")
			
			press = input("\n\t[Adicionar mas producto?](s/n): ")
		
		clear()
		if quote == True:
			self.printInformation(quote=True)

		print("\n"+"="*45)
		print("\t-=-=-=[ ALQUILER AGREGADO ]=-=-=-")
		print("="*45)


	def printInformation(self, quote=False):
		if quote == False:
			print("="*45)
			print("Nombre:           ", self.getName(),
						    self.getApellido())
			print("Telefono/Celular: ", self.getPhone()   )
			print("Direccion:        ", self.getAddress() )
			print("Deposito:         ", self.getDeposit() )
			print("Estado:           ", self.getState()   )
			print("ID:               ", self.getID()      )
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
		input("\t\nPresionar enter...")


######################################################################

choice = None
while choice != 9:

	print("\t" + """
	+============================+
	| INVERSIONES BONILLA TORRES |
	+============================+
	\tOpciones
	+============================+
	1)  Crear     Alquiler
	2)  Buscar    Alquiler
	3)  Recibir   Alquiler
	4)  Modificar Alquiler
	5)  Eliminar  Alquiler
	6)  Mostrar   Precios
	7)  Mostrar   Pendientes
	8)  Crear     Cotizacion
	9)  Salir
	+============================+
	""")

	choice = int(input("\tIngrese la opcion: "))

	if choice < 1 or choice > 9:
		clear()
		print("\n\t[!!] La opcion es invalida.")
	
	elif choice <= 9:
		clear()
		
		if choice == 1:
			print("\n"+"="*45)
			print("\t-=-=-=CREAR ALQUILER=-=-=-")
			print("="*45)
			nombre   = str(input("Nombre del cliente  : "))
			apellido = str(input("Apellido del cliente: "))
			phone    = int(input("Celular/Telefono    : "))
			address  = str(input("Direccion           : "))
			deposit  = str(input("Deposito            : "))
			newClient = Client(nombre, apellido, phone, address, deposit, clientID)
			clientID += 1
			newClient.newRent()
			clientList.append(newClient)
			newClient = None
		
		elif choice == 2:
			print("\n"+"="*45)
			print("\t-=-=-=BUSCAR ALQUILER=-=-=-")
			print("="*45)
			findClient()
		
		elif choice == 3:
			print("\n"+"="*45)
			print("\t-=-=-=RECIBIR ALQUIER=-=-")
			print("="*45)
			findClient(recv=True)
		
		elif choice == 4:
			print("\n"+"="*45)
			print("\t-=-=-=MODIFICAR ALQUILER=-=-")
			print("="*45)
			findClient(chmod=True)

		elif choice == 5:
			print("\n"+"="*45)
			print("\t-=-=-=ELIMINAR ALQUILER=-=-")
			print("="*45)
			findClient(delete=True)

		elif choice == 6:
			listProducts()
		
		elif choice == 7:
			clear()
			print("\n"+"="*45)
			print("\t-=-=-=ALQUILERES PENDIENTES=-=-")
			print("="*45)
			showDelivered()

		elif choice == 8:
			print("\n"+"="*45)
			print("\t-=-=-=CREAR COTIZACION=-=-")
			print("="*45)
			quote = Client('', '','', '', '', '')
			quote.rentProduct(quote=True)

######################################################################

clear()
print("""\n\t+==============================+
\t| SISTEMA CERRADO EXITOSAMENTE |
\t+==============================+\n""")
