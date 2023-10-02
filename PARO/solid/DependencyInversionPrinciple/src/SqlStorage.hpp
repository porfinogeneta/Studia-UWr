#pragma once

#include "Address.hpp"
#include "./solution/Storage.hpp"

#include <iostream>
#include <string>

class SqlStorage : public Storage
{
public:
    SqlStorage(const Address& address) : address(address)
    {
        std::cout << "Established connection to SQL server at " << address << std::endl;
    }

    void append(const std::string& entry) override
    {
        std::cout << "SQL@" << address << " <- " << entry << std::endl;
    }

private:
    Address address;
};
