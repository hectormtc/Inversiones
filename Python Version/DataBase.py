from Client import Client
from Utils import *

class DataBase(object):

	firstId = 1


	def __init__(self, clientList=[], delivered=[], received=[]):
		self.nextId     = DataBase.firstId
		self.delivered  = delivered
		self.received   = received
		self.clientList = clientList


	def addClient(self, fname, lname, addr, phone, depot):
		Client(self, fname, lname, addr, phone, depot)
		Client.setName(self, fname)
		Client.setLast(self, lname)
		Client.setId(self, self.nextId)
		self.incrementID()
		Client.inRent(self)
		self.clientList.append(Client())
		return self.clientList[0]


	def Cotization(self):
		Client.inputClient(self)


	def incrementID(self):
		self.nextId += 1


	def testClient(self):
		pass


	def getClientId(self,idClient):
		try:
			for client in self.clientList:
				if client.getID() == idClient:
					return client.printClient()
		except:
			fatal("buscar al cliente.")


	def getClient(self, fname, lname):
		try:
			for client in self.clientList:
				if client.getName() == fname and client.getLast() == lname:
					client.printClient()
		except:
			fatal("buscar al cliente.")


	def changeClientInfo(self, fname, lname):
		try:
			for client in self.clientList:
				if client.getName() == fname and client.getLast() == lname:
					client.inputClient()
		except:
			fatal("al modificar cliente.")


	def changeClientProduct(self, fname, lname):
		try:
			for client in self.clientList:
				if client.getName() == fname and client.getLast() == lname:
					client.inputClient()
		except:
			fatal("al modificar producto.")


	def recvRentId(self, idClient):
		try:
			for cliente in self.clientList:
				if client.getID() == idClient:
					client.notRent()
		except:
			fatal("al recibir cliente.")


	def recvRent(self, fname, lname):
		try:
			for client in self.clientList:
				if client.getName() == fname and client.getLast() == lname:
					client.notRent()
		except:
			fatal("al modificar producto.")


	def deleteClientId(self, idClient):
		try:
			for client in self.clientList:
				if client.getID() == idClient:
					clientList.remove(client)
		except:
			fatal("al eliminar cliente.")


	def deleteClient(self, fname, lname):
		try:
			for client in self.clientList:
				if client.getName() == fname and client.getLast() == lname:
					clientList.remove(client)
		except:
			fatal("al eliminar cliente.")


	def displayAll(self):
		for client in self.clientList:
			client.printClient()


	def displayOnRent(self):
		for client in self.clientList:
			if client.inRent():
				client.printClient()


	def displayNotPay(self):
		for client in self.clientList:
			if client.notPay():
				client.printClient()

