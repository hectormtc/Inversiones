import os
choice = None

prices = {
	"sillaplastica"   : 4,
	"sillametalica"   : 5,
	"buffetmediana"   : 10,
	"buffetgrande"    : 20,
	"mantelredondo8"  : 10,
	"mantelredondo10" : 15,
	"sobremantel10"   : 15,
	"sobremantel8"    : 10,
	"mantelcuadrado"  : 50,
	"mesacuadrada"    : 20,
	"mesaredonda8"    : 20,
	"mesaredonda10"   : 25
}
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
	
	STATE = False	
	
	def __init__(self):
		self.client = str(input("Nombre del cliente: "))
		self.phone = int(input("Celular/Telefono: "))
		self.address = str(input("Direccion: "))
		self.deposit = int(input("Deposito: "))
		self.wallet = []
		self.total = []
		self.product = []
	
	def getClient(self):
		return self.client
	
	def getPhone(self):
		return self.phone
	
	def getAddress(self):
		return self.address
	
	def getDeposit(self):
		return self.deposit

	def inputClient(self):
		self.client = str(input("Nombre del cliente: "))
		self.phone = int(input("Celular/Telefono: "))
		self.address = str(input("Direccion: "))
		self.deposit = int(input("Deposito: "))

	def newRent(self):
		print("\n==========NUEVA RENTA==========\n")
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
			print(str(p),"\t ",str(t))
		total = sum(self.total)	
		print("\tTOTAL:   ",str(total),"lps.")
		print("===============================")

	def rentProduct(self):
		press = input("Agregar producto?(s/n): ")
		while press != 'n':
			listProducts()
			product = str(input("PRODUCTO: "))
			cantidad = int(input("CANTIDAD: "))
			if product in prices:
				self.wallet.append(product)
				self.wallet.append(cantidad)
			else:
				print("Producto no existe\n")
				press = input("Agregar producto...(s/n): ")
			press = input("Adicionar mas producto?(s/n): ")
		print("\n===============================")		
		print("\tALQUILER: ")
		print("===============================")
		self.func(self.wallet)
		input("\nPresionar enter...")
		clear()

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
			print("BUSCAR ALQUILER")
		elif choice == 3:
			print("MODIFICAR ALQUILER")
		elif choice == 4:
			print("ELIMINAR ALQUIER")
		elif choice == 5:
			listProducts()
		
	
clear()		
print("""+==============================+
| SISTEMA CERRADO EXITOSAMENTE |
+==============================+""")
