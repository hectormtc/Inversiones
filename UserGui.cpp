#include <iostream>
#include <stdexcept>
#include "Database.h"

using namespace std;
using namespace Records;

int displayMenu();
void displayOnRent(Database& db);
void doRent(Database&    db);
void doReceive(Database& db);
void doClient(Database&  db);
void doFind(Database&    db);
void doChange(Database&  db);
void doDelete(Database&  db);


int main() {

	Database clientDB;
	bool done = false;

	while(!done) {
		int selection = displayMenu();
		switch(selection) {
		case 0:
			done = true;
			break;
		case 1:
			doClient(clientDB);	
			break;
		case 2;
			doFind(clientDB);
			break;
		case 3:
			doRecive(clientDB);
			break;
		case 4:
			doChange(clientDB);
			break;
		case 5:
			doDelete(clientDB);
			break;
		case 6:
			displayOnRent(clientDB);
			break;

		default:
			cerr << "[!!] Opcion no valida." << endl;
			break;
		}
	}
	return 0;
}

int displayMenu() {

	int selection;

	cout << "+============================+	" << endl;
	cout << "| INVERSIONES BONILLA TORRES |	" << endl;
	cout << "+============================+	" << endl;
	cout << "\tOpciones			" << endl;
	cout << "+============================+	" << endl;
	cout << "1)  Crear     Alquiler		" << endl;
	cout << "2)  Buscar    Alquiler		" << endl;
	cout << "3)  Recibir   Alquiler		" << endl;
	cout << "4)  Modificar Alquiler		" << endl;
	cout << "5)  Eliminar  Alquiler		" << endl;
	cout << "6)  Mostrar   Precios		" << endl;
	cout << "7)  Mostrar   Pendientes	" << endl;
	cout << "8)  Crear     Cotizacion	" << endl;
	cout << "0)  Salir		       	" << endl;
	cout << "+============================+	" << endl;
	cout << "Opcion---> ";
	cin  >> selection;
	return selection;
}
