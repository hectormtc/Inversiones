#include <iostream>
#include <stdexcept>
#include "Database.h"

using namespace std;

namespace Records {
	
	Client& Database::addClient(const std::string& nm, const std::string& lastnam, const std::string& addr,const std::string& phn, const std::string& depot)
		{
			Client client(firstName, lastName);
			client.setId(mNextId++);
			client.inRent();
			mClient.push_back(client);
			return mClient[mClient.size() - 1];
		}

	Client& Database::getClient(int idClient)
	{
		for(auto& client : mClient) {
		    if(client.getId() == idClient) {
			return client;
		    };
		}
	throw logic_error("[!!] No se encontro el cliente.");
	}

	void Database::displayAll() const
	{
		for(const auto& client : mClient) {
			client.display();
		}
	}

	void Database::displayOnRent() const
	{
		for(const auto& client : mClient) {
			if(client.isRent())
				client.display();
		}
	}
	
}




