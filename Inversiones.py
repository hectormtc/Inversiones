import os
from product import prices

choice = None

def listProducts():
	print("\t"+"="*32)
	print("""\tPRODUCTO\t| PRECIO""")
	print("\t"+"="*32)

	for product, price in prices.items():
		print("\t"+str(product)+"\t| "+str(price)+" lps.")
	print("\t"+"="*32)
	input("Presionar enter...")


def clear():
	os.system('clear')

clear()


class Client(object):
	
	STATE = None
	
	def __init__(self):
		self.name =       None
		self.apellido =   None
		self.address =    None
		self.deposit =    None
		self.wallet =     []
		self.total =      []
		self.subtotal =   []
		self.product =    []
		self.clientList = []
	

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
		
		printItems = zip(self.total, self.product)

		print("PRODUCTO\t| Cantidad")
		print("===============================")
		
		for t, p in printItems:
			print(str(p), "\t ", str(t),"\t ")

		print("\tTOTAL:   ",sum(self.subtotal),"lps.")
		print("===============================")
		self.setState(True)


	def rentProduct(self):
		listProducts()
		press = None
		
		while press != 'n':
			product = str(input("\nPRODUCTO: "))
			cantidad = int(input("CANTIDAD: "))
			if product in prices:
				self.wallet.append(product)
				self.wallet.append(cantidad)
				self.subtotal.append(prices[product] * cantidad)
			else:
				print("Producto no existe\n")
				press = input("Agregar producto...(s/n): ")
			press = input("Adicionar mas producto?(s/n): ")
		
		print("\n===============================")		
		print("\tALQUILER: ")
		print("===============================")
		
		self.func(self.wallet)
		self.clientList.append(Client)
		input("\nPresionar enter...")
		clear()
		self.printInformation()

	def printInformation(self):
		print("\n===============================")
		print("Nombre:", self.getName(), self.getApellido())
		print("Telefono/Celular:", self.getPhone())
		print("Direccion:", self.getAddress())
		print("Deposito:", self.getDeposit())
		print("Estado:", self.getState())


	def findClient(self, name=None, apellido=None, phone=None):
		print("""
	BUSCAR AL CLIENTE POR:

	1) Nombre
	2) Apellido
	3) Telefono""")

		select = int(input("Opcion: "))
		if select == 1:
			name = str(input("Escriba el nombre del cliente: "))
			for a in self.clientList:
				if a.getName() == name:
					print("Cliente encontrado")
				else:
					print("No funciona") 
		elif select == 2:
			pass
		elif select == 3:
			pass

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
			Client().newRent()
		elif choice == 2:
			print("==========BUSCAR ALQUILER==========\n")
			Client().findClient()
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
