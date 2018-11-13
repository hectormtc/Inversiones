import sys
import os
from Utils import fatal


class Prices(object):

	PRICES = {}
	
	def __init__(self, dictPrices={}):
		self.dictPrices = dictPrices
		self.readProducts()


	def getPrices(self):
		return self.dictPrices


	def getDict(self, value):
		return self.dictPrices[value]


	def setDict(self, item, value):
		self.dictPrices[item] = value

	
	def readProducts(self):
		try:
			with open("PRODUCT.txt", 'r') as filename:
				for line in filename:
					read = line.split(",")
					PRODUCT, VALUE = read
					VALUE = float(VALUE)
					self.setDict(PRODUCT, VALUE)
					#self.dictPrices[str(PRODUCT)] = float(VALUE)
				filename.close()
		except IOError:
			fatal("leer productos.")


	def addProduct(self, PRODUCT, VALUE):
		try:
			with open("PRODUCT.txt", 'a+') as filename:
				filename.write(PRODUCT.lower()+","+str(VALUE)+"\n")
				self.dictPrices[str(PRODUCT)] = float(VALUE)
				filename.close()
		except IOError:
			fatal("agregar producto.")


	def listPrices(self):
		print("\n\t"+"="*32)
		print("""\tPRODUCTO\t| PRECIO""")
		print("\t"+"="*32)

		for product, price in self.dictPrices.items():
			print("\t" + str(product) + "\t| " + str(price))
		print("\t"+"="*32)


	def findProduct(self, item):
		print("""\tPRODUCTO\t| PRECIO""")
		for product, price in self.dictPrices.items():
			if item in self.dictPrices:
				print("\t" + str(product) + "\t| " + str(price) + " lps.")
				break

