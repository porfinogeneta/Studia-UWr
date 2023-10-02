#pragma once

#include "Address.hpp"


#include <sstream>
#include <string>

class EventLog
{
public:
    EventLog(Storage& my_storage) : storage(my_storage)
    {
    }

    void log(const std::string& message)
    {
        std::stringstream buffer;
        buffer << "[" << (logsStored++) << "] " << message;
        storage.append(buffer.str());
    }

private:
    SqlStorage& storage;
    unsigned logsStored = 0;
};
