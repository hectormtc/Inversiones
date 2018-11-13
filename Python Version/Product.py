from Prices import *
from Utils import *

prices = Prices()


class Product(object):
	def __init__(self, monto=[], total=[], subtotal=[],
			   product=[], cantidad=[], printItems=()):
		self.monto      = monto
		self.total      = total
		self.subtotal   = subtotal
		self.product    = product
		self.cantidad   = cantidad
		self.printItems = printItems

	def inputProduct(self):
		self.producto = str(input("\n\tPRODUCTO: "))
		self.amount   = int(input("\tCANTIDAD: "  ))


	def rentProduct(self, chmod=False, quote=False):
		if chmod == True or quote == True:
			self.monto    = []
			self.total    = []
			self.subtotal = []
			self.product  = []
			self.cantidad = []
		
		press = None
		while press != 'n':
			#self.inputProduct()
			self.producto = 'silla'#str(input("\n\tPRODUCTO: "))
			self.amount   = 20 #int(input("\tCANTIDAD: "  ))

			if self.producto in prices.getPrices():
				self.setProduct(self.producto)
				self.setMonto(prices.getDict(self.producto))
				self.cantidad.append(self.amount)
				#self.subtotal.append(prices.setDict([self.producto] * self.amount))
			else:
				print("\t[!!] Producto no existe.\n")
			
			press = 'n'#press = input("\n\t[Adicionar mas producto?](s/n): ")

		self.setItems(self.getProduct(),
			      self.getCantidad(),
			      self.getSubtotal())

		if quote == True:
			self.printInformation(quote=True)


	#def printProduct(self):
		print("\n"+"="*45)		
		print("\t-=-=-=-=ALQUILER=-=-=-=-")
		print("="*45)
		
		print(self.getProduct())
		print(self.getMonto())
		print(self.getCantidad())

		for p in  self.getProduct():
			print("Product",p)

		print("PRODUCTO\t| Cantidad\t | Subtotal")
		print("="*45)
		
		for p, c, s in self.getItems():
			print(p, "\t  ", c,"\t\t  ", s)

		print("\t\t\t  TOTAL:    ",self.getTotal(),"lps.")

	#SETTERS
	def setItems(self, product, cantidad, subtotal):
		self.printItems = zip(product, cantidad, subtotal)
	
	def setMonto(self, value):
		self.monto.append(value)

	def setTotal(self, value):
		self.total.append(value)

	def setSubtotal(self, value):
		self.subtotal.append(value)

	def setProduct(self, item):
		self.product.append(item)

	def setCantidad(self, value):
		self.cantidad.append(value)
	
	#GETTERS

	def getItems(self):
		return self.printItems

	def getMonto(self):
		return self.monto

	def getTotal(self):
		return sum(self.subtotal)

	def getSubtotal(self):
		return self.subtotal

	def getProduct(self):
		return self.product

	def getCantidad(self):
		return self.cantidad
