#pragma once

#include "BankAccount.hpp"

#include <iostream>
#include <string>

struct Shop
{
    Shop(const std::string& name) : shopName(name)
    {
    }

    void buyApples(Debitable& debitable)
    {
        const unsigned price = 1999;
        std::cout << shopName << " sells an apple for " << price << " €" << std::endl;
        debitable.debit(price);
    }

private:
    std::string shopName;
};
