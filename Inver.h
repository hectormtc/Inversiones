#pragma once

#include <string>

namespace Records {

	class Client
	{
	    public:
		Client() = default;
		Client(const std::string& nm, const std::string& lastnam, const std::string& addr,const std::string& phn, const std::string& depot);

		void printInfo() const;
		void inRent(); //Hire
		void notRent();
		bool isRent() const;

		void setName(const    std::string& nm);
		void setLast(const    std::string& lname);
		void setAddress(const std::string& addr);
		void setPhone(const   std::string& phn);
		void setDeposit(const std::string& depot);
		void setId(int idNumber);
		
		const std::string& getName() const;
		const std::string& getLast() const;
		const std::string& getAddress() const;
		const std::string& getPhone() const;
		const std::string& getDeposit()const;
		//const int getId() const;
		

	    private:
		int idClient = -1;
		std::string name;
		std::string lastname;
		std::string address;
		std::string phone;
		std::string deposit;
		bool STATE = false;
	};
}
