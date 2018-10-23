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

def clear():
	os.system('clear')

clear()


def listProducts():
	print("\t"+"="*32)
	print("""\tPRODUCTO\t| PRECIO""")
	print("\t"+"="*32)

	for product, price in prices.items():
		print("\t"+str(product)+"\t| "+str(price)+" lps.")
	print("\t"+"="*32)
	input("Presionar enter...")


def findClient():
	global clienList
		
	def find(name=False, apellido=False, phone=False):
		def onList():
			print("\n[Cliente encontrado]")
			client.printInformation()
		
		def outList():
			print("\n[Cliente no encontrado]")

		if name:
			name= str(input("Escriba el nombre del cliente: "))
			for client in clientList:
				if (name == client.name):
					onList()
				else:
					pass
		if apellido:
			apellido = str(input("Escriba el apellido del cliente: "))
			for client in clientList:
				if (apellido == client.apellido):
					onList()
				else:
					pass
		if phone:
			phone = int(input("Escriba el numero del cliente: "))
			for client in clientList:
				if (phone == client.phone):
					onList()
				else:
					pass
		else:
			input("Presionar enter...")
	
	print("BUSCAR AL CLIENTE POR:\n")
	print(" 1) Nombre\n 2) Apellido\n 3) Telefono")
	print("\n===============================")

	select = int(input("Opcion: "))
	if select == 1:
		find(name=True)
	elif select == 2:
		find(apellido=True)
	elif select == 3:
		find(phone=True)


class Client(object):
	
	ID = 0
	STATE = False
	
	def __init__(self, name, apellido, address, phone, deposit, wallet, total, subtotal, product, cantidad):
		self.name =       name
		self.apellido =   apellido
		self.address =    address
		self.phone =      phone
		self.deposit =    deposit
		self.listNumbers()

	def listNumbers(self):
		self.wallet =     []
		self.total =      []
		self.subtotal =   []
		self.product =    []
		self.cantidad =   []

	def getWallet(self):
		return self.wallet

	def getTotal(self):
		return self.total

	def getSubtotal(self):
		return sum(self.subtotal)

	def getProduct(self):
		return self.product
	
	def getCantidad(self):
		return self.cantidad

	def getName(self):
		return self.name

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

	def getState(self):
		if Client.STATE == True:
			return str("En alquiler")
		elif Client.STATE == False:
			return str("Entregado")


	def inputClient(self):
		self.name = str(input("Nombre del cliente: "))
		self.apellido = str(input("Apellido del cliente: "))
		self.phone = int(input("Celular/Telefono: "))
		self.address = str(input("Direccion: "))
		self.deposit = int(input("Deposito: "))


	def newRent(self):
		self.listNumbers()
		self.inputClient()
		self.rentProduct()


	def func(self, wallet):
		for item in wallet:
			if isinstance(item, int):
				self.total.append(item)
			elif isinstance(item, str):
				self.product.append(item)

	def printProduct(self):
		print("\n"+"="*45)		
		print("\t-=-=-=-=ALQUILER=-=-=-=-")
		print("="*45)

		printItems = zip(self.getTotal(), self.getProduct(), self.getCantidad())

		print("PRODUCTO\t| Cantidad\t | Subtotal")
		print("="*45)
		
		for t, p, c in printItems:
			print(p, "\t  ", c,"\t\t  ", t)

		print("\t\t\t  TOTAL:    ",self.getSubtotal(),"lps.")
		print("="*45)


	def rentProduct(self):
		listProducts()
		press = None
		global clientList
		
		while press != 'n':
			product = str(input("\nPRODUCTO: "))
			cantidad = int(input("CANTIDAD: "))
			if product in prices:
				self.wallet.append(product)
				self.wallet.append(cantidad)
				self.cantidad.append(prices[product])
				self.subtotal.append(prices[product] * cantidad)
			else:
				print("Producto no existe\n")
			press = input("Adicionar mas producto?(s/n): ")
		
		self.func(self.wallet)
		self.saveClient()
		input("\nPresionar enter...")
		clear()
		self.printInformation()
		print("\n"+"="*45)
		print("\tALQUILER AGREGADO")
		print("="*45)
		
	def saveClient(self):
		Client.ID += 1
		self.setState(True)
		client = Client(self.name,self.apellido,self.address,
				self.phone,self.deposit, self.wallet,
				self.total,self.subtotal,self.product,self.cantidad)
		clientList.append(client)

	def printInformation(self):
		print("\n===============================")
		print("Nombre:", self.getName(), self.getApellido())
		print("Telefono/Celular:", self.getPhone())
		print("Direccion:", self.getAddress())
		print("Deposito:", self.getDeposit())
		print("Estado:", self.getState())
		print(self.printProduct())


while choice != 6:
	print("""
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

	choice = int(input("Ingrese la opcion: "))

	if choice < 1 or choice > 6:
		clear()
		print("\n[!!] La opcion es invalida.")
	elif choice <= 5:
		clear()
		if choice == 1:
			print("==========CREAR ALQUILER==========\n")
			Client('','','','','','','','','','').newRent()
		elif choice == 2:
			print("==========BUSCAR ALQUILER==========\n")
			findClient()
		elif choice == 3:
			print("==========MODIFICAR ALQUILER==========\n")
		elif choice == 4:
			print("==========ELIMINAR ALQUIER==========\n")
		elif choice == 5:
			listProducts()
		
	
clear()
	
print("""+==============================+
| SISTEMA CERRADO EXITOSAMENTE |
+==============================+""")
