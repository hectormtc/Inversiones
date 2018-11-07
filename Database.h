#pragma once
#include <iostream>
#include <vector>
#include "Inver.h"

namespace Records {
	const int firstId = 1;

	class Database
	{
	    public:

		Client& addClient(const std::string& nm, const std::string& lastnam, const std::string& addr,const std::string& phn, const std::string& depot);

		Client& addClient() = default;
		Client& getClient(int idClient);
		Client& getClient(const std::string& firstName,
				  const std::string& lastName);
		
		void displayAll() const;
		void displayOnRent() const;
		void receivedRent();

	    private:
		std::vector<Client> mClient;
		int mNextId = firstId;
    };
}
































