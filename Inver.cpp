#include <iostream>
#include "Inver.h"

using namespace std;

namespace Records {

	Client::Client(const std::string& nm,    const string& lastnam,
		       const std::string& addr,  const string& phn,
		       const std::string& depot)
		: name(nm),  lastname(lastnam),  address(addr), phone(phn), deposit(depot)
		{
		}


	void Client::printInfo() const
	{
		cout << "Nombre    : " << getName() << " " << getLast() << endl;
		cout << "Estado    : " << (isRent() ? "En Alquiler": "Entregado") << endl;
		cout << "Celular   : " << getPhone() << endl;
		cout << "Direccion : " << getAddress() << endl;
		cout << "Deposit   : " << getDeposit() << endl;
		//cout << "ID        : " << getId() << endl;
		cout << endl;
	}


	void Client::inRent()
	{
		STATE = true;
	}

	void Client::notRent()
	{
		STATE = false;
	}

	//Getters
	const string& Client::getName() const
	{ 
		return name;
	}

	const string& Client::getLast() const
	{
		return lastname;
	}

	const string& Client::getAddress() const
	{ 
		return address;
	}

	const string& Client::getPhone() const
	{
		return phone;
	}

	const string& Client::getDeposit() const
	{
		return deposit;  
	}
/*
	int Client::getId() const
	{
		return idClient;
	}
*/
	//Setters
	void Client::setName(const string& nm)
	{
		name = nm;
	}

	void Client::setLast(const string& lname)
	{
		lastname = lname;
	}

	void Client::setAddress(const string& addr)
	{
		address = addr;
	}

	void Client::setPhone(const string& phn)
	{
		phone = phn;
	}

	void Client::setDeposit(const string& depot)
	{
		deposit = depot;
	}
/*
	void Client::setId(int idNumber)
	{
		idClient = idNumber;
	}
*/
	bool Client::isRent() const
	{
		return STATE;
	}
}

using namespace Records;

int main() {

	cout << "Testing the Client Class." << endl;

	Client c;
	c.setName("Hector");
	c.setLast("Torres");
	c.setAddress("Barrio la hoya");
	c.setPhone("278123");
	c.setDeposit("200");
	c.isRent();
	c.printInfo();

	return 0;
}
