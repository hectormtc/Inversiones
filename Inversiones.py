import os
from product import prices

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

	def find(name=None, apellido=None, phone=None):
		for client in clientList:
			if name:
				if name == client.name:
					print("Cliente encontrado")
				else:
					print("Cliente no encontrado")
			if apellido:
				if apellido == client.apellido:
					print("Cliente encontrado")
					print(client.apellido)
				else:
					print("Cliente no encontrado")
			if phone:
				if phone == client.phone:
					print("Cliente encontrado")
				else:
					print("Cliente no encontrado")
	
	print("BUSCAR AL CLIENTE POR:\n")
	print(" 1) Nombre\n 2) Apellido\n 3) Telefono")
	print("\n===============================")

	select = int(input("Opcion: "))
	if select == 1:
		name= str(input("Escriba el nombre del cliete: "))
		find(name=name)
	elif select == 2:
		apellido = str(input("Escriba el apellido del cliente: "))
		find(apellido=apellido)
	elif select == 3:
		phone = int(input("Escriba el numero del cliente: "))
		find(phone=phone)


class Client(object):
	
	ID = 0
	STATE = None
	
	def __init__(self, name, apellido, address, deposit, phone):
		self.name =       name
		self.apellido =   apellido
		self.address =    address
		self.phone =      phone
		self.deposit =    deposit
		self.wallet =     []
		self.total =      []
		self.subtotal =   []
		self.product =    []
		self.cantidad =   []
	

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
		Client.State = state


	def getState(self):
		if Client.State == True:
			return str("En alquiler")
		elif Client.State == False:
			return str("Entregado")


	def inputClient(self):
		self.name = str(input("Nombre del cliente: "))
		self.apellido = str(input("Apellido del cliente: "))
		self.phone = int(input("Celular/Telefono: "))
		self.address = str(input("Direccion: "))
		self.deposit = int(input("Deposito: "))


	def newRent(self):
		self.inputClient()
		self.rentProduct()
		print("===============================")
		print("\tALQUILER AGREGADO")
		print("===============================")


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

		printItems = zip(self.total, self.product, self.cantidad)

		print("PRODUCTO\t| Cantidad\t | Subtotal")
		print("="*45)
		
		for t, p, c in printItems:
			print(str(p), "\t  ", str(c),"\t\t  ", str(t))

		print("\t\t\t  TOTAL:    ",sum(self.subtotal),"lps.")
		print("="*45)
		self.setState(True)


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
				press = input("Agregar producto...(s/n): ")
			press = input("Adicionar mas producto?(s/n): ")
		
		self.func(self.wallet)
		self.printProduct()
		self.saveClient()
		input("\nPresionar enter...")
		clear()
		self.printInformation()
		
	def saveClient(self):
		Client.ID += 1
		client = Client(self.name, self.apellido, self.address, self.deposit, self.phone)
		clientList.append(client)

	def printInformation(self):
		print("\n===============================")
		print("Nombre:", self.getName(), self.getApellido())
		print("Telefono/Celular:", self.getPhone())
		print("Direccion:", self.getAddress())
		print("Deposito:", self.getDeposit())
		print("Estado:", self.getState())
		


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
			Client('','','','','').newRent()
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
