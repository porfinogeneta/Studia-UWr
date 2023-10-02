#pragma once

#include <iostream>
#include <string>
#include "./solution/Debitable.hpp"
#include "./solution/MoneyTransferTarget.hpp"
#include "./solution/OwnedAccount.hpp"

class BankAccount : public Debitable, public MoneyTransferTarget, public OwnedAccount
{
public:
    bool debit(unsigned amount) override
    {
        if (amount > currentBalance)
        {
            return false;
        }

        currentBalance -= amount;
        return true;
    }

    void credit(unsigned deposit) override
    {
        currentBalance += deposit;
    }

    int balance() const override
    {
        return currentBalance;
    }

private:
    int currentBalance = 0;
};
