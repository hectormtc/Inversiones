from Utils import *
from Manager import *

def CreatRent():
	print("\n"+"="*45)
	print("\t-=-=-=CREAR ALQUILER=-=-=-")
	print("="*45)
	fname   = str(input("Nombre del cliente  : "))
	lname   = str(input("Apellido del cliente: "))
	phone   = str(input("Celular/Telefono    : "))
	address = str(input("Direccion           : "))
	deposit = str(input("Deposito            : "))
	DataBase.addClient(fname, lname, phone, address, deposit)
	print("\n"+"="*45)
	print("\t-=-=-=CLIENTE AGREGADO=-=-=-")
	print("="*45)


def main():
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
		5)  Pendiente Alquiler
		6)  Pendiente Pagos
		7)  Mostrar   Precios
		8)  Crear     Cotizacion
		9)  Salir
		+============================+
		""")

		choice = int(input("\t-->Opcion: "))

		if choice < 1 or choice > 9:
			clear()
			print("\n\t[!!] La opcion es invalida.")
		
		elif choice <= 9:
			clear()
			
			if choice == 1:
				cretRent()
			
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
