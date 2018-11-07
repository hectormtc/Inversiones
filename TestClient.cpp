#include <iostream>
#include "Inver.h"

using namespace std;
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
